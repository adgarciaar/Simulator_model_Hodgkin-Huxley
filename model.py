# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:16:10 2018

@author: adgarciaar
"""

import scipy as sp
from scipy.integrate import odeint

def resolveHodgkinHuxleyModel(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, currentType):

    # Channel gating kinetics
    # Functions of membrane voltage
    def alpha_m(V): 
        return 0.1*(V+40.0)/(1.0 - sp.exp(-(V+40.0) / 10.0))
    def beta_m(V):  
        return 4.0*sp.exp(-(V+65.0) / 18.0)
    def alpha_h(V): 
        return 0.07*sp.exp(-(V+65.0) / 20.0)
    def beta_h(V):  
        return 1.0/(1.0 + sp.exp(-(V+35.0) / 10.0))
    def alpha_n(V): 
        return 0.01*(V+55.0)/(1.0 - sp.exp(-(V+55.0) / 10.0))
    def beta_n(V):  
        return 0.125*sp.exp(-(V+65) / 80.0)
    
    # Membrane currents (in uA/cm^2)
    #  Sodium (Na = element name)
    def I_Na(V,m,h):
        return g_Na * m**3 * h * (V - E_Na)
    #  Potassium (K = element name)
    def I_K(V, n):  
        return g_K  * n**4 * (V - E_K)
    #  Leak
    def I_L(V):
        return g_L * (V - E_L)
    
    # External current
    def I_external(t):        
        if(currentType == 1): #discreto
            expression = cI*(t>aux1)- cI*(t>aux2)
        else:
            if(currentType == 2): #continuo
                expression = cI*(t>0)
            else: # aumento        
                expression = cI*(t>0)
                if(aux1>0 and aux2>0):
                    counter = 0
                    while(counter<=tF):
                        counter += aux2
                        expression += aux1*(t>counter)
                        
        return expression
    
    def generalEquations(X, t):
        V, m, h, n = X
        
        #calculate membrane potential & activation variables
        dVdt = (I_external(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V)) / C_m
        dmdt = alpha_m(V)*(1.0-m) - beta_m(V)*m
        dhdt = alpha_h(V)*(1.0-h) - beta_h(V)*h
        dndt = alpha_n(V)*(1.0-n) - beta_n(V)*n
        return dVdt, dmdt, dhdt, dndt
    
    t = sp.arange(tI, tF, 0.1) # The time to integrate over
    X = odeint(generalEquations, [-65, 0.05, 0.6, 0.32], t)    
    V = X[:,0]
    m = X[:,1]
    h = X[:,2]
    n = X[:,3]
    
    return V,m,h,n,t
