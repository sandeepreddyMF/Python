def my_function():
    print('hello from my function')
my_function()

print('------------------')

def my_function_withargs(user,greeting):
    print('Hello %s, Wish you %s' % (user,greeting))

my_function_withargs('jake','Happy Birthday')

print('------------------')

def sum(a,b):
    return a+b
c=sum(2,3)
print(c)

print('------------------')

def list_benefits():
    return ["More organized code","More readable code","Easier code reuse", "Allow programmers to share and connect code together"]
benefits=list_benefits()
print(benefits)

print('------------------')


def build_sentance(info):
    infox=info+' is a benefit of functions!'
    return infox
x=build_sentance("quantum computing")
print(x)

print('------------------')

def name_benefits():
    list_of_benefits=list_benefits()
    for benefits in list_of_benefits:
        print(build_sentance(benefits))

name_benefits()

print('------------------')

