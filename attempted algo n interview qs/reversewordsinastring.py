# s = input() \
s = "i like this program very much"

print()
# METHOD 1

words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)
print("Reversed String:") 
print(" ".join(string)) 


print()
# METHOD 2

print
print("Reversed String 2:") 

h = ' '.join(s.split(' ')[::-1])

print(h)

