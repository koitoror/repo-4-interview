def test():
    global x 
    x = 'local y'

    print (x)

test()
print (x)
