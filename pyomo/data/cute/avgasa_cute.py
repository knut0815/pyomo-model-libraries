#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________

# Formulated in Pyomo by Juan Lopez and Gabe Hackebeil
# Taken from:
# AMPL Model by Hande Y. Benson
#
# Copyright (C) 2001 Princeton University
# All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that the copyright notice and this
# permission notice appear in all supporting documentation.                     

#   classification QLR2-AN-8-10

from pyomo.core import * 
model = AbstractModel()

model.a = Param(RangeSet(1,8))
model.b = Param(RangeSet(1,7))
model.c = Param(RangeSet(2,8))

model.x = Var(RangeSet(1,8),bounds=(0.0,1.0),within=Integers,initialize=1)

# For Pyomo testing,
# generate the ConcreteModel version
# by loading the data
import os
if os.path.isfile(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat')):
    model = model.create(os.path.abspath(__file__).replace('.pyc','.dat').replace('.py','.dat'),preprocess=False)

def f_rule(model):
	return (sum(model.a[j]*model.x[j]**2 for j in xrange(1,9)))+\
	(sum(model.b[j]*model.x[j]*model.x[j+1] for j in xrange(1,8)))+\
	(sum(model.c[j]*model.x[j] for j in xrange(2,9)))
model.f = Objective(rule=f_rule)

def con1(model,j):
	return model.x[2*j-1]+model.x[2*j]<=1.0
model.con1 = Constraint(RangeSet(1,4),rule=con1)

def con5(model,j):
	return sum(model.x[2*i-j] for i in xrange(1,5))<=2.0
model.con5 = Constraint(RangeSet(0,1),rule=con5)

def con7(model):
	return 2.0*model.x[1] + model.x[3] - model.x[7] >= 0
model.con7 = Constraint(rule=con7)

def con8(model):
	return 5.0*model.x[1] + 3.0*model.x[3] - 3.0*model.x[5] - model.x[7] >= 0
model.con8 = Constraint(rule=con8)

def con9(model):
	return model.x[2] - model.x[4] - 3.0*model.x[6] - 5.0*model.x[8] >= 0
model.con9 = Constraint(rule=con9)

def con10(model):
	return model.x[2] - 3.0*model.x[6] - 2.0*model.x[8] >= 0
model.con10 = Constraint(rule=con10)


