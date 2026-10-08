# Workflow Guide: Working Between Local and Repository

Date: 2026-10-08

Repository: Recipout/p5x-to-l5x-converter

## Overview
This guide explains how to move between your local machine and the GitHub repository so you can work on your P5X-to-L5X converter project and keep your work synchronized.

---

## Option 1: Work Locally, Push to GitHub (Recommended for Active Development)

### Initial Setup (One-time)
1. **Clone the repository to your computer:**
   ```cmd
   git clone https://github.com/Recipout/p5x-to-l5x-converter.git
   ```
   This creates a local folder with all repository files.

2. **Navigate to the folder:**
   ```cmd
   cd p5x-to-l5x-converter
   ```

### Regular Workflow
1. **Pull latest changes from GitHub:**
   ```cmd
   git pull
   ```

2. **Work on files locally:**
   - Edit scripts, documentation, test files
   - Run your conversion script
   - Gather results and notes

3. **Stage your changes:**
   ```cmd
   git add .
   ```
   (The period adds all changed files)

4. **Commit with a message:**
   ```cmd
   git commit -m "Your descriptive message here"
   ```
   Example:
   ```cmd
   git commit -m "tested conversion on PB_Start_Stop_2.zip - extracted successfully"
   ```

5. **Push to GitHub:**
   ```cmd
   git push
   ```
   Your changes now appear in the repository.

---

## Option 2: Work Directly on GitHub (Quickest for Small Changes)

### Steps
1. **Open your repository in a web browser:**
   https://github.com/Recipout/p5x-to-l5x-converter

2. **Find the file you want to edit:**
   - Click on the file name
   - Click the pencil icon (✏️) to edit

3. **Make your changes:**
   - Edit the content directly

4. **Commit the changes:**
   - Scroll to the bottom
   - Add a commit message
   - Click "Commit changes"

5. **Changes are live immediately** in the repository

### Use This For:
- Quick updates to documentation
- Adding notes or results
- Creating new files
- Small fixes

---

## Option 3: Use GitHub Desktop (GUI for Git)

### Setup
1. **Download GitHub Desktop:**
   https://desktop.github.com/

2. **Install and sign in** with your GitHub account

3. **Clone your repository:**
   - File → Clone Repository
   - Select: Recipout/p5x-to-l5x-converter
   - Choose a local folder location

### Workflow
1. **Open the repository** in GitHub Desktop

2. **Work on files locally** using any editor (VS Code, Notepad++, etc.)

3. **GitHub Desktop automatically detects changes:**
   - Look at the "Changes" tab
   - Files you modified appear listed

4. **Commit:**
   - Write a commit message at the bottom left
   - Click "Commit to main"

5. **Push to GitHub:**
   - Click the "Push origin" button
   - Changes sync to the repository

### Use This For:
- If you prefer graphical interfaces over command line
- Visual confirmation of what changed
- Learning Git without terminal commands

---

## Recommended Workflow for Your P5X Project

### Before Starting Work
```cmd
cd C:\Users\YourName\p5x-to-l5x-converter
git pull
```

### During Work
- Test your conversion script locally
- Gather results
- Create or update documentation files
- Keep notes in markdown files (.md)

### After Testing/Creating
```cmd
git add .
git commit -m "descriptive message about what you did"
git push
```

### Example Commit Messages
```cmd
git commit -m "Successfully extracted L5X from PB_Start_Stop_2.zip"
git commit -m "Added testing results to TESTING_LOG.txt"
git commit -m "Updated conversion guide with troubleshooting steps"
git commit -m "Tested import to PLC Copilot - ladder logic displays correctly"
```

---

## Common Commands Reference

| Task | Command |
|------|---------|
| Clone repo (first time) | `git clone https://github.com/Recipout/p5x-to-l5x-converter.git` |
| Get latest changes | `git pull` |
| See what changed | `git status` |
| Add all changes | `git add .` |
| Commit changes | `git commit -m "message"` |
| Send to GitHub | `git push` |
| Check commit history | `git log` |

---

## Workflow Tips

### Before Making Changes
- Always run `git pull` first
- This prevents conflicts if the repository changed elsewhere

### Commit Frequently
- Make small, focused commits
- Use clear, descriptive messages
- Makes it easier to track progress

### Test Locally Before Pushing
- Run your conversion script
- Verify outputs are correct
- Test imports to PLC Copilot
- Then push results to repository

### Document As You Go
- Add notes to TESTING_LOG.txt
- Update documentation files
- Commit these notes with your results

---

## Which Method Should You Use?

### Use Option 1 (Local + Push) If:
- You're actively developing the script
- You run frequent tests locally
- You want to track changes with commit messages
- You work offline and sync when done

### Use Option 2 (GitHub Web) If:
- You're making quick documentation updates
- You want to add notes or testing results
- You don't have Git installed
- You're on a different computer

### Use Option 3 (GitHub Desktop) If:
- You prefer graphical interfaces
- You're new to command-line Git
- You want visual confirmation of changes
- You work with multiple repositories

---

## Quick Start - Today

1. **Open Command Prompt**
2. **Navigate to your repository folder** (or clone it):
   ```cmd
   git clone https://github.com/Recipout/p5x-to-l5x-converter.git
   cd p5x-to-l5x-converter
   ```
3. **Make your changes** (run conversion, test, document)
4. **Sync back:**
   ```cmd
   git add .
   git commit -m "Your message"
   git push
   ```

Your work is now in the repository and accessible from anywhere.

---

## Next Steps

After following this workflow:
- Your local changes are backed up on GitHub
- You can access your work from any machine
- Your commit history shows what was done and when
- You can revert to previous versions if needed
- Collaborators can see your progress

For more help:
- GitHub Guides: https://guides.github.com/
- Git Documentation: https://git-scm.com/doc
