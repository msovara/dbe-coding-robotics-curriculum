# GitHub Repository Setup Instructions

## Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name:** `dbe-coding-robotics-curriculum`
   - **Description:** "Week-long coding and robotics curriculum for DBE teacher training in South Africa"
   - **Visibility:** Choose Public or Private
   - **DO NOT** check "Initialize with README" (we already have one)
   - **DO NOT** add .gitignore or license (we already have them)
3. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

### If you haven't created the repo yet:
```powershell
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/dbe-coding-robotics-curriculum.git
git branch -M main
git push -u origin main
```

### If you already created the repo:
GitHub will show you the exact URL. Copy it and run:
```powershell
git remote add origin <YOUR_REPO_URL>
git branch -M main
git push -u origin main
```

## Step 3: Verify

1. Go to your repository on GitHub
2. You should see all your files
3. The README.md should display on the main page

## Troubleshooting

### If you get authentication errors:
- Use a Personal Access Token instead of password
- Or use GitHub Desktop app
- Or set up SSH keys

### If branch name is different:
- Current branch might be "master" instead of "main"
- Use: `git branch -M main` to rename

### If you need to update later:
```powershell
git add .
git commit -m "Your commit message"
git push
```

