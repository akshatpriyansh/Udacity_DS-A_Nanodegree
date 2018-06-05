"""

Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.

Author:
Akshat Priyansh
"""

def question2(s):

	"""
	Input - String
	Output - String

	"""

	array = []
	str_len = len(s)												# Calculating the length of the string

	if(str_len <= 1):
		if(str_len == 1):
			return s												# Handling empty string case and length==1 case
		return -1

	flag = False													# Flag is set to True if string is of even length,
	if(str_len%2==0):
		flag = True													# Else it is kept False at all times. 
		s = s[:str_len/2] + '|' + s[str_len/2:]						# This is required since if the string is even
																	# we would be inserting a special character in the middle
	for i in range(str_len):										# of the string.
		counter = 0
		j = i
		z = 1														# variable j moves on the same index as i
		x = s[i]													# but scans both sides of the index for palindromic substrings
		while(j-z >= 0 and j+z < str_len and (s[j-z] == s[j+z])):	# In the worst case, the string itself will be a palindrome. O(n^2) 
			counter += 1
			z += 1
		array.append([s[i],counter])								# Append length of each palindromic substring around an index
																	# in an array (int)
	max = -1
	index = -1
	for i in range(len(array)):										# Finding the array member with the highest substring value
		if(array[i][1]>max):										# Can also use max(arr) inbuilt function
			max = array[i][1]										# Extract the index and range
			index = i

	left = s[index-max:index]										# Go to the specific index in the string and get the left side keeping in mind the range
	right = left[::-1]												# Right part will be mirror of left part. Reverse it
	to_return = left + s[index] + right 							# Add the left part , the index and the right part

	if(flag==False):												# if the string was odd, we didn't append the special character. Return string
		return to_return
	else:
		x = to_return.replace('|','')
		return x

"""
 
Calculated Algorithmic Complexity - O( n * n ) ~ (n^2). ( We are traversing the whole array and expanding from each index to both sides)
 
"""

#Null Case
print question2("")
#-1

#Geeks for Geeks even string test case
print question2("forgeeksskeegfor")
#geeksskeeg

print question2("abcbabcbabcba")
#abcbabcbabcba

print question2("azubumiszlsi")
#ubu

print question2("bananas")
#anana