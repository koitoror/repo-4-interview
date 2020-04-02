# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    # for i in range(1, len(arr)): 
    for index in range(1, len(arr)):

        # key = arr[i] 
        value = arr[index]

        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        
        # j = i-1
        i = index - 1

        # while j >=0 and key < arr[j] : 
        #         arr[j+1] = arr[j] 
        #         j -= 1
        # arr[j+1] = key 

        while i >=0:
            if value < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = value
                i = i-1
            else:
                break

  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 