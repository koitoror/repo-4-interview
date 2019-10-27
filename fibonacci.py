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
  
print(fibonacci(9)) 

# fibonacci(9)

def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci2(9)) 