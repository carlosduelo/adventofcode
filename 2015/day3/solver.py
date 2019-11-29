houses = {(0,0): 1}

current = (0,0)
with open('./data', 'r') as lines:
    for line in lines:
        for move in line:
            if '^' == move:
                current = (current[0]+1, current[1])
            elif '>' == move:
                current = (current[0], current[1]+1)
            elif 'v' == move:
                current = (current[0]-1, current[1])
            elif '<' == move:
                current = (current[0], current[1]-1)
            presents = houses.get(current, 0) + 1
            houses[current] = presents
assert 2565 == len(houses)

houses = {(0,0): (1,1)}
current_s = (0,0)
current_r = (0,0)
santa = True
with open('./data', 'r') as lines:
    for line in lines:
        for move in line:
            if '^' == move:
                if santa:
                    current_s = (current_s[0]+1, current_s[1])
                else:
                    current_r = (current_r[0]+1, current_r[1])
            elif '>' == move:
                if santa:
                    current_s = (current_s[0], current_s[1]+1)
                else:
                    current_r = (current_r[0], current_r[1]+1)
            elif 'v' == move:
                if santa:
                    current_s = (current_s[0]-1, current_s[1])
                else:
                    current_r = (current_r[0]-1, current_r[1])
            elif '<' == move:
                if santa:
                    current_s = (current_s[0], current_s[1]-1)
                else:
                    current_r = (current_r[0], current_r[1]-1)
            if santa:
                presents = houses.get(current_s, (0,0))
                houses[current_s] = (presents[0] + 1, presents[1])
            else:
                presents = houses.get(current_r, (0,0))
                houses[current_r] = (presents[0], presents[1] + 1)
            santa = not santa
assert len(houses) == 2639
