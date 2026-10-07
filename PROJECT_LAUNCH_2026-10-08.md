# Project Launch Document
## P5X to L5X Converter

### Document Status
- Status: Ready for next-phase execution
- Date: 2026-10-07
- Owner: Recipout
- Repository: Recipout/p5x-to-l5x-converter

---

## 1. Objective
Establish a simple, reliable workflow for extracting `.l5x` files from `.p5x` archives produced by RSLogix 5000, so the extracted logic can be imported into PLC Copilot for review, validation, and engineering analysis.

---

## 2. Mission
Create a minimum viable workflow that can:
- accept exported P5X archives
- locate embedded L5X files
- extract them to a predictable output folder
- make the files usable in PLC Copilot
- support future automation and batch processing

---

## 3. Scope
### In Scope
- P5X archive handling
- L5X extraction from ZIP-based exports
- Local Windows validation workflow
- Repository-based sample file management
- Documentation and testing structure

### Out of Scope
- Full RSLogix 5000 project editing
- PLC logic simulation development
- Commercial product packaging
- Broad enterprise deployment

---

## 4. Deliverables
The following are in place or planned:

### Completed
- P5X sample files uploaded to repository
- Python extraction script created
- Quick-start instructions documented
- Test log template created
- Project brief created

### Next Phase Deliverables
- Local extraction validation on Windows
- Successful generation of `.l5x` output files
- PLC Copilot import testing
- Validation documentation of workflow results

---

## 5. Repository Contents
Current repository assets include:
- `PB_Start_Stop_2.zip`
- `PB_test.zip`
- `p5x_to_l5x.py`
- `QUICK_START.txt`
- `TESTING_LOG.txt`
- `PROJECT_BRIEF.md`
- `SESSION_SUMMARY_2026-10-07.md`

---

## 6. Workflow
### Local Execution Workflow
1. Place `.p5x` files in `Desktop/p5x_test/`
2. Ensure `Desktop/l5x_output/` exists
3. Place `p5x_to_l5x.py` on the Desktop
4. Run:

```cmd
python "%USERPROFILE%\Desktop\p5x_to_l5x.py"
```

5. Review extracted `.l5x` files in `Desktop/l5x_output/`
6. Import them into PLC Copilot
7. Confirm logic is visible and usable

---

## 7. Expected Output
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

---

## 8. Success Criteria
Tomorrow’s work is successful if:
- the script runs without errors
- `.l5x` files are extracted from the sample archives
- output files are created in the expected folder structure
- PLC Copilot can open/import at least one extracted file
- test results are documented in `TESTING_LOG.txt`

---

## 9. Risks and Constraints
### Risks
- Some `.p5x` files may not contain a valid `.l5x` payload
- Archive structure may vary by project export
- Corrupted or incomplete ZIP files may fail extraction
- PLC Copilot import may require project-specific compatibility checks

### Constraints
- Work is limited to the repository sample files and local testing environment
- No assumptions should be made about all RSLogix 5000 exports being structurally identical
- Extraction must remain non-destructive

---

## 10. Tomorrow’s Work Plan
### Task 1: Local Script Validation
- Confirm Python is available on the Windows system
- Set up the required folder structure
- Run the script against the repository sample P5X files
- Confirm output files are generated

### Task 2: Extraction Verification
- Check for the presence of `.l5x` files in `l5x_output`
- Confirm file names and count match the archive set
- Review for invalid or empty outputs

### Task 3: PLC Copilot Import Test
- Open PLC Copilot
- Import the extracted `.l5x` files
- Confirm ladder logic can load and render
- Identify any import issues, if present

### Task 4: Documentation Update
- Update `TESTING_LOG.txt` with actual results
- Document errors, if any
- Capture resolution steps and recommendations

---

## 11. Owners and Responsibilities
### Primary Owner
- Recipout

### Responsibilities
- maintain repository structure
- validate local execution on Windows
- verify output quality and import success
- document and resolve issues encountered during testing

---

## 12. Definition of Done
The next-phase project milestone is complete when:
- at least one P5X archive is successfully extracted into `.l5x`
- extracted files are accessible in the local output folder
- PLC Copilot can import and display the result
- testing results are captured in the repository

---

## 13. Closing Summary
This project has moved from setup into execution. The repository contains the sample input files, the extraction script, and the project documentation needed to run the first validation cycle. Tomorrow’s work will confirm that the process works end-to-end and produce the evidence needed for broader use.
