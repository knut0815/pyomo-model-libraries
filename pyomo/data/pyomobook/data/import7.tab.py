from pyomo.core import *

model = AbstractModel()

model.I = Set(initialize=['I1', 'I2', 'I3', 'I4'])
model.A = Set(initialize=['A1', 'A2', 'A3'])
model.U = Param(model.I,model.A)
# BUG:  This should cause an error
#model.U = Param(model.A,model.I)

instance = model.create('import7.tab.dat')

print('I '+str(sorted(list(instance.I.data()))))
print('A '+str(sorted(list(instance.A.data()))))
print('U')
for key in sorted(instance.U.keys()):
    print(cname(instance.U,key)+" "+str(value(instance.U[key])))
