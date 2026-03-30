# 🛠️ Sonic Classic Trilogy — Ultimate Complete
## How to Combine ROMs for Sega Mega Drive / Genesis
### Full Step-by-Step Combination Guide

---

> **Tool Used:** Esrael Sonic Editor II
> **Created by:** Esrael Neto © 2026
> **Output:** `Sonic Classic Trilogy - Ultimate Complete.bin` — **64 MB**

---

## 📋 Overview

This guide explains in full detail how to combine three classic Sonic the Hedgehog ROMs into a single **64 MB** Sega Mega Drive / Genesis ROM file called:

```
Sonic Classic Trilogy - Ultimate Complete.bin
```

The three ROMs being combined are:

```
🔵  Sonic The Hedgehog         (USA, Europe)  —  512 KB   (524,288 bytes)
🔴  Sonic The Hedgehog 2       (World)        —  1.0 MB  (1,048,576 bytes)
🟡  Sonic The Hedgehog 3 & K   (World)        —  4.0 MB  (4,194,304 bytes)
                                               ──────────────────────────
                                    ROMs only  —  5.5 MB  (5,767,168 bytes)
                                    Padded to  — 64.0 MB (67,108,864 bytes)
```

---

## 📁 Required Files

Before you begin, make sure you have the following files in the same folder:

| File | Size | Required |
|------|------|----------|
| `Sonic The Hedgehog (USA, Europe).bin` | 512 KB | ✅ Yes |
| `Sonic The Hedgehog 2 (World).bin` | 1.0 MB | ✅ Yes |
| `Sonic The Hedgehog 3 & Knuckles (World).bin` | 4.0 MB | ✅ Yes |
| `combine_roms.py` | — | ✅ Yes (for Method A) |

---

## 🗺️ Final ROM Layout

The 64 MB combined ROM uses the following memory map:

```
 Address Range          Size       Content
 ─────────────────────────────────────────────────────────────────────
 0x0000000 – 0x00000FF   256 B    Genesis Interrupt Vectors
 0x0000100 – 0x00001FF   256 B    ✏️  Trilogy ROM Header (written by script)
 0x0000200 – 0x007FFFF   ~512 KB  🔵  Sonic The Hedgehog 1 (body of ROM)
 0x0080000 – 0x017FFFF   1.0 MB   🔴  Sonic The Hedgehog 2
 0x0180000 – 0x057FFFF   4.0 MB   🟡  Sonic The Hedgehog 3 & Knuckles
 0x0580000 – 0x3FFFFFF   ~58 MB   ░░  Padding bytes (0xFF)
 ─────────────────────────────────────────────────────────────────────
 TOTAL                   64 MB    67,108,864 bytes
```

---

## 🐍 Method A — Python Script (Recommended)

### Prerequisites

- Python 3.6 or higher installed
- All three ROM `.bin` files in the same directory as `combine_roms.py`

### Step-by-Step

**Step 1 — Open a terminal** in the folder containing the files.

**Step 2 — Verify your ROM files are correct:**
```bash
# Linux / macOS
ls -lh *.bin

# Expected output:
# 512K  Sonic The Hedgehog (USA, Europe).bin
# 1.0M  Sonic The Hedgehog 2 (World).bin
# 4.0M  Sonic The Hedgehog 3 & Knuckles (World).bin
```

**Step 3 — Run the combine script:**
```bash
python3 combine_roms.py
```

