from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

k = defaultdict(set)
k['a'].add(1)
k['a'].add(2)
k['b'].add(4)

print(k)