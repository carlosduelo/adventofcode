def compute(noun, verb):
    intprogram = []
    with open('./data', 'r') as program:
        for pline in program:
            intprogram.extend([int(op) for op in pline.strip().split(',')])
    intprogram[1] = noun
    intprogram[2] = verb

    idx = 0
    while intprogram[idx] != 99:
        if intprogram[idx] > 99:
            raise ValueError('unknown opcode')
        if intprogram[idx] == 1:
            intprogram[intprogram[idx+3]] = intprogram[intprogram[idx+1]] + intprogram[intprogram[idx+2]]
        elif intprogram[idx] == 2:
            intprogram[intprogram[idx+3]] = intprogram[intprogram[idx+1]] * intprogram[intprogram[idx+2]]
        else:
            raise ValueError('opcode not register')
        idx += 4
    return intprogram[0]

assert compute(12, 2) == 3716293

search = 19690720
for noun in range(100):
    for verb in range(100):
        if compute(noun, verb) == search:
            assert 100*noun+verb == 6429
