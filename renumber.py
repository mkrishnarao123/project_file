import re

with open('python_answers.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('ADDITIONAL TOPICS')
before = content[:idx]
after = content[idx:]

# Replace from highest to lowest to avoid conflicts (e.g., 1 matching in 100)
for old in range(125, 80, -1):
    new_num = old - 80
    after = after.replace(f'\r\n{old}. ', f'\r\n{new_num}. ')
    after = after.replace(f'\n{old}. ', f'\n{new_num}. ')

with open('python_answers.txt', 'w', encoding='utf-8') as f:
    f.write(before + after)

# Verify
with open('python_answers.txt', 'r', encoding='utf-8') as f:
    c = f.read()

if '1. What is Singleton' in c:
    print("SUCCESS: Renumbered 81-125 to 1-45")
else:
    print("FAILED: Check the file")
