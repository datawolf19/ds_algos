from collections import Counter

c1 = Counter('anysequence')

c2 = Counter({'a':1, 'c':1, 'e':3})

c3 = Counter(a=1, c=1, e=33)

print(c1)


ct = Counter()

ct.update('abca')

print(ct)

ct.update({'a':3})

print(ct)

for item in ct:
    print(f'{item} : {ct[item]}')


ct.update({'a':-3, 'b':-2, 'd':3, 'e':2}) # performs an update

print(sorted(ct.elements())) # returns a sorted list from the iterator