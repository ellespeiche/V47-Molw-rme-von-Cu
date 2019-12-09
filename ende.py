import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
T, Td = np.loadtxt('tab5.txt', unpack=True,delimiter=',')
#
#def f(x,a,b):
#    return a*x+b
#Werte, Fehler = curve_fit(f, x, y)
#print(Werte)
#print(np.sqrt(np.diag(Fehler)))
#
#x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(T,Td,'x', label='Messergebnisse')
#plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
plt.xlabel('$T$/K')
plt.ylabel(r'$\Theta_{D}$/K')
plt.grid()
plt.legend()




plt.savefig('ende.pdf')
print ('Fertig')