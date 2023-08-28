import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Se definen los parámetros

T = 310.15 #K
K = 1.0355*10e-22*6.02214*10e20 #L*mmHg/K*mmol
Cv = 23.21 #mmol/L
Pas = 25 #mm Hg
Ci = 160/(K*T) #mmol/L


r_list = []
ca_list = []

# Se calculan los Cas para cada r
for r in np.linspace(0.25, 2):
    func = lambda Ca : ((K*T)/r) *(Ca - r*Ci + Cv) - Pas*(Ca/(Ci - Ca))**(1/3)
    Ca_inicial = 0
    solucion = fsolve(func, Ca_inicial)
    #solucion = calcular_ca(Ca_inicial, r)
    r_list.append(r)
    ca_list.append(solucion)

#Se plotea la figura
plt.figure()
plt.plot(r_list, ca_list)
plt.xlabel("Radio ventilación-perfusión (r)")
plt.ylabel("Concentración arterial (Ca) (mmol/L)")
plt.grid()
plt.show()

