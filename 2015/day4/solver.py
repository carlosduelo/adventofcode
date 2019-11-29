import hashlib

def compute(prefix, zeros):
    i = 0
    while True:
        hash = hashlib.md5(f'{prefix}{i}'.encode('utf-8')).hexdigest()
        if hash.startswith('0'*zeros):
            return i
        i+=1
assert compute('abcdef', 5) == 609043
assert compute('pqrstuv', 5) == 1048970
assert compute('iwrupvqb', 5) == 346386
assert compute('iwrupvqb', 6) == 9958218
