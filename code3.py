# Problem 3 – Communication Channel Analyzer Problem Statement
# A communication system sends messages as a continuous stream of lowercase characters.
# To avoid signal interference, a valid communication window must contain no repeated characters.

# Your task is to determine the length of the longest valid continuous segment of the stream that satisfies this condition.

 

# Input Format
# ·      A single line containing a string s

 

# Output Format
# Print a single integer — the length of the longest valid segment.

 

# Constraints
# ·      1 ≤ len(s) ≤ 10⁵

# ·      s contains only lowercase English letters

 

# Sample Input
# abcabcbb

# Sample Output
# 3

 

# Explanation
# ·      The substring "abc" contains no repeated characters and has length 3.

# ·      When the character 'a' repeat, the current segment can no longer be extended.

# ·      Subsequent substrings such as "bca" and "cab" also have length 3.

# ·      No valid substring longer than 3 exists in the input.

# Hence, the longest valid continuous segment has length:

# 3

 

 

# Another Example
# Input

# pwwkew

# Output

# 3

 

# Explanation

# ·      "pw" is valid (length = 2).

# ·      "wke" is valid (length = 3).

# ·      Any longer segment contains repeated characters.



def continuous_alphabet(a):
	char_set = set()
	b = 0
	c = []
	d = []
	e = []
	for i in range(len(a)):
		if a[0] != a[1]:
			c
		for i in range(len(c)):
			if a[0] != len(c):
				b += 1
			else:
				a[0] == len[c]:
				return 0
		
				
		else:
			a[0] == a[1]
			return 0
        	e
		largest = max(e)
		print(largest)
		return 


# input = abcabcbb

# a = 1                   1
# b = 1			2  ----------------> 3
# c = 1			3


# a = 1                   1
# b = 1			2  -----------------> 3
# c = 1			3

# b = 1			1  -----------------> 1
# b = 1			1  -----------------> 1



# pwwkew

# p = 1                   1
# w = 1			2  ----------------> 2


# w = 1			3
# k = 1                   1  ----------------> 3
# e = 1			2


# w = 1			3  ----------------> 1
















