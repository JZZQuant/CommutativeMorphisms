import re
import numpy as np

def closure(expression,pos):
    expression=expression[pos:]
    ones=[int(char=='(') for char in expression]
    minus=[int(char==')') for char in expression]
    basearray=np.subtract(ones,minus)
    return np.where(np.cumsum(basearray)==0)[0][0] + 1 +pos

def Negation(a):
    return 1-a

def And(a,b):
    return a*b

def Or(a,b):
    return 1-((2**(a+b))%2)

def duality(expression):
    operands=len(set(re.findall("[a-zA-Z]+", expression)))

    point_topology=list(set(re.findall("[a-zA-Z]+", expression)))
    topology = range(1,2**(operands)+1)
    dualspace=[]

    for i in range(0,operands):
        dualspace.append(np.array([x%2 for x in topology]))
        topology=[x/2 for x in topology]

    duality=dict(zip(point_topology,dualspace))
    duality["0"]=np.array([0]*(2**(operands)))
    duality["1"]=1-duality["0"]
    return duality
