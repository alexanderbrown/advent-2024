import re
with open('data\\day3_input.txt', 'r') as f:
    data = f.read()

pattern_mul = r'mul\((?P<one>[0-9]{1,4})\,(?P<two>[0-9]{1,4})\)'

S = 0
for match in re.finditer(pattern_mul, data):
    one = int(match.group('one'))
    two = int(match.group('two'))
    S += one * two

print(S)

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

do_index = [do.end() for do in re.finditer(pattern_do, data)]
dont_index = [dont.end() for dont in re.finditer(pattern_dont, data)]


enabled = []
for idx in range(len(data)):
    if idx in do_index:
        enabled.append(True)
    elif idx in dont_index:
        enabled.append(False)
    elif idx == 0:
        enabled.append(True)
    else:
        enabled.append(enabled[-1])
        
S = 0
for match in re.finditer(pattern_mul, data):
    idx = match.start()
    one = int(match.group('one'))
    two = int(match.group('two'))

    if enabled[idx]:
        S += one * two

print(S)
