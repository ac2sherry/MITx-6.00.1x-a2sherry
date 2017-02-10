# Problem 1
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained
#  in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#   For example, if s = 'azcbobobegghakl', your program should print:

s = 'azcbobobegghakl'
vowel = 0
for char in s:
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		vowel += 1

print('Number of vowels:',vowel)

# Problem 2
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' 
# occurs in s. For example, if s = 'azcbobobegghakl', then your 
# program should print
s = 'azcbobobegghakl'
bob = 0
for idx in range(0,len(s)):
	if s[idx:idx+3] == 'bob':
		# print(s[idx:idx+3],idx)	
		bob += 1

print('Number of times bob occurs is:',bob)

# Problem 3
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in 
# which the letters occur in alphabetical order. For example, 
# if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example,
# if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
s = 'azcbobobegghakl'
# s = 'abcbcd'
# s = 'abcdefghijklmnopqrstuvwxyz'
# s = 'rxicvftvv'
# s = 'rdrdnzbacmiijhstnjg'
# s = 'zyxwvutsrqponmlkjihgfedcba'

s_max = s[0] 						# 初始化第一个字符
s_max_tmp = s[0]				
for idx in range(1,len(s)):			# 从第二字符开始
	if s[idx] >= s[idx - 1]:		# 当前字符比前一字符大
		s_max_tmp += s[idx]			# 临时变量字符串求和
	else:
		s_max_tmp = s[idx]			# 重新初始化临时变量
	if len(s_max)<len(s_max_tmp):
		s_max = s_max_tmp

print('Longest substring in alphabetical order is: ',s_max)

