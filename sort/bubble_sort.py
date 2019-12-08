# def bubbleSort(arr):
#     n = len(arr)
 
#     # Traverse through all array elements
#     for i in range(n):
 
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
 
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
 
# bubbleSort(arr)
 
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i])


def bubble_sort(L):
    n = len(L)-1
    # print(len(L))
    for num in range(n,0,-1):
        print(num)
        print(L[num])
        for i in range(num):
            print(i)
            print(L[i])
            print(L[i+1])
        #     if L[i]>L[i+1]:
        #         L[i], L[i+1] = L[i+1], L[i]

    return L


def short_bubble_sort(L):
    """
    Args:
        L (list): A list of sortable items.

    Returns:
        A tuple of number of passes through L (for demonstration purposes) and the sorted list.

    """
    swaps = True
    for passnum in range(len(L) - 1, 0, -1):
        swaps = False

        for i in range(passnum):
            if L[i]>L[i+1]:
                swaps = True
                L[i], L[i+1] = L[i+1], L[i]
        if not swaps:
            return len(L)-passnum, L 

    return len(L)-1, L


L = [55,68,93,77]
print(bubble_sort(L))
print(short_bubble_sort(L))