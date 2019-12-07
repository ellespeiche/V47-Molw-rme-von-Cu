import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
Q,cv= np.loadtxt('tab4.txt', unpack=True,delimiter=',')

def f(cv,a,b):
    return a*cv+b
Werte, Fehler = curve_fit(f, cv, Q)
print(Werte)
print(np.sqrt(np.diag(Fehler)))

x_new = np.linspace(13.8, 22, 500)



plt.figure(1)
plt.plot(cv,Q,'x', label='Werte aus der Tabelle')
plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
plt.xlabel(r'$c_v $/$\frac{J}{mol K}$')
plt.ylabel(r'$Q$')
plt.grid()
plt.legend()




plt.savefig('Q.pdf')
print ('Fertig')
