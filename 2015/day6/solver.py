def apply_to_range(grid, action, start, end):
    s_x, s_y = [int(c) for c in start.split(',')]
    e_x, e_y = [int(c) for c in end.split(',')]
    for x in range(s_x, e_x+1):
        for y in range(s_y, e_y+1):
            grid[x][y] = action(grid[x][y])

def apply_op(op, grid):
    operation = op.split()
    if len(operation) == 4:
        apply_to_range(grid, lambda x: not x, operation[1], operation[-1])
    elif operation[1] == 'on':
        apply_to_range(grid, lambda x: True, operation[2], operation[-1])
    elif operation[1] == 'off':
        apply_to_range(grid, lambda x: False, operation[2], operation[-1])
    else:
        print('caca')


def compute(w, h):
    grid = [[False]*w for i in range(h)]
    with open('./data', 'r') as stream:
        for op in stream:
            apply_op(op, grid)
    count = 0
    for x in range(w):
        for y in range(h):
            count += 1 if grid[x][y] else 0
    return count

assert compute(1000, 1000) == 400410

def apply_op_2(op, grid):
    operation = op.split()
    if len(operation) == 4:
        apply_to_range(grid, lambda x: x+2, operation[1], operation[-1])
    elif operation[1] == 'on':
        apply_to_range(grid, lambda x: x+1, operation[2], operation[-1])
    elif operation[1] == 'off':
        apply_to_range(grid, lambda x: 0 if x == 0 else x-1, operation[2], operation[-1])
    else:
        print('caca')

def compute_2(w, h):
    grid = [[0]*w for i in range(h)]
    with open('./data', 'r') as stream:
        for op in stream:
            apply_op_2(op, grid)
    count = 0
    for x in range(w):
        for y in range(h):
            count += grid[x][y]
    return count

assert compute_2(1000, 1000) == 15343601
