from scipy.integrate import quad 
import numpy as np

import math

from scipy.optimize import brentq

fermi_dirac_func = 1

def fermi_dirac_func(E,u):

    f = 1/((math.exp(E-u)*40)+1)
    
    return(f) 

def fermi_dirac_integration(u):

    integration = quad(fermi_dirac_func,0,2,u)

    return(integration)

def equation(u):

    f = fermi_dirac_integration(u)[0]-1

    return(f)

roots = brentq(equation, 0,100)
print(roots)




    





