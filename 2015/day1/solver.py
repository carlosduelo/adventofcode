counter = 0
with open('./data', 'r') as data:
    for line in data:
        for c in line:
            if c == '(':
                counter +=1
            elif c == ')':
                counter -=1
assert counter == 74
