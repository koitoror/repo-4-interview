# s = input() \
s = "i like this program very much"

print()
# METHOD 1

words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)
print("Reversed String 1:") 
print(" ".join(string)) 


print()
# METHOD 2
print("Reversed String 2:") 

h = ' '.join(s.split(' ')[::-1])
print(h)

print()
# METHOD 3
print("Reversed String 3:")
## initializing the string
string = "I am a python programmer"
## splitting the string on space
words = string.split()
# print(words)
## reversing the words using reversed() function
words = list(reversed(words))
# print(words)
## joining the words and printing
print(" ".join(words))