# Problem 1 – Time Slot Consolidation Problem Statement
# A logging system records the time ranges during which a service was active.
# Due to multiple restarts and partial logging, the recorded time ranges may overlap or be out of order.

# Your task is to consolidate the recorded time ranges so that the final output contains the minimum number of non-overlapping time ranges that fully represent the active duration of the service.

 

# Input Format
# ·      The first line contains an integer n, the number of recorded time ranges

# ·      The next n lines each contain two integers start and end

 

# Output Format
# Print the consolidated time ranges in ascending order of start time.
# Each range should be printed on a new line as start end.

 

# Constraints
# ·      1 ≤ n ≤ 10⁵

# ·      0 ≤ start ≤ end ≤ 10⁹

# ·      Input ranges are not guaranteed to be sorted
# Sample Input
# 4

# 1 3

# 2 6

# 8 10

# 15 18

# Sample Output
# 1 6

# 8 10

# 15 18

def non_overlaping(a):
   a.sort(d = lambda x: x[0])
    
    a = []
for i in range(len(a)):
	if a[0] ==a[1] && a[0]<=a[1] && a[-1] > a[0]:
		return 0
	else:
		a[0] > a[1]
		return a

# explanation: 

# 1 != 3						a[1]
# 3 < 2							a[1]
# 2 > 6 						a[1, 6]
# 6 > 8							a[8]
# 8 > 10 						a[8, 10]
# 10 > 15 						a[15]
# 15 > 18 						a[15, 18]
