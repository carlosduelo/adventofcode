import re
def compute_len(word):
    word = word.strip('"')
    word = word.replace('\\"', '"')
    word = word.replace("\\'", "'")
    word = word.replace("\\\\", "\\")
    word = re.sub(r"\\x[0-9A-Fa-f][0-9A-Fa-f]", "u", word)
    l = len(word)
    return len(word)

def read(path):
    count_characters = 0
    count_str_characters = 0
    with open(path, 'r') as stream:
        for line in stream:
            count_str_characters += len(line.strip())
            count_characters += compute_len(line.strip())
    return count_str_characters - count_characters

def compute_len2(word):
    l = 2
    for c in word:
        if c == '"':
            l += 2
        elif c == "'":
            l += 2
        elif c == "\\":
            l += 2
        else:
            l += 1
    return l

def read2(path):
    count_characters = 0
    count_str_characters = 0
    with open(path, 'r') as stream:
        for line in stream:
            count_str_characters += compute_len2(line.strip())
            count_characters += len(line.strip())
    return count_str_characters - count_characters

assert read('./input') == 1333
assert read2('./input') == 2046
