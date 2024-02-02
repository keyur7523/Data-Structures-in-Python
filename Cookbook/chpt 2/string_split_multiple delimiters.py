string = "asdf_ fghy;,thgf, fgyh, ajkl,    foo"
import re
#fields = re.split(r'[;,\s]\s*', string)

fields = re.split(r'(?:_|;|,|\s)\s*', string)
print(fields) 

values = fields[::2]
delimiters = fields[1::2] + ['']

print(values)
print(delimiters)

print(''.join(v+d for v,d in zip(values,delimiters)))