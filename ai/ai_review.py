import os

print("AI Code Review Started")

files = os.popen("git diff --name-only HEAD~1").read()

print("Changed Files:")
print(files)

print("AI Review Completed")