biodata = [
    'Keyur', 
    'Pawaskar', 
    'keyur.pawaskar@somaiya.edu', 
    '9870028095', 
    '9870026452', 
    '9969286845'
    ]

fname, lname, email, *contacts = biodata

#print(fname)
#print(lname)
#print(email)
#print(contacts)
#print(*contacts)

records = [
    ('foo', 1, 3),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def d_foo(x, y):
    print('foo', x, y)

def d_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        d_foo(*args)
    if tag == 'bar':
        d_bar(*args)


#  unpacking and ignoring certain values:

record = ['acme', 50, 123.45, (23, 11, 1998)]
name, *_, (*_, year) = record
#print(name)
#print(year) 

# some application for star unpacking

k = [12, 14, 18, 11, 36]

def sum(k):
    head, *tail = k
    return head + sum(tail) if tail else head

#print(sum(k))

