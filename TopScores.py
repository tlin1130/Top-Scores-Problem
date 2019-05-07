
# Given a list of unsorted scores in range[0,highest_possible_scores],
# fastsort() sorts the list in O(n) time and space using a dictionary
def fastsort(highest_possible_score, unsorted_scores):

	dictionary = {}
	sorted_scores = [None] * len(unsorted_scores)
	index = 0 

	for each_score in unsorted_scores:

		if each_score in dictionary:
			dictionary[each_score] += 1
		else:
			dictionary[each_score] = 1

	for i in range(0,highest_possible_score + 1):

		if not(i in dictionary):
			continue
		else:

			value = dictionary[i]

			for j in range(index, index + value):
				sorted_scores[j] = i

			index = index + value

	return sorted_scores

# test code
highest_possible_score = 100

unsorted_scores = [37,89,41,65,91,53]
result = fastsort(highest_possible_score, unsorted_scores)
print result
# result = [37,41,53,65,89,91]

unsorted_scores = [3,10,20,10,7,3]
result = fastsort(highest_possible_score, unsorted_scores)
print result
# result = [3,3,7,10,10,20]

unsorted_scores = [100,50,70,20,20,30,60,80,60,100]
result = fastsort(highest_possible_score, unsorted_scores)
print result
# result = [20,20,30,50,60,60,70,80,100,100]
