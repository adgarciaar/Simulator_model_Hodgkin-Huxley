# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:53:04 2018

@author: adrian
"""

from tkinter import Tk, Label, Button, Entry, messagebox, Radiobutton, IntVar
from graficas import GUIgraficas
import subprocess

class GUI:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Simulador modelo Hodgkin-Huxley")

        self.main_label = Label(master, text="Simulador modelo Hodgkin-Huxley")
        
        self.label_parametros = Label(master, text="Parámetros")
        
        self.label_vacio1 = Label(master, text="")
        self.label_vacio2 = Label(master, width=5, text="")
        self.label_vacio3 = Label(master, text="")
        self.label_vacio4 = Label(master, width=15, text="")
        self.label_vacio5 = Label(master, width=5, text="")
        self.label_vacio6 = Label(master, text="")
        self.label_vacio7 = Label(master, text="")
        self.label_vacio8 = Label(master, text="")
        
        self.label_capacitancia = Label(master, text="Capacitancia membrana (uF/cm^2)")
        self.label_conductanciaNa = Label(master, text="Conductancia gNa (mS/cm^2)")
        self.label_conductanciaK = Label(master, text="Conductancia gK (mS/cm^2)")
        self.label_conductanciaL = Label(master, text="Conductancia gL (mS/cm^2)")
        self.label_potencialNa = Label(master, text="Potencial ENa (mV)")
        self.label_potencialK = Label(master, text="Potencial EK (mV)")
        self.label_potencialL = Label(master, text="Potencial EL (mV)")
      
        self.txt_capacitancia = Entry(master,width=6)
        self.txt_conductanciaNa = Entry(master,width=6)
        self.txt_conductanciaK  = Entry(master,width=6)
        self.txt_conductanciaL = Entry(master,width=6)
        self.txt_potencialNa = Entry(master,width=6)
        self.txt_potencialK = Entry(master,width=6)
        self.txt_potencialL = Entry(master,width=6)
        
        self.label_ajustes = Label(master, text="Ajustes")
        
        self.label_tiempoInicio = Label(master, text="Tiempo inicio (ms)")
        self.label_tiempoFin = Label(master, text="Tiempo fin (ms)")
        self.label_corrienteEntrada = Label(master, text="Corriente de entrada (uA/cm^2)")
        self.label_aux1 = Label(master, text="Inicio estímulo (ms)")
        self.label_aux2 = Label(master, text="Fin estímulo (ms)")
        self.label_tipoCorriente = Label(master, text="Corriente estímulo")

        self.txt_tiempoInicio = Entry(master,width=6)
        self.txt_tiempoFin = Entry(master,width=6)
        self.txt_corrienteEntrada = Entry(master,width=6)
        self.txt_aux1 = Entry(master,width=6)
        self.txt_aux2 = Entry(master,width=6)
        
        self.simular_button = Button(master, width=20, text="Simular", command=self.simular)
        self.parametrosDefault_button = Button(master, width=33, text="Establecer parámetros predeterminados", command=self.establecerPPredeterminados)
        self.ajustesDefault_button = Button(master, width=33, text="Establecer ajustes de prueba", command=self.establecerAPredeterminados)
        self.limpiar_button = Button(master, width=6, text="Limpiar", command=self.limpiar)
        self.ayuda_button = Button(master, width=6, text="Ayuda", command=self.ayudar)
        self.salir_button = Button(master, width=6, text="Salir", command=self.salir)
        
        #Ingresar componentes dentro del grid
        
        self.main_label.grid(row=0, columnspan=7)
        
        self.label_vacio1.grid(row=1, columnspan=7)
        self.label_vacio2.grid(column=0, rowspan=11)
        self.label_vacio3.grid(row=3, columnspan=7)
        self.label_vacio4.grid(column=3, rowspan=11)
        self.label_vacio5.grid(column=6, rowspan=11)
        self.label_vacio6.grid(row=13, columnspan=7)
        self.label_vacio7.grid(row=14, columnspan=4)
        self.label_vacio8.grid(row=12, columnspan=7)
        
        self.label_parametros.grid(row=2, column=1, columnspan=2)
        
        self.label_capacitancia.grid(row=4, column=1)
        self.label_conductanciaNa.grid(row=5, column=1)
        self.label_conductanciaK.grid(row=6, column=1)
        self.label_conductanciaL.grid(row=7, column=1)
        self.label_potencialNa.grid(row=8, column=1)
        self.label_potencialK.grid(row=9, column=1)
        self.label_potencialL.grid(row=10, column=1)
        
        self.txt_capacitancia.grid(column=2, row=4)
        self.txt_conductanciaNa.grid(column=2, row=5)
        self.txt_conductanciaK.grid(column=2, row=6)
        self.txt_conductanciaL.grid(column=2, row=7)
        self.txt_potencialNa.grid(column=2, row=8)
        self.txt_potencialK.grid(column=2, row=9)
        self.txt_potencialL.grid(column=2, row=10)
        
        self.label_ajustes.grid(row=2, column=4, columnspan=2)
        
        self.label_tiempoInicio.grid(row=4, column=4)
        self.label_tiempoFin.grid(row=5, column=4)
        self.label_corrienteEntrada.grid(row=6, column=4)
        self.label_aux1.grid(row=10, column=4)
        self.label_aux2.grid(row=11, column=4)
        self.label_tipoCorriente.grid(row=8, column=4)
       
        self.txt_tiempoInicio.grid(row=4, column=5)
        self.txt_tiempoFin.grid(row=5, column=5)
        self.txt_corrienteEntrada.grid(row=6, column=5)
        self.txt_aux1.grid(row=10, column=5)
        self.txt_aux2.grid(row=11, column=5)
        
        self.simular_button.grid(row=15, column=1)
        self.limpiar_button.grid(row=15, column=3)
        self.ayuda_button.grid(row=15, column=4)
        self.salir_button.grid(row=15, column=5)
        self.parametrosDefault_button.grid(row=13, column=1, columnspan=2) 
        self.ajustesDefault_button.grid(row=13, column=4, columnspan=2)
        
        self.ventanaGraficas = None
        self.guiGraficas = None
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.var = IntVar()
        
        self.radioBDiscreto = Radiobutton(master, text="Discreto", variable=self.var, value=1, command=self.selectDiscreto)
        self.radioBContinuo = Radiobutton(master, text="Continuo", variable=self.var, value=2, command=self.selectContinuo)
        self.radioBAumento = Radiobutton(master, text="Aumento", variable=self.var, value=3, command=self.selectAumento)
        self.radioBDiscreto.select()
        self.radioBContinuo.deselect()
        self.radioBAumento.deselect()
        self.radioBDiscreto.grid(row=7, column=5)
        self.radioBContinuo.grid(row=8, column=5)
        self.radioBAumento.grid(row=9, column=5)       
        

    def simular(self): 
        
        validacion1 = True
        validacion1 = validacion1 and self.txt_capacitancia.get() != ""
        validacion1 = validacion1 and self.txt_conductanciaNa.get() != ""
        validacion1 = validacion1 and self.txt_conductanciaK.get() != ""
        validacion1 = validacion1 and self.txt_conductanciaL.get() != ""
        validacion1 = validacion1 and self.txt_potencialNa.get() != ""
        validacion1 = validacion1 and self.txt_potencialK.get() != ""
        validacion1 = validacion1 and self.txt_potencialL.get() != ""
        validacion1 = validacion1 and self.txt_tiempoInicio.get() != ""
        validacion1 = validacion1 and self.txt_tiempoFin.get() != ""
        validacion1 = validacion1 and self.txt_corrienteEntrada.get() != ""
         
        if( self.var.get() == 1 or self.var.get() == 3 ):        
            validacion1 = validacion1 and self.txt_aux1.get() != ""  
            validacion1 = validacion1 and self.txt_aux2.get() != ""  
        
        if(validacion1 == True):
            
            validacion2 = True
            validacion2 = validacion2 and self.esFlotante(self.txt_capacitancia.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_conductanciaNa.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_conductanciaK.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_conductanciaL.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_potencialNa.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_potencialK.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_potencialL.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_tiempoInicio.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_tiempoFin.get())
            validacion2 = validacion2 and self.esFlotante(self.txt_corrienteEntrada.get())
            
            if( self.var.get() == 1 or self.var.get() == 3 ):                    
                validacion2 = validacion2 and self.esFlotante(self.txt_aux1.get())
                validacion2 = validacion2 and self.esFlotante(self.txt_aux2.get())
            
            if(validacion2 == True):
                
                if( float(self.txt_tiempoInicio.get())<0.0 
                   or float(self.txt_tiempoFin.get())<float(self.txt_tiempoInicio.get()) 
                   or float(self.txt_corrienteEntrada.get())<0.0 ):
                    messagebox.showinfo("Error", "Hay datos no válidos")
                else: 
                    validacion3 = False
                    if( self.var.get() == 1 ): #discreto
                        if ( float(self.txt_aux1.get())<float(self.txt_tiempoInicio.get()) 
                            or float(self.txt_aux2.get())>float(self.txt_tiempoFin.get())
                            or float(self.txt_aux1.get())==float(self.txt_aux2.get()) 
                            or float(self.txt_aux1.get())>float(self.txt_aux2.get()) ):
                            messagebox.showinfo("Error", "Hay datos no válidos")
                        else:
                            validacion3 = True
                    if( self.var.get() == 3 ): #aumento
                        if ( float(self.txt_aux1.get())<0.0 
                            or float(self.txt_aux2.get())<0.0
                            or float(self.txt_aux2.get())>=float(self.txt_tiempoFin.get()) ):
                            messagebox.showinfo("Error", "Hay datos no válidos")
                        else:
                            validacion3 = True
                    if( self.var.get() == 2 ): #continuo
                        validacion3 = True
                    if (validacion3 == True):
                        self.graficar()
            else:            
                messagebox.showinfo("Error", "Hay datos no válidos")
                
        else:
            messagebox.showinfo("Error", "No se han completado todos los datos")
        
    def esFlotante(self, n):
        try:
            n1 = float(n)
        except (ValueError, TypeError):
            return False
        else:
            return True
        
    def graficar(self):
    		
        C_m = float( self.txt_capacitancia.get() )
        g_Na = float( self.txt_conductanciaNa.get() )
        g_K = float( self.txt_conductanciaK.get() )
        g_L = float( self.txt_conductanciaL.get() )
        E_Na = float( self.txt_potencialNa.get() )
        E_K = float( self.txt_potencialK.get() )
        E_L = float( self.txt_potencialL.get() )
        tI = float( self.txt_tiempoInicio.get() )
        tF = float( self.txt_tiempoFin.get() )
        cI = float( self.txt_corrienteEntrada.get() )
        
        if( self.var.get() == 1 or self.var.get() == 3 ):       
            aux1 = float( self.txt_aux1.get() )
            aux2 = float( self.txt_aux2.get() )
        else:
            aux1 = -1
            aux2 = -1
        
        if(self.ventanaGraficas!=None):
            self.ventanaGraficas.quit()    
            self.ventanaGraficas.destroy()
            
        self.ventanaGraficas = Tk()
        self.guiGraficas = GUIgraficas(self.ventanaGraficas,C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI, aux1, aux2, self.var.get())
        self.ventanaGraficas.mainloop()
        self.ventanaGraficas = None
        
    def establecerPPredeterminados(self):
        self.txt_capacitancia.delete(0,'end')
        self.txt_capacitancia.insert(0,1.0)
        self.txt_conductanciaNa.delete(0,'end')
        self.txt_conductanciaNa.insert(0,120.0)
        self.txt_conductanciaK.delete(0,'end')
        self.txt_conductanciaK.insert(0,36.0)
        self.txt_conductanciaL.delete(0,'end')
        self.txt_conductanciaL.insert(0,0.3)
        self.txt_potencialNa.delete(0,'end')
        self.txt_potencialNa.insert(0,50.0)
        self.txt_potencialK.delete(0,'end')
        self.txt_potencialK.insert(0,-77.0)
        self.txt_potencialL.delete(0,'end')
        self.txt_potencialL.insert(0,-54.387)
        
    def establecerAPredeterminados(self):        
        self.txt_tiempoInicio.delete(0,'end')
        self.txt_tiempoInicio.insert(0,0) 
        self.txt_tiempoFin.delete(0,'end')
        self.txt_tiempoFin.insert(0,100.0) 
        self.txt_corrienteEntrada.delete(0,'end')
        self.txt_corrienteEntrada.insert(0,10.0)
        self.txt_aux1.delete(0,'end')        
        self.txt_aux2.delete(0,'end')       
        
        if( self.var.get() == 1 ):
            self.txt_aux1.insert(0,40.0)
            self.txt_aux2.insert(0,50.0)
        else:
            if( self.var.get() == 3 ):
                self.txt_aux1.insert(0,3.0)
                self.txt_aux2.insert(0,20.0)               
        
    def limpiar(self):        
        self.txt_capacitancia.delete(0,'end')
        self.txt_conductanciaNa.delete(0,'end')
        self.txt_conductanciaK.delete(0,'end')
        self.txt_conductanciaL.delete(0,'end')
        self.txt_potencialNa.delete(0,'end')
        self.txt_potencialK.delete(0,'end')
        self.txt_potencialL.delete(0,'end')        
        self.txt_tiempoInicio.delete(0,'end')
        self.txt_tiempoFin.delete(0,'end')
        self.txt_corrienteEntrada.delete(0,'end')
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        if(self.ventanaGraficas!=None):
            self.ventanaGraficas.quit()    
            self.ventanaGraficas.destroy()
        
    def ayudar(self):
        subprocess.Popen("ayuda.pdf",shell=True)
        
    def salir(self):
        self.master.quit()    
        self.master.destroy()  
    
    def on_closing(self):
        self.master.quit()     
        self.master.destroy()
        
    def selectDiscreto(self):
        self.txt_aux1.grid()
        self.txt_aux2.grid()
        self.label_aux1.grid()   
        self.label_aux2.grid()         
        
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.label_aux1.config(text='Inicio estímulo(ms)')
        self.label_aux2.config(text='Fin estímulo(ms)')
        
    def selectContinuo(self):
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.txt_aux1.grid_remove()
        self.txt_aux2.grid_remove()
        self.label_aux1.grid_remove()    
        self.label_aux2.grid_remove()         
        
    def selectAumento(self):
        self.txt_aux1.grid()
        self.txt_aux2.grid()
        self.label_aux1.grid()   
        self.label_aux2.grid()  
        
        self.txt_aux1.delete(0,'end')
        self.txt_aux2.delete(0,'end')
        self.label_aux1.config(text='Aumento de corriente(uA/cm^2)')
        self.label_aux2.config(text='Cada (ms)')

def main():
    root = Tk()
    myGui = GUI(root)
    root.mainloop()    

if __name__ == "__main__":
    main()