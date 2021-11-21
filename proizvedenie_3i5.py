numbers = [3,7,15,6,4,30,25]
new = 1
for x in numbers:
    if x % 3 == 0 and x % 5 == 0:
        new *= x
print (new)
