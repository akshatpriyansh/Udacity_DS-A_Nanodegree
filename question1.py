"""
Q. Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad", then the
function returns True. Your function definition should look like:	
question1(s, t) and return a boolean True or False.


Author:
Akshat Priyansh
"""
def question1(s1,s2):

	"""
	Input - String, String

	Output - Boolean

	"""
	if(len(s1)<1 or len(s2)<1):				# Null Case
		return False

	if(len(s2)>len(s1)):					# O(1)
		temp = s2
		s2 = s1
		s1 = temp 


	(l1,l2) = convert_to_chars(s1,s2)		# call function to convert strings to char lists
	l1 = sorted(l1)							# O(n log(n))

	for char in l2:							# O(n) loop for traversing in List
		index = binary_search(l1,char)		# O(log n) for checking character in list (Binary Search)
		if(index>=0):						
			del l1[index]					# If the character to be checked is found, we delete it
			continue						# so that it is not looked up again
		else:
			return False					# Return false if not anagram
	return True								# Return true is anagram

def binary_search(arr,value):

	"""

	Binary Search Iterative Implementation

	This method searches for a character value in a list of characters

	Complexity - O(log(n))

	"""

	low = 0
	high = len(arr)-1

	while(low<=high):
		mid = low + (high-low)/2			# (high-low)/2 is not suggested to be computed for finding mid index, index low+(high-low)/2
		if(arr[mid]==value):				# if found, return index
			return mid
		else:
			if ord(arr[mid])<ord(value):	# compare on basis of ASCII values
				low = mid + 1
			else:
				high = mid - 1
	return -1

def convert_to_chars(s1,s2):

	"""
	Helper method

	This method takes two strings as input and returns lists of characters

	Example Input : "Akshat"
	Example Output : ['A','k','s','h','a','t']
	"""

	list1 = list(s1)
	list2 = list(s2)
	return list1,list2


"""

Calculated Algorithmic Complexity - O( n + n log(n) + log(n) ) ~ average case complexity O(n log(n))

"""

# Test Cases - Tested for null, edge, special and large input cases




# Empty String
print question1("asd","")
#False

# Simple test case.
print question1("app", "paple")
# True

# Test case with a space character.
print question1(" ", "a space")
# True

# Test case with numbers.
print question1("15", "4732890793878894351")
# True

# Test case with punctuation.
print question1("$ %", "100% $Expensive")
# True

# Test case that returns false.
print question1("music", "muscle")
# False

print question1("udacity", "cityuda")
#True

# Test case with large input
print question1("uniuansdiunasuidniuanjkanjkfnajbianiquiotuweoiyrpquyoipwueyriopwjioeywiopeuryioem,nbcvcxcmvnx,mcvb,znm09___jan____809135790`3-2591-053;4p3,konduin","jan")
#True