**Step 4 — Wait for completion.** The script will print a full log:
```
======================================================================
  🦔  SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE
       Tool : Esrael Sonic Editor II
       By   : Esrael Neto  ©  2026
======================================================================

  📂  VALIDATING SOURCE ROMs
  ─────────────────────────────────────────────────────────────────────
  ✅  Sonic The Hedgehog (USA, Europe).bin
       Size   : 524,288 bytes  (512 KB)
  ✅  Sonic The Hedgehog 2 (World).bin
       Size   : 1,048,576 bytes  (1024 KB)
  ✅  Sonic The Hedgehog 3 & Knuckles (World).bin
       Size   : 4,194,304 bytes  (4096 KB)

  📥  LOADING ROMs
  ─────────────────────────────────────────────────────────────────────
  🔵  Sonic 1      :    524,288 bytes  (512 KB)
  🔴  Sonic 2      :  1,048,576 bytes  (1024 KB)
  🟡  Sonic 3 & K  :  4,194,304 bytes  (4 MB)

  🗺️   ROM LAYOUT  (64 MB)
  ─────────────────────────────────────────────────────────────────────
  Offset 0x0000000 – 0x007FFFF  │ Sonic 1       512 KB
  Offset 0x0080000 – 0x017FFFF  │ Sonic 2      1024 KB
  Offset 0x0180000 – 0x057FFFF  │ Sonic 3 & K     4 MB
  Offset 0x0580000 – 0x3FFFFFF  │ Padding       ~58 MB

  🔧  ASSEMBLING ROM
  ─────────────────────────────────────────────────────────────────────
  ✅  Sonic 1       copied  @ 0x0000000
  ✅  Sonic 2       copied  @ 0x0080000
  ✅  Sonic 3 & K   copied  @ 0x0180000
  ✅  Padding       applied

  📝  WRITING ROM HEADER  (offset 0x100)
  ─────────────────────────────────────────────────────────────────────
  ✅  Console Name  : SEGA MEGA DRIVE
  ✅  Copyright     : (C)ESRAEL 2026.JAN
  ✅  Domestic Name : SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE
  ✅  Checksum      : 0xF1A5

  💾  WRITING OUTPUT ROM
  ─────────────────────────────────────────────────────────────────────
  ✅  Output File   : Sonic Classic Trilogy - Ultimate Complete.bin
  ✅  Final Size    : 67,108,864 bytes  (64 MB)
  ✅  MD5 Checksum  : 2f3549fe6e6953cee165a578b08a7b85

======================================================================
  🎮  COMBINATION COMPLETE!
======================================================================
```

**Step 5 — Verify the output file:**
```bash
ls -lh "Sonic Classic Trilogy - Ultimate Complete.bin"
# Expected: 64M  Sonic Classic Trilogy - Ultimate Complete.bin
```

---

## 🛠️ Method B — Esrael Sonic Editor II (GUI)

Use the **Esrael Sonic Editor II** graphical interface to combine the ROMs.

### Step 1 — Launch Esrael Sonic Editor II

Open the **Esrael Sonic Editor II** application on your computer.

### Step 2 — Open the Multi-ROM / Trilogy Panel

From the main menu, navigate to:
```
Trilogy  →  Multi-ROM Combiner
```

### Step 3 — Create a New Trilogy Project

Click:
```
New Project  →  Sonic Classic Trilogy: Ultimate Complete
```

### Step 4 — Load Each ROM in Order

Add the ROMs **in this exact order**:

```
[Slot 1]  🔵  Sonic The Hedgehog (USA, Europe).bin
[Slot 2]  🔴  Sonic The Hedgehog 2 (World).bin
[Slot 3]  🟡  Sonic The Hedgehog 3 & Knuckles (World).bin
```

> ⚠️ **Order matters!** Always load Sonic 1 first, Sonic 2 second, Sonic 3 & Knuckles third.

### Step 5 — Configure Output Settings

Set the following options in the editor:

| Setting | Value |
|---------|-------|
| **Project Name** | Sonic Classic Trilogy: Ultimate Complete |
| **Output File** | `Sonic Classic Trilogy - Ultimate Complete.bin` |
| **Output Size** | 64 MB |
| **Padding Byte** | `0xFF` |
| **Header Name** | `SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE` |
| **Region** | JUE (Japan / USA / Europe) |
| **Copyright** | `(C)ESRAEL 2026.JAN` |

### Step 6 — Build the Combined ROM

Click the **Build / Combine** button.

