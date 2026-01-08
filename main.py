
print("My first push")


print("hello world")
print("This is made on ivy's branch")
print("This was made on master branch")

from math_utils import add

print("Welcome to Math App")
print("Sum:", add(2, 3))

# ✅ Git Merge Without Conflicts (Python Example)

# The key idea:
# ➡️ Each branch edits a different file (or different functions).

# 📁 Project Structure
# git-merge-no-conflict/
# │
# ├── main.py
# ├── math_utils.py

# 🟢 Step 1: Initialize Project (main branch)
# main.py
# from math_utils import add

# print("Sum:", add(2, 3))

# math_utils.py
# def add(a, b):
#     return a + b

# Commit
# git init
# git add .
# git commit -m "Initial project with add function"

# 🌿 Step 2: Feature Branch 1 (feature-subtract)
# git checkout -b feature-subtract

# Modify math_utils.py
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# Commit
# git add math_utils.py
# git commit -m "Add subtract function"

# 🌿 Step 3: Feature Branch 2 (feature-message)
# git checkout main
# git checkout -b feature-message

# Modify main.py
# from math_utils import add

# print("Welcome to Math App")
# print("Sum:", add(2, 3))

# Commit
# git add main.py
# git commit -m "Add welcome message"

# 🔀 Step 4: Merge Branches into Main (No Conflicts)
# Merge first branch
# git checkout main
# git merge feature-subtract

# Merge second branch
# git merge feature-message


# ✅ No conflicts occur because:

# feature-subtract modified math_utils.py

# feature-message modified main.py

# 🧹 Step 5: Delete Feature Branches
# git branch -d feature-subtract
# git branch -d feature-message

# ▶️ Step 6: Run the Program
# python main.py


# Output:

# Welcome to Math App
# Sum: 5

# 🧠 Why No Conflicts?

# ✔ Different files were modified
# ✔ Git can auto-merge safely
# ✔ Clean commit history

# 💡 Pro Tips to Avoid Conflicts

# One feature → one file

# Keep branches short-lived

# Pull main frequently

# Merge often

