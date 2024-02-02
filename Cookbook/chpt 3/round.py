#print(round(1.2363, 2))

x = 1.28756
#print('value is {:0.2f}'.format(x))

a = 2.1
b = 4.2
#print(a + b)
#print(round(a + b, 2))

from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.1')

c = Decimal('1.3')
d = Decimal('1.7')

with localcontext() as ctx:
    ctx.prec = 4
#    print(c/d)

#print(a + b)

x = 123434234.56789

print(format(x, '0,.2f')) # a comma for thousands
print(format(x, '<10.1f'), 'aa') # left centered
print(format(x, '^10.1f'), 'aa') # centered
print(format(x, '>10.1f'), 'aa') # right centered

print(format(x, 'e'))
print(format(x, '0.2e'))



