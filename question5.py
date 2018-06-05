"""
Q. Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), where ll is the first node of a linked list 
and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.


class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = None


Author:
Akshat Priyansh
"""

class Node(object):									# Contructing Node Class

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):							# Construction LinkedList Class

	def __init__(self, value):
		self.root = Node(value)

	def question5(self, value):						# Main Function
		total_nodes = self.no_of_nodes()			# Counts the number of nodes in the Linked List

		if(value >= total_nodes or value==None):	# Handling edge case and null input 
			return -1

		index = total_nodes - value					# Index is calculated from total number of nodes - index -  O(n)
		curr = self.root
		count = 1
		while(curr):								# O(n)
			if(count == index):						# When count becomes equal to index, we have arrived at our target node
				return count
			else:
				curr = curr.next					# Else iterate forward and increase count
				count += 1

	def append(self, value):						# Adds a node to the front of the LinkedList
		curr = self.root
		while(curr.next):							# O(n)
			curr = curr.next

		curr.next = Node(value)

	def no_of_nodes(self):							# Counts the number of nodes in the LinkedList
		curr = self.root
		count = 0
		while(curr):								# O(n)
			count +=1 
			curr = curr.next
		return count

	def print_list(self):							# Prints the linked List
		curr = self.root
		while(curr):								# O(n)
			print(curr.data)
			curr = curr.next

"""

Calculated Algorithmic Complexity - O(n)

"""

# Constructing and adding nodes to the Linked List

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)

## Test Cases

# Empty Values
print ll.question5(" ")
# -1

# Incorrect Value
print ll.question5("hello")
# -1

# input more that the index
print ll.question5(9)
# -1

# Last node
print ll.question5(0)
# 8

# Middle node
print ll.question5(4)
# 4


