# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:53:04 2018

@author: adgarciaar
"""

from tkinter import Tk, Label, Button, Entry, messagebox, Radiobutton, IntVar
from graphics import guiGraphics
import subprocess

class GUI:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Simulator Hodgkin-Huxley model")

        self.main_label = Label(master, text="Simulator Hodgkin-Huxley model")
        
        self.label_parameters = Label(master, text="Parameters")
        
        self.label_empty1 = Label(master, text="")
        self.label_empty2 = Label(master, width=5, text="")
        self.label_empty3 = Label(master, text="")
        self.label_empty4 = Label(master, width=15, text="")
        self.label_empty5 = Label(master, width=5, text="")
        self.label_empty6 = Label(master, text="")
        self.label_empty7 = Label(master, text="")
        self.label_empty8 = Label(master, text="")
        
        self.label_capacitance = Label(master, text="Membrane capacitance (uF/cm^2)")
        self.label_NaConductance = Label(master, text="gNa conductance (mS/cm^2)")
        self.label_KConductance = Label(master, text="gK conductance (mS/cm^2)")
        self.label_LConductance = Label(master, text="gL conductance (mS/cm^2)")
        self.label_NaPotential = Label(master, text="ENa potential (mV)")
        self.label_KPotential = Label(master, text="EK potential (mV)")
        self.label_LPotential = Label(master, text="EL potential (mV)")
      
        self.txt_capacitance = Entry(master,width=6)
        self.txt_NaConductance = Entry(master,width=6)
        self.txt_KConductance  = Entry(master,width=6)
        self.txt_LConductance = Entry(master,width=6)
        self.txt_NaPotential = Entry(master,width=6)
        self.txt_KPotential = Entry(master,width=6)
        self.txt_LPotential = Entry(master,width=6)
        
        self.label_settings = Label(master, text="Settings")
        
        self.label_startTime = Label(master, text="Start time (ms)")
        self.label_endTime = Label(master, text="End time (ms)")
        self.label_inCurrent = Label(master, text="In current (uA/cm^2)")
        self.label_aux1 = Label(master, text="Start time stimulus (ms)")
        self.label_aux2 = Label(master, text="End time stimulus (ms)")
        self.label_currentType = Label(master, text="Stimulus current")

        self.txt_startTime = Entry(master,width=6)
        self.txt_endTime = Entry(master,width=6)
        self.txt_inCurrent = Entry(master,width=6)
        self.txt_aux1 = Entry(master,width=6)
        self.txt_aux2 = Entry(master,width=6)
        
        self.button_simulate = Button(master, width=20, text="Simulate", command=self.simular)
        self.button_defaultParameters = Button(master, width=33, text="Set default parameters", command=self.setDefaultParameters)
        self.button_defaultSettings = Button(master, width=33, text="Set test settings", command=self.setDefaultSettings)
        self.button_clean = Button(master, width=6, text="Clean", command=self.clean)
        self.button_helping = Button(master, width=6, text="Help", command=self.helping)
        self.button_close = Button(master, width=6, text="Close", command=self.close)
        
        #Ingresar componentes dentro del grid
        
        self.main_label.grid(row=0, columnspan=7)
        
        self.label_empty1.grid(row=1, columnspan=7)
        self.label_empty2.grid(column=0, rowspan=11)
        self.label_empty3.grid(row=3, columnspan=7)
        self.label_empty4.grid(column=3, rowspan=11)
        self.label_empty5.grid(column=6, rowspan=11)
        self.label_empty6.grid(row=13, columnspan=7)
        self.label_empty7.grid(row=14, columnspan=4)
        self.label_empty8.grid(row=12, columnspan=7)
        
        self.label_parameters.grid(row=2, column=1, columnspan=2)
        
        self.label_capacitance.grid(row=4, column=1)
        self.label_NaConductance.grid(row=5, column=1)
        self.label_KConductance.grid(row=6, column=1)
        self.label_LConductance.grid(row=7, column=1)
        self.label_NaPotential.grid(row=8, column=1)
        self.label_KPotential.grid(row=9, column=1)
        self.label_LPotential.grid(row=10, column=1)
        
        self.txt_capacitance.grid(column=2, row=4)
        self.txt_NaConductance.grid(column=2, row=5)
        self.txt_KConductance.grid(column=2, row=6)
        self.txt_LConductance.grid(column=2, row=7)
        self.txt_NaPotential.grid(column=2, row=8)
        self.txt_KPotential.grid(column=2, row=9)
        self.txt_LPotential.grid(column=2, row=10)
        
        self.label_settings.grid(row=2, column=4, columnspan=2)
        
        self.label_startTime.grid(row=4, column=4)
        self.label_endTime.grid(row=5, column=4)
        self.label_inCurrent.grid(row=6, column=4)
        self.label_aux1.grid(row=10, column=4)
        self.label_aux2.grid(row=11, column=4)
        self.label_currentType.grid(row=8, column=4)
       
        self.txt_startTime.grid(row=4, column=5)
        self.txt_endTime.grid(row=5, column=5)
        self.txt_inCurrent.grid(row=6, column=5)
        self.txt_aux1.grid(row=10, column=5)
        self.txt_aux2.grid(row=11, column=5)
        
        self.button_simulate.grid(row=15, column=1)
        self.button_clean.grid(row=15, column=3)
        self.button_helping.grid(row=15, column=4)
        self.button_close.grid(row=15, column=5)
        self.button_defaultParameters.grid(row=13, column=1, columnspan=2) 
        self.button_defaultSettings.grid(row=13, column=4, columnspan=2)
        
        self.windowGraphics = None
        self.guiGraphics = None
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.var = IntVar()
        
        self.radioBDiscrete = Radiobutton(master, text="Discrete", variable=self.var, value=1, command=self.selectDiscrete)
        self.radioBContinuous = Radiobutton(master, text="Continuous", variable=self.var, value=2, command=self.selectContinuous)
        self.radioBIncrement = Radiobutton(master, text="Increase", variable=self.var, value=3, command=self.selectIncrement)
        self.radioBDiscrete.select()
        self.radioBContinuous.deselect()
        self.radioBIncrement.deselect()
        self.radioBDiscrete.grid(row=7, column=5)
        self.radioBContinuous.grid(row=8, column=5)
        self.radioBIncrement.grid(row=9, column=5)       
        

    def simular(self): 
        
        validation1 = True
        validation1 = validation1 and self.txt_capacitance.get() != ""
        validation1 = validation1 and self.txt_NaConductance.get() != ""
        validation1 = validation1 and self.txt_KConductance.get() != ""
        validation1 = validation1 and self.txt_LConductance.get() != ""
        validation1 = validation1 and self.txt_NaPotential.get() != ""
        validation1 = validation1 and self.txt_KPotential.get() != ""
        validation1 = validation1 and self.txt_LPotential.get() != ""
        validation1 = validation1 and self.txt_startTime.get() != ""
        validation1 = validation1 and self.txt_endTime.get() != ""
        validation1 = validation1 and self.txt_inCurrent.get() != ""
         
        if( self.var.get() == 1 or self.var.get() == 3 ):        
            validation1 = validation1 and self.txt_aux1.get() != ""  
            validation1 = validation1 and self.txt_aux2.get() != ""  
        
        if(validation1 == True):
            
            validation2 = True
            validation2 = validation2 and self.isFloat(self.txt_capacitance.get())
            validation2 = validation2 and self.isFloat(self.txt_NaConductance.get())
            validation2 = validation2 and self.isFloat(self.txt_KConductance.get())
            validation2 = validation2 and self.isFloat(self.txt_LConductance.get())
            validation2 = validation2 and self.isFloat(self.txt_NaPotential.get())
            validation2 = validation2 and self.isFloat(self.txt_KPotential.get())
            validation2 = validation2 and self.isFloat(self.txt_LPotential.get())
            validation2 = validation2 and self.isFloat(self.txt_startTime.get())
            validation2 = validation2 and self.isFloat(self.txt_endTime.get())
            validation2 = validation2 and self.isFloat(self.txt_inCurrent.get())
            
            if( self.var.get() == 1 or self.var.get() == 3 ):                    
                validation2 = validation2 and self.isFloat(self.txt_aux1.get())
                validation2 = validation2 and self.isFloat(self.txt_aux2.get())
            
            if(validation2 == True):
                
                if( float(self.txt_startTime.get())<0.0 
                   or float(self.txt_endTime.get())<float(self.txt_startTime.get()) 
                   or float(self.txt_inCurrent.get())<0.0 ):
                    messagebox.showinfo("Error", "There are no valid data")
                else: 
                    validation3 = False
                    if( self.var.get() == 1 ): #discreto
                        if ( float(self.txt_aux1.get())<float(self.txt_startTime.get()) 
                            or float(self.txt_aux2.get())>float(self.txt_endTime.get())
                            or float(self.txt_aux1.get())==float(self.txt_aux2.get()) 
                            or float(self.txt_aux1.get())>float(self.txt_aux2.get()) ):
                            messagebox.showinfo("Error", "There are no valid data")
                        else:
                            validation3 = True
                    if( self.var.get() == 3 ): #aumento
                        if ( float(self.txt_aux1.get())<0.0 
                            or float(self.txt_aux2.get())<0.0
                            or float(self.txt_aux2.get())>=float(self.txt_endTime.get()) ):
                            messagebox.showinfo("Error", "There are no valid data")
                        else:
                            validation3 = True
                    if( self.var.get() == 2 ): #continuo
                        validation3 = True
                    if (validation3 == True):
                        self.plot()
            else:            
                messagebox.showinfo("Error", "There are no valid data")
                
        else:
            messagebox.showinfo("Error", "There are empty fields")
        
    def isFloat(self, n):
        try:
            n1 = float(n)
        except (ValueError, TypeError):
            return False
        else:
            return True
        
    def plot(self):
    		
        C_m = float( self.txt_capacitance.get() )
        g_Na = float( self.txt_NaConductance.get() )
        g_K = float( self.txt_KConductance.get() )
        g_L = float( self.txt_LConductance.get() )
        E_Na = float( self.txt_NaPotential.get() )
        E_K = float( self.txt_KPotential.get() )
        E_L = float( self.txt_LPotential.get() )
        tI = float( self.txt_startTime.get() )
        tF = float( self.txt_endTime.get() )
        cI = float( self.txt_inCurrent.get() )
        
        if( self.var.get() == 1 or self.var.get() == 3 ):       
            aux1 = float( self.txt_aux1.get() )
            aux2 = float( self.txt_aux2.get() )
        else:
            aux1 = -1
            aux2 = -1
        
        if(self.windowGraphics!=None):
            self.windowGraphics.quit()    
            self.windowGraphics.destroy()
            
        self.windowGraphics = Tk()
        self.guiGraphics = guiGraphics(self.windowGraphics,C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, self.var.get())
        self.windowGraphics.mainloop()
        self.windowGraphics = None
        
    def setDefaultParameters(self):
        self.txt_capacitance.delete(0,'end')
        self.txt_capacitance.insert(0,1.0)
        self.txt_NaConductance.delete(0,'end')
        self.txt_NaConductance.insert(0,120.0)
        self.txt_KConductance.delete(0,'end')
        self.txt_KConductance.insert(0,36.0)
        self.txt_LConductance.delete(0,'end')
        self.txt_LConductance.insert(0,0.3)
        self.txt_NaPotential.delete(0,'end')
        self.txt_NaPotential.insert(0,50.0)
        self.txt_KPotential.delete(0,'end')
        self.txt_KPotential.insert(0,-77.0)
        self.txt_LPotential.delete(0,'end')
        self.txt_LPotential.insert(0,-54.387)
        
    def setDefaultSettings(self):        
        self.txt_startTime.delete(0,'end')
        self.txt_startTime.insert(0,0) 
        self.txt_endTime.delete(0,'end')
        self.txt_endTime.insert(0,100.0) 
        self.txt_inCurrent.delete(0,'end')
        self.txt_inCurrent.insert(0,10.0)
        self.txt_aux1.delete(0,'end')        
        self.txt_aux2.delete(0,'end')       
        
        if( self.var.get() == 1 ):
            self.txt_aux1.insert(0,40.0)
            self.txt_aux2.insert(0,50.0)
        else:
            if( self.var.get() == 3 ):
                self.txt_aux1.insert(0,3.0)
                self.txt_aux2.insert(0,20.0)               
        
    def clean(self):        
        self.txt_capacitance.delete(0,'end')
        self.txt_NaConductance.delete(0,'end')
        self.txt_KConductance.delete(0,'end')
        self.txt_LConductance.delete(0,'end')
        self.txt_NaPotential.delete(0,'end')
        self.txt_KPotential.delete(0,'end')
        self.txt_LPotential.delete(0,'end')        
        self.txt_startTime.delete(0,'end')
        self.txt_endTime.delete(0,'end')
        self.txt_inCurrent.delete(0,'end')
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        if(self.windowGraphics!=None):
            self.windowGraphics.quit()    
            self.windowGraphics.destroy()
        
    def helping(self):
        subprocess.Popen("helping.pdf",shell=True)
        
    def close(self):
        self.master.quit()    
        self.master.destroy()  
    
    def on_closing(self):
        self.master.quit()     
        self.master.destroy()
        
    def selectDiscrete(self):
        self.txt_aux1.grid()
        self.txt_aux2.grid()
        self.label_aux1.grid()   
        self.label_aux2.grid()         
        
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.label_aux1.config(text='Start time stimulus (ms)')
        self.label_aux2.config(text='End time stimulus (ms)')
        
    def selectContinuous(self):
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.txt_aux1.grid_remove()
        self.txt_aux2.grid_remove()
        self.label_aux1.grid_remove()    
        self.label_aux2.grid_remove()         
        
    def selectIncrement(self):
        self.txt_aux1.grid()
        self.txt_aux2.grid()
        self.label_aux1.grid()   
        self.label_aux2.grid()  
        
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.label_aux1.config(text='Current increase (uA/cm^2)')
        self.label_aux2.config(text='Every (ms)')

def main():
    root = Tk()
    myGui = GUI(root)
    root.mainloop()    

if __name__ == "__main__":
    main()