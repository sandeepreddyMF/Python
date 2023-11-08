phonebook= {}
phonebook["john"] = 123456
phonebook["jake"] = 567890
phonebook["jill"] = 246801
print(phonebook)

print('------------------')

phonebook1 = {
    "sandeep" : 534015,
    "sriman"  : 511835,
    "naresh"  : 534018
}
print(phonebook1)

print('------------------')

for name,number in phonebook1.items():
    print("Emp number of %s is %d" % (name,number))

print(phonebook)
del phonebook["jill"]
print(phonebook)
phonebook["jill"] = 246801
print(phonebook)