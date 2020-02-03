import numpy as np
from fractions import Fraction
def display(vector, decimal):
   return np.round((vector).astype(np.float), decimals=decimal)
x = Fraction(1,3)
Mat = np.matrix([[0,0,1],
        [Fraction(1,2),0,0],
        [Fraction(1,2),1,0]])
Ex = np.zeros((3,3))
Ex[:] = x
beta = 0.7
Al = beta * Mat + ((1-beta) * Ex)
r = np.matrix([x,x,x])
r = np.transpose(r)
previous = r
for i in range(1,100):
   r = Al * r
   print (display(r,3))
   if (previous==r).all():
      break
   previous = r
print ("Final:\n", display(r,3))
print ("sum", np.sum(r))