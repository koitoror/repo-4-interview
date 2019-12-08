class Employee:
    def __init__(self, name):

        self.name = name
    
    def display(self):

        print('My name is - ', self.name)


first = Employee('Rushford')
second = Employee('James')

first.display()
second.display()
