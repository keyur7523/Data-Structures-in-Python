from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 8
d['Ram'] = 6

for key in d:
    print(key, d[key])