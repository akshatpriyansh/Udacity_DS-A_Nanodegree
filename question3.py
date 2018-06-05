"""
Q. Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad", then the
function returns True. Your function definition should look like:	
question1(s, t) and return a boolean True or False.


Author:
Akshat Priyansh
"""

def question3(G):
	"""

	Input - Edge List
	Output - Edge List
	

	""" 
	example = {}									# for validation
	if(type(G) != type(example) ):
		return -1
	vertices = G.keys()								# Vertices are the keys in the G dictionary
	edges = set()									
	for vertex in vertices:							# O(V * E(V))
		for j in G[vertex]:
			if vertex > j[0]:						# Sorting the characters on basis on their value,
				edges.add((j[1],j[0],vertex))		# So (A,B) and (B,A) are not considered as separate edges
			elif vertex < j[0]:
				edges.add((j[1],vertex, j[0]))


	sorted_set = sorted(edges)						# Set takes care of duplicate edges, we sort on basis of edge weight

	output_list = []
	vertices = [set(x) for x in vertices]			# Generating individual groups for each vertex

	for edge in sorted_set:							# O(V * E)
		for vertice in xrange(len(vertices)):
			if edge[1] in vertices[vertice]:		# The two if conditions find the index value of group the element is in
				index1 = vertice
			if edge[2] in vertices[vertice]:		
				index2 = vertice

		if(index1 > index2):														# The below two if conditions make sure the index 
			vertices[index2] = set.union(vertices[index1],vertices[index2])			# in not in the same group. 
			vertices.pop(index1)													# Because if they are, it means cycle will be present.
			output_list.append(edge)	

		if(index1 < index2):														# The idea is to merge groups until only a single group is left
			vertices[index1] = set.union(vertices[index1],vertices[index2])			# Then we know that we need to break
			vertices.pop(index2)
			output_list.append(edge)

		if(len(vertices)==1):														# break when groups are 1. Our result is in form of a list. We need to construct an edge list
			break	

	output_dict = {}

	for edge in output_list:														# Constructing edge list
		if edge[1] in output_dict:
			output_dict[edge[1]].append((edge[2],edge[0]))
		else:
			output_dict[edge[1]] = [(edge[2],edge[0])]

		if edge[2] in output_dict:
			output_dict[edge[2]].append((edge[1],edge[0]))
		else:
			output_dict[edge[2]] = [(edge[1],edge[0])]

	return output_dict

"""

Calculated Algorithmic Complexity - O(E * V)

"""

# Test Cases - Tested for null, edge, special and large input cases


# Null Case

G0 = {}

print question3(G0) 
# {}


# Not a Graph Case

G1 = ['B','C','D']

print question3(G1)
# -1


#Base Cases

G1 = {	'A': [('B', 2)],
 		'B': [('A', 2), ('C', 5)], 
 		'C': [('B', 5)]

 		}

H1 = {	'A' :[('B',2)],
		'B': [('A',2),('C',5)],
		'C' : [('B',5)]  

		}


print question3(G1) 


G2 = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}

H2 = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]}

print question3(G2)

