def compute_distance(map):
    m = min([abs(k[0])+abs(k[1]) for k,v in map.items() if len(v) > 1])
    e = min([ sum([min(o) for w,o in v.items()]) for k,v in map.items() if len(v) > 1])
    return (m, e)

def get_move(dir):
    if dir == 'R':
        return lambda pos,value: (pos[0]+value, pos[1])
    elif dir == 'L':
        return lambda pos,value: (pos[0]-value, pos[1])
    elif dir == 'U':
        return lambda pos,value: (pos[0], pos[1]+value)
    elif dir == 'D':
        return lambda pos,value: (pos[0], pos[1]-value)

def fill_map(map, wire, name):
    current = (0, 0)
    steps = 1
    for move in wire.split(','):
        amove = get_move(move[0].upper())
        for m in range(int(move[1:])):
            current = amove(current, 1)
            map[current] = map.get(current, {name: list()})
            map[current][name] = map[current].get(name, list())
            map[current][name].append(steps)
            steps += 1

def compute(wire1, wire2):
    map = {}
    fill_map(map, wire1, '1')
    fill_map(map, wire2, '2')
    return compute_distance(map)


def sample1():
    wire1 = 'R8,U5,L5,D3'
    wire2 = 'U7,R6,D4,L4'
    assert compute(wire1, wire2) == (6, 30)

def sample2():
    wire1 = 'r75,d30,r83,u83,l12,d49,r71,u7,l72'
    wire2 = 'u62,r66,u55,r34,d71,r55,d58,r83'
    assert compute(wire1, wire2) == (159, 610)

def sample3():
    wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    assert compute(wire1, wire2) == (135, 410)

def problem():
    with open('./input', 'r') as strem:
        wire1 = next(strem)
        wire2 = next(strem)
        assert compute(wire1, wire2) == (293, 27306)

sample1()
sample2()
sample3()
problem()
