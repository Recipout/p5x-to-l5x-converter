# P5X to L5X Converter

## Project Purpose
This project converts Rockwell Automation `P5X` archives into extractable `L5X` files for use with PLC Copilot and related Logix Designer workflows.

The files in this repository are intended to support early validation and extraction testing before broader deployment or automation.

## Current Status
Status: Ready for local Windows validation

Completed items:
- P5X test archives were placed into the repository
- A Python extraction script was created
- Usage guidance and validation steps were documented
- Repository structure is ready for local testing and future expansion

## Included Files
- `PB_Start_Stop_2.zip`
- `PB_test.zip`
- `p5x_to_l5x.py`
- `QUICK_START.txt`
- `TESTING_LOG.txt`
- `SESSION_SUMMARY_2026-10-07.md`

## How the Script Works
The script scans a folder for `.p5x` files, opens each one as a ZIP archive, extracts embedded `.l5x` files, and writes them to an output folder.

Important note:
- This is an extraction workflow, not a file conversion rewrite.
- The script preserves the exported `.l5x` files as-is.

## Required Local Setup
On a Windows machine:

1. Create a Desktop folder named `p5x_test`
2. Create a Desktop folder named `l5x_output`
3. Copy the `.p5x` files into `Desktop/p5x_test`
4. Save `p5x_to_l5x.py` to the Desktop
5. Open Command Prompt and run:

```cmd
python "%USERPROFILE%\Desktop\p5x_to_l5x.py"
```

Expected result:
- Extracted `.l5x` files appear in `Desktop/l5x_output`
- Each archive creates its own output folder if needed

## Expected Output Structure

```text
Desktop/
├── p5x_test/
│   ├── PB_Start_Stop_2.zip
│   └── PB_test.zip
├── l5x_output/
│   ├── PB_Start_Stop_2/
│   │   └── Project.l5x
│   └── PB_test/
│       └── Project.l5x
└── p5x_to_l5x.py
```

## Validation Goals
The current validation test is designed to confirm:
- the `.p5x` archives are valid ZIP files
- the script finds `.l5x` content within the archive
- the output files are extracted correctly
- the extracted content can be imported into PLC Copilot

## Recommended Next Steps
- Run the script locally with the repository test files
- Import the extracted `.l5x` files into PLC Copilot
- Verify ladder logic loads correctly
- Validate rung display and simulation behavior
- Update `TESTING_LOG.txt` with final results

## Summary
This repository is positioned as a small, focused extraction utility for RSLogix 5000-generated P5X files. It provides a simple, low-friction workflow to make `.l5x` content available for PLC Copilot and related engineering review tools.
