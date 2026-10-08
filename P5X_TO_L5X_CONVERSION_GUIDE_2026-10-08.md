# P5X to L5X Conversion Guide

Date: 2026-10-08

Repository: Recipout/p5x-to-l5x-converter

## Objective
This file captures the confirmed working method for converting exported `.p5x` archives into `.l5x` files so they can be imported into PLC Copilot.

## Verified Working Command
```cmd
python r"%USERPROFILE%\Desktop\p5x_to_l5x.py"
```

## What This Script Does
The script opens each `.p5x` file as a ZIP archive, finds embedded `.l5x` files, and extracts them to a predictable output folder.

This is an extraction workflow, not a file conversion that rewrites logic. The `.l5x` files remain valid PLC Logix files.

## Required Folder Layout
Create these folders on your Desktop:

```text
Desktop/
├── p5x_test/
├── l5x_output/
└── p5x_to_l5x.py
```

## Step-by-Step Instructions
### 1. Install Python
Make sure Python 3.6 or newer is installed.

Check with:
```cmd
python --version
```

If Python is missing, install it from:
https://www.python.org/downloads/

Make sure the option "Add Python to PATH" is selected during installation.

### 2. Create the required folders
On your Windows Desktop, create:
- `Desktop\p5x_test\`
- `Desktop\l5x_output\`

### 3. Save the conversion script
Place the file `p5x_to_l5x.py` in:
```text
Desktop\p5x_to_l5x.py
```

### 4. Add your P5X files
Copy each `.p5x` file into:
```text
Desktop\p5x_test\
```

### 5. Run the extraction
Open Command Prompt and run:
```cmd
python r"%USERPROFILE%\Desktop\p5x_to_l5x.py"
```

### 6. Confirm success
The script should print output similar to:
```text
Found N P5X file(s)
EXTRACTION COMPLETE
```

Then check:
```text
Desktop\l5x_output\
```

The extracted `.l5x` files should appear there.

## Expected Result
Example structure:
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
├── p5x_to_l5x.py
└── notes.txt
```

## Import into PLC Copilot
1. Open PLC Copilot.
2. Import one extracted `.l5x` file from `Desktop\l5x_output\`.
3. Confirm the ladder logic loads and rungs display correctly.
4. Document any import errors or missing data.

## Troubleshooting
### “python is not recognized”
- Install Python
- Make sure it was added to PATH
- Restart the terminal or machine

### “Folder not found”
- Ensure `Desktop\p5x_test\` exists
- Ensure spelling is correct

### “No .p5x files found”
- Put valid `.p5x` files into `Desktop\p5x_test\`
- Do not place `.p5x.zip` files there unless they are actually `.p5x`

### “No L5X found inside”
- The archive may be corrupt or not contain an L5X payload
- Test the archive with 7-Zip or WinRAR

### “BadZipFile”
- The `.p5x` archive is corrupted or incomplete
- Re-export or re-obtain the file

## Summary
The confirmed working conversion method is:
```cmd
python r"%USERPROFILE%\Desktop\p5x_to_l5x.py"
```

This will scan `Desktop\p5x_test\`, extract any embedded `.l5x` files, and place them in `Desktop\l5x_output\` for PLC Copilot import.

## Final Note
This file is saved in the repository so it can be downloaded and reused as a reference for future conversion runs.
