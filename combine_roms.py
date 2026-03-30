#!/usr/bin/env python3
"""
=============================================================================
  Sonic Classic Trilogy - Ultimate Complete
  ROM Combiner Script for Sega Mega Drive / Genesis
=============================================================================
  Tool Used  : Esrael Sonic Editor II
  Created by : Esrael Neto © 2026
  Output     : Sonic Classic Trilogy - Ultimate Complete.bin (64 MB)
=============================================================================

  Combines:
    1. Sonic The Hedgehog      (USA, Europe) - 512 KB
    2. Sonic The Hedgehog 2    (World)       - 1.0 MB
    3. Sonic The Hedgehog 3 & Knuckles (World) - 4.0 MB

  Final ROM Layout (64 MB / 67,108,864 bytes):
    0x000000 - 0x07FFFF  → Sonic 1        ( 512 KB)
    0x080000 - 0x17FFFF  → Sonic 2        (1.0 MB)
    0x180000 - 0x57FFFF  → Sonic 3 & K    (4.0 MB)
    0x580000 - 0x3FFFFFF → Padding/Free   (remaining to 64 MB)
=============================================================================
"""

import os
import sys
import struct
import hashlib

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))

ROM_SONIC1   = os.path.join(SCRIPT_DIR, "Sonic The Hedgehog (USA, Europe).bin")
ROM_SONIC2   = os.path.join(SCRIPT_DIR, "Sonic The Hedgehog 2 (World).bin")
ROM_SONIC3K  = os.path.join(SCRIPT_DIR, "Sonic The Hedgehog 3 & Knuckles (World).bin")

OUTPUT_ROM   = os.path.join(SCRIPT_DIR, "Sonic Classic Trilogy - Ultimate Complete.bin")

TARGET_SIZE  = 64 * 1024 * 1024   # 64 MB  = 67,108,864 bytes
PADDING_BYTE = 0xFF                 # Standard Genesis ROM padding

# Expected sizes for validation
EXPECTED_SIZES = {
    ROM_SONIC1:  524288,    # 512 KB
    ROM_SONIC2:  1048576,   # 1.0 MB
    ROM_SONIC3K: 4194304,   # 4.0 MB
}

# ─────────────────────────────────────────────
#  GENESIS ROM HEADER FIELDS  (offset 0x100)
# ─────────────────────────────────────────────

HEADER_CONSOLE_NAME   = b"SEGA MEGA DRIVE "        # 16 bytes  0x100
HEADER_COPYRIGHT      = b"(C)ESRAEL 2026.JAN"      # 16 bytes  0x110  (padded below)
HEADER_DOMESTIC_NAME  = b"SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE       "  # 48 bytes 0x120
HEADER_OVERSEAS_NAME  = b"SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE       "  # 48 bytes 0x150
HEADER_SERIAL         = b"GM T-000000-00"           # 14 bytes  0x180
HEADER_CHECKSUM       = 0x0000                       # 2  bytes  0x18E  (recalculated)
HEADER_IO_SUPPORT     = b"JD              "         # 16 bytes  0x190
HEADER_ROM_START      = 0x00000000                   # 4  bytes  0x1A0
HEADER_ROM_END        = TARGET_SIZE - 1              # 4  bytes  0x1A4
HEADER_RAM_START      = 0x00FF0000                   # 4  bytes  0x1A8
HEADER_RAM_END        = 0x00FFFFFF                   # 4  bytes  0x1AC
HEADER_SRAM_TYPE      = b"    "                      # 4  bytes  0x1B0
HEADER_SRAM_START     = 0x00000000                   # 4  bytes  0x1B4
HEADER_SRAM_END       = 0x00000000                   # 4  bytes  0x1B8
HEADER_NOTES          = b"ESRAEL SONIC EDITOR II - ROM HACK               "  # 48 bytes 0x1BC (padded)
HEADER_REGION         = b"JUE             "         # 16 bytes  0x1F0

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def pad_or_trim(data: bytes, length: int, pad_byte: int = 0x20) -> bytes:
    """Pad with spaces (0x20) or trim to exact byte length."""
    return (data + bytes([pad_byte] * length))[:length]

def calculate_checksum(rom_data: bytes) -> int:
    """
    Standard Sega Genesis ROM checksum.
    Sum all 16-bit words from offset 0x200 onward, keep lower 16 bits.
    """
    checksum = 0
    for i in range(0x200, len(rom_data) - 1, 2):
        word = (rom_data[i] << 8) | rom_data[i + 1]
        checksum = (checksum + word) & 0xFFFF
    return checksum

def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def print_banner():
    print("=" * 70)
    print("  🦔  SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE  🦔")
    print("       ROM Combiner for Sega Mega Drive / Genesis")
    print("       Tool : Esrael Sonic Editor II")
    print("       By   : Esrael Neto  ©  2026")
    print("=" * 70)

def print_section(title: str):
    print(f"\n{'─' * 70}")
    print(f"  {title}")
    print(f"{'─' * 70}")

# ─────────────────────────────────────────────
#  VALIDATION
# ─────────────────────────────────────────────

