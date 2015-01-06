from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set()
model.B = Param(model.A)
# @:decl

instance = model.create('param4.dat')

print('B')
keys = instance.B.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.B[key])))
