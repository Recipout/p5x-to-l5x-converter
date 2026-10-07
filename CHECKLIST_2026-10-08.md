# Tomorrow's Checklist
## P5X to L5X Validation

### Setup
- [ ] Confirm Python 3.6+ is installed
- [ ] Create `Desktop/p5x_test/`
- [ ] Create `Desktop/l5x_output/`
- [ ] Copy `PB_Start_Stop_2.zip` into `Desktop/p5x_test/`
- [ ] Copy `PB_test.zip` into `Desktop/p5x_test/`
- [ ] Copy `p5x_to_l5x.py` to Desktop

### Run Extraction
- [ ] Open Command Prompt
- [ ] Run:
  ```cmd
  python "%USERPROFILE%\Desktop\p5x_to_l5x.py"
  ```
- [ ] Confirm script prints `Found 2 P5X file(s)`
- [ ] Confirm script prints `EXTRACTION COMPLETE`

### Verify Output
- [ ] Check `Desktop/l5x_output/`
- [ ] Confirm `.l5x` files were created
- [ ] Confirm file count matches expected output
- [ ] Confirm the files are not empty

### PLC Copilot Import
- [ ] Open PLC Copilot
- [ ] Import one extracted `.l5x` file
- [ ] Confirm ladder logic displays
- [ ] Confirm rungs appear correctly
- [ ] Note any import errors

### Document Results
- [ ] Update `TESTING_LOG.txt`
- [ ] Record command used
- [ ] Record output location
- [ ] Record pass/fail status
- [ ] Note any issues or fixes

### Exit Criteria
- [ ] At least one L5X file extracted successfully
- [ ] At least one file imported successfully into PLC Copilot
- [ ] Results documented in repository
