old_str = 'xdhgxxnmbrx'
new_str = ''
for x in old_str:
    if x == 'x':
        new_str += 'y'
    else:
        new_str += x
print (new_str)
