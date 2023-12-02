import os

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as f:
    lines = f.readlines()
result = 0

for line in lines:
    digits = [c for c in line.strip() if c.isdigit()]
    result += int(digits[0] + digits[-1])

print(result)
