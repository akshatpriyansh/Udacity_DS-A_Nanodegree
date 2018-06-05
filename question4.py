"""

Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, but if both nodes are
descendents of the root's left child, then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), where T is the tree represented as 
a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents 
a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers 
representing the two nodes in no particular order.

Author:
Akshat Priyansh
"""

def question4(T,r,n1,n2):
	"""
	Input - Matrix (List of lists), Root (int), Node1 (int), Node2(int)
	Output - Lowest Common Ancestor (int)

	"""

	if(len(T)<=1):								# Edge case : If the Tree only consists of a root and no children
		return -1

	if(n1==None or n2==None):					# Edge case : If n1 and n2 are not actually numbers
		return -1

	len_T = len(T)
	if(not n1 < len_T or not n2 < len_T):		# Edge case : If the nodes gives in parameters do not actually exist in the tree
		return -1

	n1_list = []						
	n2_list = []

	for i in range(len(T)):						# Traverse the list and append all the parents of node1 if found in O(N)
		if T[i][n1]==1:
			n1_list.append(i)

	for i in range(len(T)):						# Traverse the list and append all the parents of node2 is found in O(N)
		if T[i][n2]:
			n2_list.append(i)

												# The root is a common ancestor of every node in the tree
	if not r in n1_list:						# check if the root is in the list, if not, add it
		n1_list.append(r)

	if not r in n2_list:						# check if the root is in the list, if not, add it
		n2_list.append(r)

	n1_list = reversed(n1_list)					# Since we are operating on a binary tree, we sort
	for i in n1_list:							# in decending order to operate on the latest nodes
		if i in n2_list:						# if a match is found, we know that it is the lowest common ancestor
			return i 							# If nothing is found, the root node is bound to be returned. And it correct.


 
"""
 
Calculated Algorithmic Complexity - O(n)
 
"""


M = [[0, 1, 0, 0, 0]]
print question4(M,3,1,4) 
# -1

# node does not exist in tree

M = [[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0]]

print question4(M,3,8,4) 
# -1

# Normal Case

M = [[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0]]

print question4(M,3,1,4) 
# 3
