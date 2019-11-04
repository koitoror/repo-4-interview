# Function for nth fibonacci number 

FibArray = [0,1] 
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
# Driver Program 
print (fibonacci(9))
print (fibonacci(0)) 
print (fibonacci(2)) 
print (fibonacci(-1)) 

def fibonacci2(n):
    if n < 0:
        return "enter a valid number"
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci2(9)) 
print (fibonacci2(0)) 
print (fibonacci2(-1)) 


def fbn(n):
    if n < 0:
        return "enter a valid number"
    elif 0 <= n <= 1:
        return n 
    return fbn(n-1) + fbn(n-2)
print (fbn(9)) 
print (fbn(0)) 
print (fbn(-1)) 

"""Fibonacci series module"""
def fibo(n):    
    FiboList=[]
    a,b=0,1
    while b<n:
        FiboList.append(b)
        a, b = b, a+b
    return FiboList
if __name__== "__main__":
    print ("Fibonacci series", fibo(100))


def fibonacci(n):
    fibolist=[]
    if n < 0:
        return "incorrect input"
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci(9))
print (fibonacci(1))

# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
	
	# Taking 1st two fibonacci nubers as 0 and 1 
	FibArray = [0, 1] 
	
	while len(FibArray) < n + 1: 
		FibArray.append(0) 
	
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = fibonacci(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = fibonacci(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 
	
print (fibonacci(2)) 

# Taking 1st two fibonacci numbers as 0 and 1 
  
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
# Driver Program 
  
print (fibonacci(9))
print (fibonacci(2)) 

# Helper function that multiplies 
# 2 matrices F and M of size 2*2, 
# and puts the multiplication 
# result back to F[][] 

# Helper function that calculates 
# F[][] raise to the power n and 
# puts the result in F[][] 
# Note that this function is 
# designed only for fib() and 
# won't work as general 
# power function 
def fib(n): 
	F = [[1, 1], 
		[1, 0]] 
	if (n == 0): 
		return 0
	power(F, n - 1) 
	
	return F[0][0] 

def multiply(F, M): 

	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0]) 
	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1]) 
	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0]) 
	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1]) 
	
	F[0][0] = x 
	F[0][1] = y 
	F[1][0] = z 
	F[1][1] = w 

def power(F, n): 

	M = [[1, 1], 
		[1, 0]] 

	# n - 1 times multiply the 
	# matrix to {{1,0},{0,1}} 
	for i in range(2, n + 1): 
		multiply(F, M) 

# Driver Code 
if __name__ == "__main__": 
	n = 9
	print(fib(n)) 

# Fibonacci Series using 
# Optimized Method 

# function that returns nth 
# Fibonacci number 
def fib(n): 
	
	F = [[1, 1], 
		[1, 0]] 
	if (n == 0): 
		return 0
	power(F, n - 1) 
		
	return F[0][0] 
	
def multiply(F, M): 
	
	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0]) 
	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1]) 
	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0]) 
	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1]) 
	
	F[0][0] = x 
	F[0][1] = y 
	F[1][0] = z 
	F[1][1] = w 
		
# Optimized version of 
# power() in method 4 
def power(F, n): 

	if( n == 0 or n == 1): 
		return; 
	M = [[1, 1], 
		[1, 0]]; 
		
	power(F, n // 2) 
	multiply(F, F) 
		
	if (n % 2 != 0): 
		multiply(F, M) 
	
# Driver Code 
if __name__ == "__main__": 
	n = 9
	print(fib(n)) 

# Python 3 Program to find n'th fibonacci Number in 
# with O(Log n) arithmatic operations 
MAX = 1000

# Create an array for memoization 
f = [0] * MAX

# Returns n'th fuibonacci number using table f[] 
def fib(n) : 
	# Base cases 
	if (n == 0) : 
		return 0
	if (n == 1 or n == 2) : 
		f[n] = 1
		return (f[n]) 

	# If fib(n) is already computed 
	if (f[n]) : 
		return f[n] 

	if( n & 1) : 
		k = (n + 1) // 2
	else : 
		k = n // 2

	# Applyting above formula [Note value n&1 is 1 
	# if n is odd, else 0. 
	if((n & 1) ) : 
		f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
	else : 
		f[n] = (2*fib(k-1) + fib(k))*fib(k) 

	return f[n] 


# Driver code 
n = 30
print(fib(n)) 

import math

def fib(n):   
    phi = (1 + math.sqrt(5)) / 2;  
    # return round(pow(phi, n) / math.sqrt(5));  
    return int (pow(phi, n) // math.sqrt(5))

 
# Driver Code 
n = 30;  
print (fib(n)) ; 
