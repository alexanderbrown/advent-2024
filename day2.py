import csv
import numpy as np

# Load the data

reports = []
with open('data\\day2_input.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        reports.append(np.array([int(x) for x in row]))

# To be safe, reports must be monotonic and have no differences greater than 3

def is_safe(report: list[int]):
    diffs = np.diff(report)
    if np.any(np.abs(diffs) > 3):
        return False
    is_monotonic = np.all(diffs > 0) or np.all(diffs < 0)
    return is_monotonic

safe = 0
for report in reports:
    safe += is_safe(report)

print(safe)

# Allow one bad example per report - try all possible subsets

safe = 0
for report in reports:
    for i in range(len(report)):
        test_report = np.delete(report, i)
        if is_safe(test_report):
            safe += 1
            break

print(safe)
    
    