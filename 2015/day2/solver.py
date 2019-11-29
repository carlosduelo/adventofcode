import sys

def compute(l, w, h):
    extra = min([l*w, w*h, h*l])
    return 2*l*w + 2*w*h + 2*h*l + extra


t = 0
with open('./data', 'r') as _in:
    for box in _in:
        t += compute(*[int(x) for x in box.split('x')])
assert t == 1588178
