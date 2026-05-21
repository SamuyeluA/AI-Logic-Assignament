# Problem 2 – Maximum Signal Strength Problem Statement
# You are monitoring a sensor that records integer signal values at fixed time intervals.
# Due to system limitations, you can only analyze a fixed number of consecutive readings at a time.

# Your task is to determine the maximum total signal strength obtainable from any consecutive block of exactly k readings.

 

# Input Format
# ·      First line: integer n (number of readings)

# ·      Second line: n space-separated integers

# ·      Third line: integer k

 

# Output Format
# Print a single integer representing the maximum total signal strength.

 

# Constraints
# ·      1 ≤ n ≤ 10⁵

# ·      1 ≤ k ≤ n

# ·      Signal values may be negative or positive

# ·      -10⁴ ≤ value ≤ 10⁴

 

# Sample Input
# 6

# 2 1 5 1 3 2

# 3

# Sample Output
# 9

 

#   Explanation
# All possible consecutive blocks of size 3 are evaluated:

# ·      [2, 1, 5] → sum = 8

# ·      [1, 5, 1] → sum = 7

# ·      [5, 1, 3] → sum = 9

# ·      [1, 3, 2] → sum = 6



def max_sig_strength(a, size):
	
	b = []
 # size is 3
	for i in range(len(a)):
		if s >= len(a)
		b = a[0]+a[1]+a[3]
		
		a.remove(a[0])
		
	largest = max(b)
	print(largest)


		
		
# ·      [2, 1, 5] → sum = 8             b = [8]

# ·      [1, 5, 1] → sum = 7             b = [8, 7]

# ·      [5, 1, 3] → sum = 9             b = [8, 7, 9]

# ·      [1, 3, 2] → sum = 6             b = [8, 7, 9, 6]




















