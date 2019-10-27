# a represents the array 
# n : Number of elements in array a 
def getMissingNo(a, n):  
    i, total = 0, 1
  
    for i in range(2, n + 2): 
        total += i 
        total -= a[i - 2] 
    return total 
  
# Driver Code 
arr = [1, 2, 3, 5] 
print(getMissingNo(arr, len(arr))) 

  
def getMissingNo1(a, n): 
    x1 = a[0] 
    x2 = 1
      
    for i in range(1, n): 
        x1 = x1 ^ a[i] 
          
    for i in range(2, n + 2): 
        x2 = x2 ^ i 
      
    return x1 ^ x2 
  
# Driver program to test above function 
# if __name__=='__main__': 
  
a = [1, 2, 4, 5, 6] 
n = len(a) 
miss = getMissingNo1(a, n)  
print(miss) 


# a represents the array 
# n : Number of elements in array a 
def getMissingNo2(a, n):  
    i, total = 0, 1
  
    for i in range(2, n + 2): 
        total += i 
        total -= a[i - 2] 
    return total 
  
# Driver Code 
arr = [1, 2, 3, 5] 
print(getMissingNo2(arr, len(arr))) 