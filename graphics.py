# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:17:03 2018

@author: adrian
"""

from tkinter import Button, TOP, BOTH, LEFT, RIGHT, CENTER, filedialog

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

from model import resolveHodgkinHuxleyModel

import pylab as plt
import scipy as sp

class guiGraphics:
    
    def __init__(self, master, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, currentType):
        
        self.master = master
        self.master.title("Graphics")
        self.cI = cI
        self.aux1 = aux1
        self.aux2 = aux2
        self.tF = tF
        self.tI = tI
        self.currentType = currentType
        self.V, self.m, self.h, self.n, self.t = resolveHodgkinHuxleyModel(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, currentType)

        self.fig = plt.figure(num=None, figsize=(12, 6), dpi=90, facecolor='w', edgecolor='k')
        
        plt.subplot(3,1,1)
        plt.title('Dynamics Hodgkin-Huxley model')
        plt.plot(self.t, self.V, 'k')
        plt.ylabel('V (mV)')
        
        plt.subplot(3,1,2)
        plt.plot(self.t, self.m, 'r', label='m')
        plt.plot(self.t, self.h, 'g', label='h')
        plt.plot(self.t, self.n, 'b', label='n')
        plt.ylabel('Activation value')
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
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)     
        
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        buttonClose = Button(master=master, width=32, text="Close", command=self.close)
        buttonClose.pack(side=RIGHT)
        
        buttonPrintData = Button(master=master, width=32, text="Save data", command=self.guardarDatos)
        buttonPrintData.pack(side=LEFT, anchor=CENTER)
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)        
        
    def close(self):
        self.master.quit()     # stops mainloop
        self.master.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
    def on_closing(self):
        self.master.quit()     
        self.master.destroy()
        
    def guardarDatos(self):
        self.master.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv file","*.csv"),("all files","*.*")))
        direction = self.master.filename + '.csv'
        f= open(direction,'w+')
        f.write( 't, V, m, h, n\n' )
        for i in range(self.t.size):
            string = str(self.t[i])+','+str(self.V[i])+','+str(self.m[i])+','+str(self.h[i])+','+str(self.n[i])+'\n'
            f.write( string )
        f.close()
        
    def I_entrada(self, t):
        if(self.currentType == 1): #discrete
            expression = self.cI*(t>self.aux1)- self.cI*(t>self.aux2)
        else:
            if(self.currentType == 2): #continuous
                expression = self.cI*(t>0)
            else: # increase        
                expression = self.cI*(t>0)
                if(self.aux1>0 and self.aux2>0):
                    counter = 0
                    while(counter<=self.tF):
                        counter += self.aux2
                        expression += self.aux1*(t>counter)
                        
        return expression