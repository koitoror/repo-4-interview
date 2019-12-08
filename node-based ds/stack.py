
# def createStack(): 
# 	stack = [] 
# 	return stack 

# def isEmpty(stack): 
# 	return len(stack) == 0

# def push(stack, x): 
# 	stack.append(x) 

# def pop(stack): 
# 	if isEmpty(stack): 
# 		print("Error : stack underflow") 
# 	else: 
# 		return stack.pop() 


# class Stack():
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def is_empty(self):
#         return self.items == []

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#     def get_stack(self):
#         return self.items


class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None