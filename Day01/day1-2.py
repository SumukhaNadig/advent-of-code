import os
import re

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as f:
    lines = f.readlines()
result = 0

digit_map = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "zero" : "0"
}
pattern = r"\d|one|two|three|four|five|six|seven|eight|nine|zero"

for line in lines:
    digits = []
    matched_digit = re.search(pattern, line.strip())
    while matched_digit:
        digits.append(matched_digit.group())
        next_start = matched_digit.start() + 1
        line = line[next_start:]
        matched_digit = re.search(pattern, line)
    digits = [digit_map[digit] if digit in digit_map else digit for digit in digits]
    result += int(digits[0] + digits[-1])

print(result)