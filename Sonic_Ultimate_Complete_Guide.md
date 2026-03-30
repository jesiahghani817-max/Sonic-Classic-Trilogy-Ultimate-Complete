# Sonic Classic Trilogy - Ultimate Complete: ROM Combination Guide

This guide provides the technical steps and methodology for creating the **Sonic Classic Trilogy - Ultimate Complete** ROM hack for the Sega Mega Drive/Genesis. This project aims to combine the core trilogy—**Sonic the Hedgehog 1**, **Sonic the Hedgehog 2**, and **Sonic the Hedgehog 3 & Knuckles**—into a single, cohesive 5.5MB (44 Megabit) binary file.

Created by **Esrael Neto © 2026**, this project leverages the advanced capabilities of **Esrael Sonic Editor II** and the foundational architecture of the **Sonic Delta** series.

---

## Project Overview

The goal is to merge three legendary titles into one "Ultimate" ROM. Unlike simple multi-carts, this hack integrates the games using a unified engine, typically based on the **Sonic 3 & Knuckles** codebase due to its advanced object handling and memory management.

### Specifications
| Feature | Detail |
| :--- | :--- |
| **Project Name** | Sonic Classic Trilogy - Ultimate Complete |
| **File Name** | `Sonic Classic Trilogy - Ultimate Complete.bin` |
| **Target Size** | 5.5 MB (approx. 44 Megabits) |
| **Platform** | Sega Mega Drive / Genesis |
| **Primary Tool** | Esrael Sonic Editor II |
| **Base Engine** | Sonic 3 & Knuckles (Modified) |

---

## Technical Requirements

To begin the combination process, you must have the following assets ready in your workspace:

1.  **Esrael Sonic Editor II**: The primary suite for level, art, and palette editing across all three titles.
2.  **Original ROMs**:
    *   `Sonic the Hedgehog (USA, Europe).bin` (v1.0 or v1.1)
    *   `Sonic the Hedgehog 2 (World).bin`
    *   `Sonic the Hedgehog 3 & Knuckles (World).bin`
3.  **Sonic Delta Framework**: A pre-modified disassembly or base ROM that supports extended ROM sizes beyond the standard 4MB limit.

---

## Step-by-Step Combination Process

### 1. Preparing the 5.5MB Workspace
Standard Genesis cartridges are limited to 4MB. To achieve 5.5MB, you must use a custom mapper (similar to the SEGA mapper used in *Super Street Fighter II*).
*   Open **Esrael Sonic Editor II**.
*   Initialize a new project using the **Sonic 3 & Knuckles** disassembly as the base.
*   Configure the ROM header to reflect the 5.5MB size and enable SRAM for cross-game progress saving.

### 2. Porting Assets with Esrael Sonic Editor II
The editor allows for seamless asset transfer between the supported titles.
*   **Level Layouts**: Import the level data from Sonic 1 and Sonic 2 into the S3&K engine. Use the "Level Editor" module to adjust object IDs, as they differ between games.
*   **Art and Palettes**: Use the "Art Editor" and "Palette Editor" to import the iconic tilesets and color schemes. Ensure that the VRAM allocation does not conflict with the S3&K HUD and character sprites.
*   **Music and Sound**: The Z80 driver must be updated to include the DAC samples and FM tracks from all three games.

### 3. Implementing the Unified Menu
A custom "Game Selection" menu is required to navigate between the trilogies.
*   Modify the S3&K Title Screen code to include a selection interface.
*   Implement "Level Select" hooks that jump to the starting zone of each respective game (Green Hill, Emerald Hill, or Angel Island).

### 4. Memory Mapping and Bank Switching
Since the ROM exceeds 4MB, you must manage data banking:
*   Store Sonic 1 and Sonic 2 data in the extended memory regions (above $400000).
*   Use bank-switching routines to swap the necessary level data into the active memory window during gameplay.

---

## Key Improvements in the Ultimate Edition
*   **Integrated Physics**: All three games share the refined S3&K physics, including the Insta-Shield and elemental shields.
*   **Character Consistency**: Play as Sonic, Tails, or Knuckles across all zones from the first game to the last.
*   **Save System**: A unified SRAM system that tracks emeralds and progress across the entire trilogy.

---

## Troubleshooting and Hardware Compatibility
*   **Everdrive Users**: To run a 5.5MB ROM on original hardware, ensure your Everdrive OS supports the SEGA mapper. Some versions may require a modified `MEGAOS.BIN`.
*   **Checksum Errors**: Always use the "Fix Checksum" tool within Esrael Sonic Editor II before testing the ROM in an emulator.

---

> "The Ultimate Complete edition is the culmination of decades of Sonic ROM hacking, bringing the entire 16-bit legacy into a single, seamless experience." — **Esrael Neto**