The editor will:
1. Validate all three source ROMs
2. Copy each ROM into the correct memory position
3. Write the combined ROM header
4. Calculate and embed the ROM checksum
5. Pad the ROM to 64 MB
6. Save the final `.bin` file

### Step 7 — Test in Emulator

Load the output file in your emulator to confirm it works correctly:
```
Sonic Classic Trilogy - Ultimate Complete.bin
```

---

## 💻 Method C — Command Line (Manual)

### Linux / macOS

```bash
# ─────────────────────────────────────────────────────────────────
# STEP 1: Concatenate all three ROMs in order
# ─────────────────────────────────────────────────────────────────
cat "Sonic The Hedgehog (USA, Europe).bin" \
    "Sonic The Hedgehog 2 (World).bin" \
    "Sonic The Hedgehog 3 & Knuckles (World).bin" \
    > "Sonic Classic Trilogy - Ultimate Complete.bin"

echo "Combined size: $(wc -c < 'Sonic Classic Trilogy - Ultimate Complete.bin') bytes"
# Output: 5767168 bytes

# ─────────────────────────────────────────────────────────────────
# STEP 2: Pad to exactly 64 MB (67,108,864 bytes)
# ─────────────────────────────────────────────────────────────────
python3 -c "
TARGET  = 64 * 1024 * 1024   # 67,108,864 bytes
ROM     = 'Sonic Classic Trilogy - Ultimate Complete.bin'
import os
current = os.path.getsize(ROM)
pad     = TARGET - current
print(f'Current size : {current:,} bytes')
print(f'Padding      : {pad:,} bytes (0xFF)')
with open(ROM, 'ab') as f:
    f.write(b'\xFF' * pad)
print(f'Final size   : {os.path.getsize(ROM):,} bytes ({os.path.getsize(ROM)//1024//1024} MB)')
print('Done!')
"

# ─────────────────────────────────────────────────────────────────
# STEP 3: Verify final size
# ─────────────────────────────────────────────────────────────────
ls -lh "Sonic Classic Trilogy - Ultimate Complete.bin"
# Expected: 64M  Sonic Classic Trilogy - Ultimate Complete.bin
```

### Windows (PowerShell)

```powershell
# STEP 1: Set file names
$sonic1  = "Sonic The Hedgehog (USA, Europe).bin"
$sonic2  = "Sonic The Hedgehog 2 (World).bin"
$sonic3k = "Sonic The Hedgehog 3 & Knuckles (World).bin"
$output  = "Sonic Classic Trilogy - Ultimate Complete.bin"
$target  = 64 * 1024 * 1024   # 67,108,864 bytes

# STEP 2: Combine ROMs
$data = [System.IO.File]::ReadAllBytes($sonic1) +
        [System.IO.File]::ReadAllBytes($sonic2) +
        [System.IO.File]::ReadAllBytes($sonic3k)

# STEP 3: Pad to 64 MB
$pad  = $target - $data.Length
$data = $data + ([byte[]](,0xFF * $pad))

# STEP 4: Write output
[System.IO.File]::WriteAllBytes($output, $data)
Write-Host "Done! Size: $((Get-Item $output).Length) bytes"
# Expected: 67108864 bytes
```

### Windows (Command Prompt)

```cmd
REM STEP 1: Combine ROMs using COPY
copy /b "Sonic The Hedgehog (USA, Europe).bin" + ^
        "Sonic The Hedgehog 2 (World).bin" + ^
        "Sonic The Hedgehog 3 & Knuckles (World).bin" ^
        "Sonic Classic Trilogy - Ultimate Complete.bin"

REM STEP 2: Pad to 64 MB using Python
python combine_roms.py
```

---

## ✅ Verification Checklist

After combining, verify the following before testing:

