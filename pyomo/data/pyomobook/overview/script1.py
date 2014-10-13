import pyomo.environ
from pyomo.opt import SolverFactory
from concrete1 import model

model.pprint()

instance = model.create()
instance.pprint()

opt = SolverFactory("glpk")
results = opt.solve(instance)

results.write()