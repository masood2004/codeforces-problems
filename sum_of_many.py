import sys

total = 0
for line in sys.stdin:
    total += int(line.strip())
print(total)