def validate_roms() -> bool:
    """Check that all three source ROMs exist and are the correct size."""
    print_section("📂  VALIDATING SOURCE ROMs")
    all_ok = True
    for path, expected in EXPECTED_SIZES.items():
        name = os.path.basename(path)
        if not os.path.isfile(path):
            print(f"  ❌  MISSING  : {name}")
            all_ok = False
            continue
        actual = os.path.getsize(path)
        status = "✅" if actual == expected else "⚠️ "
        size_kb = actual // 1024
        exp_kb  = expected // 1024
        print(f"  {status}  {name}")
        print(f"       Size   : {actual:,} bytes  ({size_kb} KB)")
        if actual != expected:
            print(f"       Expected: {expected:,} bytes ({exp_kb} KB)  ← SIZE MISMATCH")
            all_ok = False
    return all_ok

# ─────────────────────────────────────────────
#  ROM HEADER BUILDER
# ─────────────────────────────────────────────

def build_header(checksum: int = 0x0000) -> bytes:
    """
    Build a complete 256-byte Sega Genesis ROM header (0x100 – 0x1FF).
    Offsets are relative to the START of the header block.
    """
    header = bytearray(256)

    # 0x000  Console Name        (16 bytes)
    header[0x00:0x10] = pad_or_trim(HEADER_CONSOLE_NAME, 16)
    # 0x010  Copyright           (16 bytes)
    header[0x10:0x20] = pad_or_trim(HEADER_COPYRIGHT, 16)
    # 0x020  Domestic Name       (48 bytes)
    header[0x20:0x50] = pad_or_trim(HEADER_DOMESTIC_NAME, 48)
    # 0x050  Overseas Name       (48 bytes)
    header[0x50:0x80] = pad_or_trim(HEADER_OVERSEAS_NAME, 48)
    # 0x080  Serial Number       (14 bytes)
    header[0x80:0x8E] = pad_or_trim(HEADER_SERIAL, 14)
    # 0x08E  Checksum            (2  bytes, big-endian)
    struct.pack_into(">H", header, 0x8E, checksum)
    # 0x090  I/O Support         (16 bytes)
    header[0x90:0xA0] = pad_or_trim(HEADER_IO_SUPPORT, 16)
    # 0x0A0  ROM Start Address   (4  bytes, big-endian)
    struct.pack_into(">I", header, 0xA0, HEADER_ROM_START)
    # 0x0A4  ROM End Address     (4  bytes, big-endian)
    struct.pack_into(">I", header, 0xA4, HEADER_ROM_END)
    # 0x0A8  RAM Start           (4  bytes)
    struct.pack_into(">I", header, 0xA8, HEADER_RAM_START)
    # 0x0AC  RAM End             (4  bytes)
    struct.pack_into(">I", header, 0xAC, HEADER_RAM_END)
    # 0x0B0  SRAM Type           (4  bytes)
    header[0xB0:0xB4] = pad_or_trim(HEADER_SRAM_TYPE, 4)
    # 0x0B4  SRAM Start          (4  bytes)
    struct.pack_into(">I", header, 0xB4, HEADER_SRAM_START)
    # 0x0B8  SRAM End            (4  bytes)
    struct.pack_into(">I", header, 0xB8, HEADER_SRAM_END)
    # 0x0BC  Notes               (48 bytes)
    header[0xBC:0xEC] = pad_or_trim(HEADER_NOTES, 48)
    # 0x0F0  Region              (16 bytes)
    header[0xF0:0x100] = pad_or_trim(HEADER_REGION, 16)

    return bytes(header)

# ─────────────────────────────────────────────
#  COMBINE ROMs
# ─────────────────────────────────────────────

