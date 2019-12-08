import collections
lst = collections.deque()

# Inserting elements at the front
# or back takes O(1) time:
lst.append('B')
lst.append('C')
lst.appendleft('A')
lst
# deque(['A', 'B', 'C'])

# However, inserting elements at
# arbitrary indexes takes O(n) time:
# lst.insert(2, 'X')
lst
# deque(['A', 'B', 'X', 'C'])

# Removing elements at the front
# or back takes O(1) time:
lst.pop()
# 'C'
lst.popleft()
# 'A'
lst
# deque(['B', 'X'])

# Removing elements at arbitrary
# indexes or by key takes O(n) time again:
# del lst[1]
lst.remove('B')

# Deques can be reversed in-place:
lst = collections.deque(['A', 'B', 'X', 'C'])
lst.reverse()
# deque(['C', 'X', 'B', 'A'])

# Searching for elements takes
# O(n) time:
# lst.index('X')
# 1