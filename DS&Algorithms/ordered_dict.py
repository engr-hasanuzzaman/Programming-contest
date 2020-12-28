from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print("After initial insert dict is")
for key, val in od.items():
    print((key, val))

# after updating the insertion order has been maintained
od['a'] = 5
print("After update dict is {}".format(od))

# after deleting existing key and re-assign that will follow new insertion order
od.pop('b')
od['b'] = 'new entry'
for key, val in od.items():
    print((key, val))
