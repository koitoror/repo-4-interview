lst = ['heavensent']

a = ['sent']

for x in lst:
    for b in a: 
        if b in x:
            print (x)
        else:
            print(0)

# def longReverse(x):
#     result = 0
#     remainder = abs(x) % 10

#     while remainder != 0:
#         remainder = 10
#         result += remainder
#         remainder /= 10
#     return result



# print(longReverse(123))

# Time complexity
#n input size
# time: O(n)
# space: O(1)

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    for i in range(n):
            heap_permutation(data, n - 1)
            if n % 2 == 0:
                data[i], data[n-1] = data[n-1], data[i]
            else:
                data[0], data[n-1] = data[n-1], data[0]

    data = [1, 2, 3]
    print (heap_permutation(data, len(data)))