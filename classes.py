class Myclass:
    variable='blah'

    def function(self):
        print('message inside class')

myobjectx=Myclass()
myobjecty=Myclass()

print(myobjectx.variable)
myobjecty.variable='blahblah'
print(myobjecty.variable)

myobjectx.function()

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

print('------------------')

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle()
car2=Vehicle()
car1.name="Fer"
car1.color="red convertible"
car2.name="Jump"
car2.kind="van"
car2.color="blue"
car1.value=60000.00
car2.value=10000.00
# test code
print(car1.description())
print(car2.description())
print(car2.color)