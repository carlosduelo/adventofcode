def check1(start, end):
    password = start
    while password <= end:
        p = str(password)
        good = False
        for idx in range(len(p)-1):
            if p[idx] > p[idx+1]:
                good = False
                break
            if p[idx] == p[idx+1]:
                good = True
        if good:
            yield p
        password += 1

def check2(start, end):
    for password in check1(start, end):
        l = []
        for c in password:
            if not l:
                l = [(c, 1)]
            elif c == l[-1][0]:
                l[-1] = (c, l[-1][1] + 1)
            else:
                l.append((c, 1))
        good = False
        for a in l:
            if a[1] == 2:
                if good:
                    break
                good = True

        if good:
            yield password

def compute(start, end):
    return sum(1 for i in check1(start, end))

def compute2(start, end):
    return sum(1 for i in check2(start, end))

assert compute(146810, 612564) == 1748
assert compute2(146810, 612564) == 1180
