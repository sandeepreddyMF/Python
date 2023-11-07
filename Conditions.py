x = 2
print(x == 2)
print(x == 3)
print(x < 3)
print(x != 3)

name='john'
list=['jake','john','jill']
age=23
if name=='john' and age==23:
    print ('and works')
if name=='john' or name=='jake':
    print ('or works')
if name in list:
    print ('in list works')
if x==2:
    print('x equals two!')
else:
    print('x does not equal two!')
if x>2:
    print('not greater')
elif x < 2:
    print('not less than')
else:
    print('x is 2')

x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)

print(not False)
print((not False) is True)