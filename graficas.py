# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:17:03 2018

@author: adrian
"""

from tkinter import Button, TOP, BOTH, BOTTOM, LEFT, RIGHT, CENTER, filedialog

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

from modelo import resolverModeloHodgkinHuxley

import pylab as plt
import scipy as sp

class GUIgraficas:
    
    def __init__(self, master, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, tipoCorriente):
        
        self.master = master
        self.master.title("Gráficas")
        self.cI = cI
        self.aux1 = aux1
        self.aux2 = aux2
        self.tF = tF
        self.tI = tI
        self.tipoCorriente = tipoCorriente
        self.V, self.m, self.h, self.n, self.t = resolverModeloHodgkinHuxley(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, tipoCorriente)

        self.fig = plt.figure(num=None, figsize=(12, 6), dpi=90, facecolor='w', edgecolor='k')
        
        plt.subplot(3,1,1)
        plt.title('Dinámica modelo Hodgkin-Huxley')
        plt.plot(self.t, self.V, 'k')
        plt.ylabel('V (mV)')
        
        plt.subplot(3,1,2)
        plt.plot(self.t, self.m, 'r', label='m')
        plt.plot(self.t, self.h, 'g', label='h')
        plt.plot(self.t, self.n, 'b', label='n')
        plt.ylabel('Valor de activación')
        plt.legend()
        
        t = sp.arange(tI, tF, 0.1)
        plt.subplot(3,1,3)
        plt.plot(t, self.I_entrada(t), 'k')
        plt.xlabel('t (ms)')
        plt.ylabel('$I_{in}$ ($\\mu{A}/cm^2$)')
        plt.ylim(-1, 31)       
        
        plt.close()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)     
        
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        buttonCerrar = Button(master=master, width=32, text="Cerrar", command=self.cerrar)
        buttonCerrar.pack(side=RIGHT)
        
        buttonImprimirDatos = Button(master=master, width=32, text="Guardar datos", command=self.guardarDatos)
        buttonImprimirDatos.pack(side=LEFT, anchor=CENTER)
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)        
        
    def cerrar(self):
        self.master.quit()     # stops mainloop
        self.master.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
    def on_closing(self):
        self.master.quit()     
        self.master.destroy()
        
    def guardarDatos(self):
        self.master.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv file","*.csv"),("all files","*.*")))
        direccion = self.master.filename + '.csv'
        f= open(direccion,'w+')
        f.write( 't, V, m, h, n\n' )
        for i in range(self.t.size):
            string = str(self.t[i])+','+str(self.V[i])+','+str(self.m[i])+','+str(self.h[i])+','+str(self.n[i])+'\n'
            f.write( string )
        f.close()
        
    def I_entrada(self, t):
        if(self.tipoCorriente == 1): #discreto
            expresion = self.cI*(t>self.aux1)- self.cI*(t>self.aux2)
        else:
            if(self.tipoCorriente == 2): #continuo
                expresion = self.cI*(t>0)
            else: # aumento        
                expresion = self.cI*(t>0)
                if(self.aux1>0 and self.aux2>0):
                    contador = 0
                    while(contador<=self.tF):
                        contador += self.aux2
                        expresion += self.aux1*(t>contador)
                        
        return expresion