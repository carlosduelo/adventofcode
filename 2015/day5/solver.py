def hasvocals(word, nvocals=3):
    vocals = 'aeiou'
    n = 0
    for c in word:
        if c in vocals:
            n += 1
    return n >= nvocals

def double(word):
    i = 0
    max = len(word)
    while i < max - 1:
        if word[i] == word[i+1]:
            return True
        i += 1
    return False

def is_valid(word):
    for c in ['ab', 'cd', 'pq', 'xy']:
        if c in word:
            return False
    return True

def double_twice(word):
    i = 0
    max = len(word)
    while i < max - 2:
        if word[i:i+2] in word[i+2:]:
            return True
        i += 1

def letter_repeats(word):
    i = 0
    max = len(word)
    while i < max - 2:
        if word[i] == word[i+2]:
            return True
        i += 1

with open('./data', 'r') as lines:
    count = 0
    for word in lines:
        if hasvocals(word, 3) and double(word) and is_valid(word):
            count += 1
    assert count == 258

with open('./data', 'r') as lines:
    count = 0
    for word in lines:
        if double_twice(word) and letter_repeats(word):
            count += 1
    assert count == 53
