import math

def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) / 2
        if value < data[math.floor(middle)]:
            right = middle - 1
        elif value > data[math.floor(middle)]:
            left =  math.floor(middle) + 1
        else:
            return math.ceil(middle)
    raise ValueError('Value is not in the list')
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))