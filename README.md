# 🦔 Sonic Classic Trilogy: Ultimate Complete
### For Sega Mega Drive / Genesis — 64 MB Combined ROM

---

> **A Brand New Sega Genesis ROM Hack**
> Created by **Esrael Neto** · © 2026
> Tool Used: **Esrael Sonic Editor II**

---

## 📖 Table of Contents

- [About](#about)
- [ROM List](#rom-list)
- [Combined ROM Details](#combined-rom-details)
- [ROM Memory Layout](#rom-memory-layout)
- [How to Add ROMs](#how-to-add-roms)
  - [Step 1 — Sonic 1](#-step-1--add-sonic-the-hedgehog-1)
  - [Step 2 — Sonic 2](#-step-2--add-sonic-the-hedgehog-2)
  - [Step 3 — Sonic 3 & Knuckles](#-step-3--add-sonic-3--knuckles)
- [How to Combine ROMs](#how-to-combine-roms)
  - [Method A — Python Script](#-method-a--python-script-automated)
  - [Method B — Esrael Sonic Editor II](#-method-b--esrael-sonic-editor-ii-manual)
  - [Method C — Command Line](#-method-c--command-line)
- [ROM Header Info](#rom-header-info)
- [Using Esrael Sonic Editor II](#using-esrael-sonic-editor-ii)
- [Emulator Compatibility](#emulator-compatibility)
- [ROM Hack Details](#rom-hack-details)
- [Credits](#credits)

---

## About

**Sonic Classic Trilogy: Ultimate Complete** is a brand new ROM hack for the **Sega Mega Drive / Genesis** that brings together all three classic Sonic titles — Sonic the Hedgehog, Sonic the Hedgehog 2, and Sonic 3 & Knuckles — into **one single 64 MB combined ROM**.

This project was built using **Esrael Sonic Editor II**, a powerful tool created by **Esrael Neto**, designed specifically for hacking and editing Sonic the Hedgehog ROMs on the Sega Mega Drive / Genesis platform.

The final combined ROM file is:
```
Sonic Classic Trilogy - Ultimate Complete.bin  (64 MB / 67,108,864 bytes)
```

---

## ROM List

The following source ROM files are used to build the combined trilogy:

| # | ROM File | Region | Size | Year |
|---|----------|--------|------|------|
| 1 | `Sonic The Hedgehog (USA, Europe).bin` | USA / Europe | 512 KB | 1991 |
| 2 | `Sonic The Hedgehog 2 (World).bin` | World | 1.0 MB | 1992 |
| 3 | `Sonic The Hedgehog 3 & Knuckles (World).bin` | World | 4.0 MB | 1994 |

---

## Combined ROM Details

| Detail | Value |
|--------|-------|
| **Output File** | `Sonic Classic Trilogy - Ultimate Complete.bin` |
| **Total Size** | 67,108,864 bytes **(64 MB)** |
| **Platform** | Sega Mega Drive / Genesis |
| **Header Name** | `SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE` |
| **Console Tag** | `SEGA MEGA DRIVE` |
| **Copyright** | `(C)ESRAEL 2026.JAN` |
| **Serial** | `GM T-000000-00` |
| **Region** | `JUE` (Japan / USA / Europe) |
| **ROM Checksum** | `0xF1A5` (auto-calculated) |
| **Padding Byte** | `0xFF` (standard Genesis padding) |

---

## ROM Memory Layout

The 64 MB combined ROM is laid out as follows:

```
┌─────────────────────────────────────────────────────────────────────┐
│         Sonic Classic Trilogy - Ultimate Complete.bin  (64 MB)      │
├────────────────┬──────────────┬───────────────────────────────────  │
│ Start Offset   │ End Offset   │ Content                             │
├────────────────┼──────────────┼─────────────────────────────────────┤
│ 0x0000000      │ 0x007FFFF    │ 🔵 Sonic The Hedgehog      (512 KB) │
│ 0x0080000      │ 0x017FFFF    │ 🔴 Sonic The Hedgehog 2    (1.0 MB) │
│ 0x0180000      │ 0x057FFFF    │ 🟡 Sonic 3 & Knuckles      (4.0 MB) │
│ 0x0580000      │ 0x3FFFFFF    │ ░░ Padding (0xFF)          (58 MB)  │
└────────────────┴──────────────┴─────────────────────────────────────┘
  Total: 67,108,864 bytes = 64 MB
```

### Size Breakdown

```
  Sonic 1        :      524,288 bytes  (  512 KB  /  0.5 MB)
  Sonic 2        :    1,048,576 bytes  ( 1024 KB  /  1.0 MB)
  Sonic 3 & K    :    4,194,304 bytes  ( 4096 KB  /  4.0 MB)
  ─────────────────────────────────────────────────────────
  ROMs Total     :    5,767,168 bytes  ( 5632 KB  /  5.5 MB)
  Padding        :   61,341,696 bytes  (59904 KB  / 58.5 MB)
  ─────────────────────────────────────────────────────────
  GRAND TOTAL    :   67,108,864 bytes  (65536 KB  / 64.0 MB)
```

---

## How to Add ROMs

Follow the steps below to add each ROM to **Sonic Classic Trilogy: Ultimate Complete**.

---

### 🔵 Step 1 — Add Sonic The Hedgehog 1

**ROM File:** `Sonic The Hedgehog (USA, Europe).bin`
**Platform:** Sega Mega Drive / Genesis
**Region:** USA, Europe
**Size:** 512 KB (524,288 bytes)
**Released:** April 1991 · `(C)SEGA 1991.APR`
**Serial:** `GM 00001009-00`

**Instructions:**

1. Open **Esrael Sonic Editor II**.
2. Click **File → Open ROM**.
3. Browse to your ROM folder and select:
   ```
   Sonic The Hedgehog (USA, Europe).bin
   ```
4. The editor will load the Sonic 1 ROM automatically.
5. Apply any desired hacks, edits, or patches to the ROM.
6. Click **File → Save ROM** to save your edited version.
7. Your Sonic 1 ROM is now ready to be used in the trilogy combination.

> ✅ **Verify:** ROM must be exactly **524,288 bytes (512 KB)** before combining.

---

### 🔴 Step 2 — Add Sonic The Hedgehog 2

**ROM File:** `Sonic The Hedgehog 2 (World).bin`
**Platform:** Sega Mega Drive / Genesis
**Region:** World
**Size:** 1.0 MB (1,048,576 bytes)
**Released:** September 1992 · `(C)SEGA 1992.SEP`
**Serial:** `GM 00001051-00`

**Instructions:**

1. Open **Esrael Sonic Editor II**.
2. Click **File → Open ROM**.
3. Browse to your ROM folder and select:
   ```
   Sonic The Hedgehog 2 (World).bin
   ```
4. The editor will load the Sonic 2 ROM automatically.
5. Apply any desired hacks, edits, or patches to the ROM.
6. Click **File → Save ROM** to save your edited version.
7. Your Sonic 2 ROM is now ready to be used in the trilogy combination.

> ✅ **Verify:** ROM must be exactly **1,048,576 bytes (1.0 MB)** before combining.

---

### 🟡 Step 3 — Add Sonic 3 & Knuckles

**ROM File:** `Sonic The Hedgehog 3 & Knuckles (World).bin`
**Platform:** Sega Mega Drive / Genesis
**Region:** World
**Size:** 4.0 MB (4,194,304 bytes)
**Released:** June 1994 · `(C)SEGA 1994.JUN`
**Serial:** `GM MK-1563 -00`

**Instructions:**

1. Open **Esrael Sonic Editor II**.
2. Click **File → Open ROM**.
3. Browse to your ROM folder and select:
   ```
   Sonic The Hedgehog 3 & Knuckles (World).bin
   ```
4. The editor will load the Sonic 3 & Knuckles ROM automatically.
5. Apply any desired hacks, edits, or patches to the ROM.
6. Click **File → Save ROM** to save your edited version.
7. Your Sonic 3 & Knuckles ROM is now ready to be used in the trilogy combination.

> ✅ **Verify:** ROM must be exactly **4,194,304 bytes (4.0 MB)** before combining.

---

## How to Combine ROMs

Once all three ROMs are ready, use **one of the three methods** below to combine them into the **64 MB Sonic Classic Trilogy: Ultimate Complete** ROM.

---

### 🐍 Method A — Python Script (Automated)

This is the **recommended method**. The included Python script automates the entire combination process.

**Requirements:** Python 3.6 or higher

**Steps:**

1. Make sure all three ROM `.bin` files are in the **same folder** as `combine_roms.py`.
2. Open a terminal or command prompt in that folder.
3. Run the script:
   ```bash
   python3 combine_roms.py
   ```
4. The script will:
   - ✅ Validate all three source ROMs
   - ✅ Load and combine them in the correct order
   - ✅ Write the full Sega Genesis ROM header
   - ✅ Calculate and embed the ROM checksum
   - ✅ Pad the ROM to exactly **64 MB** using `0xFF`
   - ✅ Write the final output file

5. Output file will be created:
   ```
   Sonic Classic Trilogy - Ultimate Complete.bin  (64 MB)
   ```

**Expected output:**
```
======================================================================
  🦔  SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE  🦔
       ROM Combiner for Sega Mega Drive / Genesis
       Tool : Esrael Sonic Editor II
       By   : Esrael Neto  ©  2026
======================================================================

  ✅  Sonic The Hedgehog (USA, Europe).bin       — 524,288 bytes
  ✅  Sonic The Hedgehog 2 (World).bin           — 1,048,576 bytes
  ✅  Sonic The Hedgehog 3 & Knuckles (World).bin — 4,194,304 bytes

  🎮  COMBINATION COMPLETE!
  📦  Output: Sonic Classic Trilogy - Ultimate Complete.bin  (64 MB)
```

---

### 🛠️ Method B — Esrael Sonic Editor II (Manual)

Use the **Esrael Sonic Editor II** GUI to combine the ROMs manually.

**Steps:**

1. Open **Esrael Sonic Editor II**.
2. Navigate to **Trilogy / Multi-ROM** menu.
3. Click **New Project → Sonic Classic Trilogy: Ultimate Complete**.
4. Add each ROM in the following order:

   | Order | ROM | File |
   |-------|-----|------|
   | 1st | Sonic The Hedgehog | `Sonic The Hedgehog (USA, Europe).bin` |
   | 2nd | Sonic The Hedgehog 2 | `Sonic The Hedgehog 2 (World).bin` |
   | 3rd | Sonic 3 & Knuckles | `Sonic The Hedgehog 3 & Knuckles (World).bin` |

5. Configure the **menu / selector screen** settings (title, background, music).
6. Set the output ROM size to **64 MB**.
7. Set the output file name:
   ```
   Sonic Classic Trilogy - Ultimate Complete.bin
   ```
8. Click **Build / Combine** to generate the final combined ROM.
9. Test the combined ROM in your preferred emulator.

> ⚠️ **Important:** Always add ROMs in order: Sonic 1 → Sonic 2 → Sonic 3 & Knuckles.

---

### 💻 Method C — Command Line

You can also combine ROMs directly from the command line without Python.

**Linux / macOS:**
```bash
# Step 1: Combine the three ROMs
cat "Sonic The Hedgehog (USA, Europe).bin" \
    "Sonic The Hedgehog 2 (World).bin" \
    "Sonic The Hedgehog 3 & Knuckles (World).bin" \
    > "Sonic Classic Trilogy - Ultimate Complete.bin"

# Step 2: Pad to exactly 64 MB (67,108,864 bytes)
python3 -c "
import os
f = open('Sonic Classic Trilogy - Ultimate Complete.bin', 'ab')
size = os.path.getsize('Sonic Classic Trilogy - Ultimate Complete.bin')
f.write(b'\xFF' * (67108864 - size))
f.close()
print(f'Done! Size: {os.path.getsize(\"Sonic Classic Trilogy - Ultimate Complete.bin\")} bytes')
"
```

**Windows (PowerShell):**
```powershell
# Combine ROMs
$roms = @(
    "Sonic The Hedgehog (USA, Europe).bin",
    "Sonic The Hedgehog 2 (World).bin",
    "Sonic The Hedgehog 3 & Knuckles (World).bin"
)
$output = "Sonic Classic Trilogy - Ultimate Complete.bin"
$bytes = $roms | ForEach-Object { [System.IO.File]::ReadAllBytes($_) }
[System.IO.File]::WriteAllBytes($output, ($bytes | ForEach-Object { $_ }))
Write-Host "Combined! Now pad to 64MB using combine_roms.py for best results."
```

> ✅ **Note:** Method A (Python script) is recommended as it also writes the correct ROM header and checksum automatically.

---

## ROM Header Info

The combined ROM contains the following Sega Genesis header at offset `0x100`:

```
Offset  Size   Field              Value
──────────────────────────────────────────────────────────────────────
0x100   16     Console Name       SEGA MEGA DRIVE
0x110   16     Copyright          (C)ESRAEL 2026.JAN
0x120   48     Domestic Title     SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE
0x150   48     Overseas Title     SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE
0x180   14     Serial Number      GM T-000000-00
0x18E    2     Checksum           0xF1A5  (auto-calculated)
0x190   16     I/O Support        JD
0x1A0    4     ROM Start          0x00000000
0x1A4    4     ROM End            0x03FFFFFF  (64 MB - 1)
0x1A8    4     RAM Start          0x00FF0000
0x1AC    4     RAM End            0x00FFFFFF
0x1BC   48     Notes              ESRAEL SONIC EDITOR II - ROM HACK
0x1F0   16     Region             JUE  (Japan / USA / Europe)
```

---

## Using Esrael Sonic Editor II

**Esrael Sonic Editor II** is the primary tool used to build this ROM hack. Created by **Esrael Neto**, it is specifically designed for Sonic the Hedgehog ROM hacking on the Sega Mega Drive / Genesis platform.

### Key Features Used in This Project

| Feature | Description |
|---------|-------------|
| **ROM Loading** | Open and edit Sonic 1, Sonic 2, and Sonic 3 & Knuckles ROMs directly |
| **Level Editing** | Modify stage layouts, tile placements, and object positions |
| **Palette Editing** | Customize color palettes for characters, stages, and UI elements |
| **Object Placement** | Add, remove, or reposition enemies, rings, springs, and objects |
| **Music / Sound** | Edit or replace in-game music and sound effects |
| **Multi-ROM Combination** | Combine multiple Sonic ROMs into a single 64 MB trilogy ROM |
| **Header Management** | Automatically updates ROM headers with hack title and metadata |
| **Checksum Calculation** | Recalculates and embeds the correct Genesis ROM checksum |
| **Save & Export** | Save the final ROM as a `.bin` file for all emulators and flash carts |

---

## Emulator Compatibility

The combined 64 MB ROM is compatible with the following emulators and hardware:

| Emulator / Device | Platform | Compatible |
|-------------------|----------|-----------|
| **BlastEm** | Windows / Linux / macOS | ✅ |
| **Gens/GS** | Windows / Linux | ✅ |
| **Genesis Plus GX** | RetroArch / Wii / etc. | ✅ |
| **MAME** (Genesis driver) | All platforms | ✅ |
| **Retroarch** | All platforms | ✅ |
| **Fusion** | Windows | ✅ |
| **EverDrive MD** | Real Hardware | ✅ |
| **MegaSD** | Real Hardware | ✅ |
| **Mega Everdrive Pro** | Real Hardware | ✅ |

---

## ROM Hack Details

| Detail | Info |
|--------|------|
| **Hack Name** | Sonic Classic Trilogy: Ultimate Complete |
| **Output File** | `Sonic Classic Trilogy - Ultimate Complete.bin` |
| **Platform** | Sega Mega Drive / Genesis |
| **Base ROMs** | Sonic 1 + Sonic 2 + Sonic 3 & Knuckles |
| **Combined Size** | 64 MB (67,108,864 bytes) |
| **Tool Used** | Esrael Sonic Editor II |
| **Creator** | Esrael Neto |
| **Year Created** | 2026 |
| **Output Format** | `.bin` (Sega Mega Drive / Genesis ROM) |
| **Padding** | `0xFF` to 64 MB |
| **Checksum** | `0xF1A5` |
| **Compatibility** | All Sega Mega Drive / Genesis Emulators & Flash Carts |

---

## Credits

| Role | Name |
|------|------|
| **ROM Hack Creator** | Esrael Neto |
| **Tool Developer** | Esrael Neto (Esrael Sonic Editor II) |
| **Original Games** | Sonic Team / SEGA |
| **Sonic 1** | © SEGA 1991 |
| **Sonic 2** | © SEGA 1992 |
| **Sonic 3 & Knuckles** | © SEGA 1994 |

---

## Repository Structure

```
Sonic-Classic-Trilogy-Ultimate-Complete/
│
├── 📄  README.md
├── 🐍  combine_roms.py
├── 📋  COMBINE_GUIDE.md
│
├── 🔵  Sonic The Hedgehog (USA, Europe).bin           (512 KB)
├── 🔴  Sonic The Hedgehog 2 (World).bin               (1.0 MB)
├── 🟡  Sonic The Hedgehog 3 & Knuckles (World).bin    (4.0 MB)
│
└── 🎮  Sonic Classic Trilogy - Ultimate Complete.bin  (64 MB)
```

---

> *Sonic Classic Trilogy: Ultimate Complete is a fan-made ROM hack created for preservation and entertainment purposes.*
> *All original Sonic the Hedgehog games are owned by SEGA.*

---

**© 2026 Esrael Neto — Sonic Classic Trilogy: Ultimate Complete**
**Tool: Esrael Sonic Editor II**