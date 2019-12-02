fuel = 0
with open('./data', 'r') as lines:
    for mass  in lines:
        fuel += (int(mass) // 3) - 2
assert fuel == 3402609

def compute(mass):
    fuel = (int(mass) // 3) - 2
    if fuel <= 0:
        return 0
    return compute(fuel) + fuel

fuel = 0
with open('./data', 'r') as lines:
    for mass  in lines:
        fuel += compute(int(mass))
assert fuel == 5101025
