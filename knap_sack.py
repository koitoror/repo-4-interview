# A naive recursive implementation of 0-1 Knapsack Problem 

# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(C, wt, val, n): 
# def knapSack(n, C)

	# Base Case 
	if n == 0 or C == 0 : 
		return 0


	# If weight of the nth item is more than Knapsack of capacity 
	# W, then this item cannot be included in the optimal solution 
	elif (wt[n-1] > C): 
		return knapSack(C, wt, val, n-1)
 
	# elif w[n-1] > C:
	# 	result = knapSack(n-1, C)

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		tmp1 = val[n-1] + knapSack(C-wt[n-1], wt, val, n-1)
		tmp2 = knapSack(C, wt, val, n-1)
		# print(tmp1, tmp2)
	
		return max(tmp1, tmp2) 

 		# tmp1 = v[n-1] + knapSack(n-1, C-w[n-1])
		# tmp2 = knapSack(n-1, C)
		# result = max(tmp1, tmp2)
# end of function knapSack 

# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
C = 50
n = len(val) 
print (knapSack(C, wt, val, n)) 


# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
	
	# print(K)

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
				# print(K[i][w], end = "")
			elif wt[i-1] <= w: 
				# print('\n')
				# print(K[i][w], end = "")
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) 
			else: 
				# print(K[i-1][w], end = "")
				K[i][w] = K[i-1][w] 
				
				
	return K[n][W] 

# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 


# def kSack(C, wt, val):
# 	ratios = []
# 	for i in n-1:
# 		ratio = val/wt
# 		ratio.append(ratio)
# 		if ratio = max(ratio):
# 			p = C-val
# 			return kSack(P, val)
# 			if ratio
