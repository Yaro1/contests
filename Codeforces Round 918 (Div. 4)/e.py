import sys
# Python program for the above approach

# Returns the maximum length


def maxLen(arr):

	# NOTE: Dictionary in python is
	# implemented as Hash Maps
	# Create an empty hash map (dictionary)
	hash_map = {}

	# Initialize result
	max_len = 0

	# Initialize sum of elements
	curr_sum = 0

	# Traverse through the given array
	for i in range(len(arr)):

		# Add the current element to the sum
		curr_sum += arr[i]

		if curr_sum == 0:
			max_len = i + 1

		# NOTE: 'in' operation in dictionary
		# to search key takes O(1). Look if
		# current sum is seen before
		if curr_sum in hash_map:
			max_len = max(max_len, i - hash_map[curr_sum])
		else:

			# else put this sum in dictionary
			hash_map[curr_sum] = i

	return max_len



def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    prefix_check = []
    for i in range(n):
        if i % 2 == 0:
            prefix_check.append(a[i])
        else:
            prefix_check.append(-a[i])
    prefix = [prefix_check[0]]
    for i in range(1, len(prefix_check)):
        prefix.append(prefix[-1] + prefix_check[i])
    d = {0: True}
    for i in prefix:
        if i in d:
            print("YES")
            return
        else:
            d[i] = True
    print("NO")

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# 2 5 10 4 4 9 6 7 8
# -3 5 6 0 -5 -3 -1 1