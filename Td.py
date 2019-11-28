import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
TK,cv,Q=np.loadtxt('tab3.txt', unpack=True,delimiter=',')

Td=Q*TK
print(Td)

m=np.mean(Td)
f=np.std(Td, ddof=1)/np.sqrt(len(Td))

print(m,f)