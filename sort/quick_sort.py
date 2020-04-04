# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 

    # print(i, end=' ')
    # print(high, end=' ')
    # print()

    # print(low)
    # print(high)

    for j in range(low , high):

        # arr = [10, 7, 8, 9, 1, 5] 
        # print(low)
        # print(high)

        # If current element is smaller than or 
        # equal to pivot 

        if   arr[j] <= pivot:
            # print(low)
            # print(high) 
            print('    arr[i= {}]='.format(i), arr[i], '     arr[j= {}]='.format(j), arr[j], sep='\t')
            # print()
            print(pivot)
            print()
            

            # increment index of smaller element 
            i +=1
            
            print('    arr[i= {}]='.format(i), arr[i], '     arr[j= {}]='.format(j), arr[j], sep='\t')
            # print('arr[i= {}]='.format(i), arr[i])
            # print('arr[j= {}]='.format(j), arr[j])
            # print()
            print(pivot)
            print()

            arr[i],arr[j] = arr[j],arr[i] 
            
            print('    arr[i= {}]='.format(i), arr[i], '     arr[j= {}]='.format(j), arr[j], sep='\t')
            # print('arr[i= {}]='.format(i), arr[i])
            # print('arr[j= {}]='.format(j), arr[j])
            # print()
            print(pivot)
            print()

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    # print(low)
    # print(high)
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pivot_index = partition(arr,low,high) 
        # print(pivot_index)
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pivot_index-1) 
        quickSort(arr, pivot_index+1, high) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end=' '), 
# print(arr)
  