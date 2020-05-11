def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" "),

# Python Program for implementation of 
# Recursive Bubble sort 

def bubble_sort(arr): 
	for i, num in enumerate(arr): 
		try: 
			if arr[i+1] < num: 
				arr[i], arr[i+1] = arr[i+1], num 
				bubble_sort(arr) 
		except IndexError: 
			pass
	return arr 

arr = [64, 34, 25, 12, 22, 11, 90] 
bubble_sort(arr) 

print()
print()
print("Sorted array:"); 
for i in range(0, len(arr)): 
	print(arr[i], end=' ') 
 