def combine_roms():
    """Main function: read, combine, patch header, pad, write."""

    print_banner()

    # ── 1. Validate ──────────────────────────────────────────────────────
    if not validate_roms():
        print("\n  ❌  Validation failed. Please check the ROM files above.")
        sys.exit(1)

    # ── 2. Load ROMs ─────────────────────────────────────────────────────
    print_section("📥  LOADING ROMs")

    with open(ROM_SONIC1,  "rb") as f: data_s1  = f.read()
    with open(ROM_SONIC2,  "rb") as f: data_s2  = f.read()
    with open(ROM_SONIC3K, "rb") as f: data_s3k = f.read()

    print(f"  🔵  Sonic 1        : {len(data_s1):>10,} bytes  ({len(data_s1)//1024} KB)  MD5: {md5(data_s1)}")
    print(f"  🔴  Sonic 2        : {len(data_s2):>10,} bytes  ({len(data_s2)//1024} KB)  MD5: {md5(data_s2)}")
    print(f"  🟡  Sonic 3 & K    : {len(data_s3k):>10,} bytes  ({len(data_s3k)//1024//1024} MB)   MD5: {md5(data_s3k)}")

    # ── 3. ROM Layout ────────────────────────────────────────────────────
    print_section("🗺️   ROM LAYOUT  (64 MB)")

    offset_s1  = 0x000000
    offset_s2  = offset_s1  + len(data_s1)
    offset_s3k = offset_s2  + len(data_s2)
    offset_end = offset_s3k + len(data_s3k)

    print(f"  Offset 0x{offset_s1:07X} – 0x{offset_s2-1:07X}  │ Sonic 1        {len(data_s1)//1024:>5} KB")
    print(f"  Offset 0x{offset_s2:07X} – 0x{offset_s3k-1:07X}  │ Sonic 2        {len(data_s2)//1024:>5} KB")
    print(f"  Offset 0x{offset_s3k:07X} – 0x{offset_end-1:07X}  │ Sonic 3 & K  {len(data_s3k)//1024//1024:>5} MB")
    print(f"  Offset 0x{offset_end:07X} – 0x{TARGET_SIZE-1:07X}  │ Padding (0xFF) {(TARGET_SIZE-offset_end)//1024//1024:>5} MB")
    print(f"\n  Total Target Size : {TARGET_SIZE:,} bytes  (64 MB)")

    # ── 4. Assemble raw ROM ───────────────────────────────────────────────
    print_section("🔧  ASSEMBLING ROM")

    rom = bytearray(TARGET_SIZE)
    rom[:] = bytes([PADDING_BYTE]) * TARGET_SIZE      # fill with 0xFF first

    # Copy ROMs in order
    rom[offset_s1  : offset_s1  + len(data_s1) ] = data_s1
    rom[offset_s2  : offset_s2  + len(data_s2) ] = data_s2
    rom[offset_s3k : offset_s3k + len(data_s3k)] = data_s3k

    print(f"  ✅  Sonic 1       copied  @ 0x{offset_s1:07X}")
    print(f"  ✅  Sonic 2       copied  @ 0x{offset_s2:07X}")
    print(f"  ✅  Sonic 3 & K   copied  @ 0x{offset_s3k:07X}")
    print(f"  ✅  Padding       applied  0x{offset_end:07X} → 0x{TARGET_SIZE-1:07X}")

    # ── 5. Patch the Trilogy ROM Header at 0x100 ─────────────────────────
    print_section("📝  WRITING ROM HEADER  (offset 0x100)")

    header_bytes = build_header(checksum=0x0000)   # placeholder checksum
    rom[0x100:0x200] = header_bytes

    # ── 6. Calculate & embed checksum ────────────────────────────────────
    checksum = calculate_checksum(bytes(rom))
    struct.pack_into(">H", rom, 0x18E, checksum)
    print(f"  ✅  Console Name  : {bytes(rom[0x100:0x110]).decode('ascii', errors='replace').strip()}")
    print(f"  ✅  Copyright     : {bytes(rom[0x110:0x120]).decode('ascii', errors='replace').strip()}")
    print(f"  ✅  Domestic Name : {bytes(rom[0x120:0x150]).decode('ascii', errors='replace').strip()}")
    print(f"  ✅  Overseas Name : {bytes(rom[0x150:0x180]).decode('ascii', errors='replace').strip()}")
    print(f"  ✅  Serial        : {bytes(rom[0x180:0x18E]).decode('ascii', errors='replace').strip()}")
    print(f"  ✅  Checksum      : 0x{checksum:04X}")
    print(f"  ✅  ROM End Addr  : 0x{TARGET_SIZE-1:08X}")
    print(f"  ✅  Region        : {bytes(rom[0x1F0:0x200]).decode('ascii', errors='replace').strip()}")

    # ── 7. Write output ───────────────────────────────────────────────────
    print_section("💾  WRITING OUTPUT ROM")

    with open(OUTPUT_ROM, "wb") as f:
        f.write(rom)

    final_size = os.path.getsize(OUTPUT_ROM)
    final_md5  = hashlib.md5(bytes(rom)).hexdigest()

    print(f"  ✅  Output File   : {os.path.basename(OUTPUT_ROM)}")
    print(f"  ✅  Final Size    : {final_size:,} bytes  ({final_size // 1024 // 1024} MB)")
    print(f"  ✅  MD5 Checksum  : {final_md5}")

    # ── 8. Summary ────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("  🎮  COMBINATION COMPLETE!")
    print("=" * 70)
    print(f"""
  📦  Output ROM   : Sonic Classic Trilogy - Ultimate Complete.bin
  📐  Size         : {final_size:,} bytes  (64 MB)
  🎮  Platform     : Sega Mega Drive / Genesis
  🔧  Tool Used    : Esrael Sonic Editor II
  👤  Created by   : Esrael Neto  ©  2026

  🗂️   ROM Contents:
       [1]  🔵  Sonic The Hedgehog           @ 0x{offset_s1:07X}  (512 KB)
       [2]  🔴  Sonic The Hedgehog 2         @ 0x{offset_s2:07X}  (1.0 MB)
       [3]  🟡  Sonic The Hedgehog 3 & K     @ 0x{offset_s3k:07X}  (4.0 MB)

  ✅  Ready to use with any Sega Mega Drive / Genesis emulator!
  ✅  Compatible with flash cartridges (Everdrive, MegaSD, etc.)
""")
    print("=" * 70)


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    combine_roms()