| Check | Expected Value | Status |
|-------|---------------|--------|
| Output file exists | `Sonic Classic Trilogy - Ultimate Complete.bin` | ☐ |
| File size | **67,108,864 bytes (64 MB)** | ☐ |
| Header at 0x100 | `SEGA MEGA DRIVE` | ☐ |
| ROM title | `SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE` | ☐ |
| Checksum at 0x18E | `0xF1A5` | ☐ |
| ROM end address | `0x03FFFFFF` | ☐ |
| Sonic 1 at offset | `0x0000000` | ☐ |
| Sonic 2 at offset | `0x0080000` | ☐ |
| Sonic 3 & K at offset | `0x0180000` | ☐ |
| Padding | `0xFF` from `0x0580000` to end | ☐ |

---

## 🎮 Testing the Combined ROM

### Recommended Emulators

1. **BlastEm** — Best accuracy, recommended for testing
   ```bash
   blastem "Sonic Classic Trilogy - Ultimate Complete.bin"
   ```

2. **Genesis Plus GX (RetroArch)**
   - Open RetroArch → Load Core → Genesis Plus GX
   - Load Content → Select the `.bin` file

3. **Gens/GS**
   - File → Open ROM → Select the `.bin` file

### What to Verify

- ✅ Game boots to a title or selection menu
- ✅ Sonic 1 loads and plays correctly
- ✅ Sonic 2 loads and plays correctly
- ✅ Sonic 3 & Knuckles loads and plays correctly
- ✅ No graphical corruption or crashes
- ✅ Audio plays correctly in all three games
- ✅ Save states work (if applicable)

---

## ❗ Troubleshooting

### ROM Won't Boot

| Problem | Solution |
|---------|----------|
| Wrong file size | Re-run `combine_roms.py` to get exactly 64 MB |
| Corrupted source ROM | Re-obtain the original source `.bin` files |
| Wrong ROM order | Must be: Sonic 1 → Sonic 2 → Sonic 3 & K |
| Bad checksum | Re-run the Python script — it recalculates automatically |

### Size is Wrong

```bash
# Check current size
wc -c "Sonic Classic Trilogy - Ultimate Complete.bin"
# Must be: 67108864

# If wrong, delete and re-run the script
rm "Sonic Classic Trilogy - Ultimate Complete.bin"
python3 combine_roms.py
```

### Python Script Errors

```
❌  MISSING  : Sonic The Hedgehog (USA, Europe).bin
```
→ Make sure all three `.bin` files are in the same folder as `combine_roms.py`.

```
⚠️   Size mismatch: expected 524288, got XXXXXX
```
→ Your source ROM is not the correct version. Use the standard dumps listed in this guide.

---

## 📊 MD5 Checksums (Source ROMs)

For reference, the MD5 checksums of the source ROMs used to build this project:

| ROM | MD5 |
|-----|-----|
| Sonic The Hedgehog (USA, Europe).bin | `1bc674be034e43c96b86487ac69d9293` |
| Sonic The Hedgehog 2 (World).bin | `8e2c29a1e65111fe2078359e685e7943` |
| Sonic The Hedgehog 3 & Knuckles (World).bin | `c5b1c655c19f462ade0ac4e17a844d10` |
| **Sonic Classic Trilogy - Ultimate Complete.bin** | `2f3549fe6e6953cee165a578b08a7b85` |

---

## 📝 Notes

- The combined ROM uses **standard Sega Mega Drive / Genesis ROM format** — no special emulator support is required.
- The **64 MB size** is the maximum supported by most Genesis flash cartridges (EverDrive, MegaSD).
- The ROM header is written at offset `0x100` as per the official Sega Mega Drive hardware specification.
- The checksum is calculated from offset `0x200` onward, summing all 16-bit big-endian words, as per the Genesis standard.
- Padding with `0xFF` (all ones) is the standard for unused Genesis ROM space.

---

> *Sonic Classic Trilogy: Ultimate Complete is a fan-made ROM hack created for preservation and entertainment purposes.*
> *All original Sonic the Hedgehog games are owned by SEGA.*

---

**© 2026 Esrael Neto — Sonic Classic Trilogy: Ultimate Complete**
**Tool: Esrael Sonic Editor II**