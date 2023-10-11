""""-----------------------------------------------------------------------
 Universidad del Valle de Guatemala
 Física 3
 05/10/2023
 Diego García 22404
 César López 22535

 Ejercicio #5 parcial 2
-----------------------------------------------------------------------"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
from sympy import *
from sympy.abc import x
import math

#---------------------------------------------funciones del código-------------------------------------------------
def actualizar(*args): #Actualiza dinamicamente la interfaz dependiendo del capacitor
    if capacitor.current() == 0:
        l1.config(text='Tamaño de las placas(m)')
        l2.config(text='Ancho de las placas(m)')
        l3.config(text='Espacio entre placas(m)')
        l4.grid()
        caja4.grid()
    elif capacitor.current() == 1:
        l1.config(text='Radio interno(m)')
        l2.config(text='Radio externo(m)')
        l3.config(text='Voltaje(V)')
        l4.grid_remove()
        caja4.grid_remove()
    else:
        l1.config(text='Radio interno(m)')
        l2.config(text='Radio externo(m)')
        l3.config(text='Largo del cilindro(m)')
        l4.grid()
        caja4.grid()
    
    res1.config(text='                                                                         ')
    res2.config(text='                                                                         ')
    res3.config(text='                                                                         ')
    res4.config(text='                                                                         ')
    res5.config(text='                                                                         ')
    res6.config(text='                                                                         ')
    res7.config(text='                                                                         ')
    res8.config(text='                                                                         ')
    res9.config(text='                                                                         ')

    createNew()

def createNew():   #crea y limpia el canvas
    c.delete('all')
    c.place(x=750,y=10) 

def create_circle(x, y, r,**kwargs): #para hacer circulos más facil
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return c.create_oval(x0, y0, x1, y1,**kwargs)

def create_circle_arc(x, y, r, **kwargs):   #para hacer arcos más fácil
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs.pop("end") - kwargs["start"]
    return c.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def grafica(tipoc,tipod,datoA,datoB,datoC): #graficas
    #escala = 43
    wm = 380
    hm = 340

    if tipoc==0:                        #Placas paralelas
        largo = datoA*21
        ancho = datoB*21
        distancia = datoC*21

        if tipod==0:                    #Sin dielectrico
            createNew()
            c.create_line(wm-largo,hm+distancia,wm-largo,hm-distancia,dash=(2, 2),fill="purple",width=3)
            c.create_line(wm+largo,hm+distancia,wm+largo,hm-distancia,dash=(2, 2),fill="purple",width=3)
            c.create_rectangle(wm-largo,hm+distancia,wm+largo,hm+distancia+ancho,width=5,fill="blue",outline="blue")
            c.create_rectangle(wm-largo,hm-distancia,wm+largo,hm-distancia-ancho,width=5,fill="red",outline="red")

        elif tipod==1:                  #Dielectrico medio
            createNew()
            c.create_rectangle(wm-largo,hm+distancia,wm,hm-distancia,outline="grey",fill="lightgrey",width=3)
            c.create_line(wm+largo,hm+distancia,wm+largo,hm-distancia,dash=(2, 2),fill="purple",width=3)
            c.create_rectangle(wm-largo,hm+distancia,wm+largo,hm+distancia+ancho,width=5,fill="blue",outline="blue")
            c.create_rectangle(wm-largo,hm-distancia,wm+largo,hm-distancia-ancho,width=5,fill="red",outline="red")

        else:                           #Dielectrico completo
            createNew()
            c.create_rectangle(wm-largo,hm+distancia,wm+largo,hm-distancia,outline="grey",fill="lightgrey",width=3)
            c.create_rectangle(wm-largo,hm+distancia,wm+largo,hm+distancia+ancho,width=5,fill="blue",outline="blue")
            c.create_rectangle(wm-largo,hm-distancia,wm+largo,hm-distancia-ancho,width=5,fill="red",outline="red")
        
    else:                               #Cilindro y esfera
        ra = datoA*21
        rb = datoB*21

        if tipod==0:                    #Sin dielectrico
            createNew()
            create_circle(wm,hm,rb,width=5,outline="red")
            create_circle(wm,hm,ra,width=5,outline="blue")

        elif tipod==1:                  #Dielectrico medio
            createNew()
            create_circle_arc(wm,hm,rb,start=180,end=360,fill="lightgrey",outline="grey",width=5)
            create_circle(wm,hm,ra,fill="#bde0fe",outline="#bde0fe")
            create_circle(wm,hm,rb,width=5,outline="red")
            create_circle(wm,hm,ra,width=5,outline="blue")

        else:                           #Dielectrico completo
            createNew()
            create_circle(wm,hm,rb,fill="lightgrey",outline="grey",width=5)
            create_circle(wm,hm,ra,fill="#bde0fe",outline="#bde0fe")
            create_circle(wm,hm,rb,width=5,outline="red")
            create_circle(wm,hm,ra,width=5,outline="blue")


#---------------------------------------------- Página inicial ----------------------------------------------
v = Tk()
v.title('Problema #5')
v.geometry('1520x700')
t = Label(v,text=('Propiedades de un capacitor'),font=('Arial 18 underline'))
t.grid(column=0,row=0)
ins = Label(v,text=('Escoja el capacitor'),font=('Arial 16'))
ins.grid(column=0,row=1)
c = Canvas(v,bg = "#bde0fe",height = "680",width= "760")

#--------------------------------------------- Combo boxes -------------------------------------------------
capacitor = ttk.Combobox(v,values=['Placas paralelas','Esférico','Cilíndrico'],state='readonly')
capacitor.grid(column=0,row=2)
capacitor.current(0)
capacitor.bind("<<ComboboxSelected>>", actualizar)

dielectrico = ttk.Combobox(v,values=['Sin dielectrico','Dielectrico medio','Dielectrico completo'],state='readonly')
dielectrico.grid(column=0,row=3)
dielectrico.current(0)
dielectrico.bind("<<ComboboxSelected>>", actualizar)

#--------------------------------------------- Labels y cajas para recibir datos -------------------------------------------------

l1 = Label(v,text='Largo de las placas(m)',font=('Arial 13'))
l1.grid(column=1,row=1)
caja1 = Entry(v,font=('Arial 14'))
caja1.grid(column=2,row=1)

l2 = Label(v,text='Ancho de las placas(m)',font=('Arial 13'))
l2.grid(column=1,row=2)
caja2 = Entry(v,font=('Arial 14'))
caja2.grid(column=2,row=2)

l3 = Label(v,text='Espacio entre placas(m)',font=('Arial 13'))
l3.grid(column=1,row=3)
caja3 = Entry(v,font=('Arial 14'))
caja3.grid(column=2,row=3)

l4 = Label(v,text='Voltaje(V)',font=('Arial 13'))
l4.grid(column=1,row=4)
caja4 = Entry(v,font=('Arial 14'))
caja4.grid(column=2,row=4)


#--------------------------------------------- Labels de respuestas -------------------------------------------------
empty = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
empty.grid(column=0,row=6,columnspan=2)
res1 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res1.grid(column=0,row=7,columnspan=2)
res2 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res2.grid(column=0,row=8,columnspan=2)
res3 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res3.grid(column=0,row=9,columnspan=2)
res4 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res4.grid(column=0,row=10,columnspan=2)
res5 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res5.grid(column=0,row=11,columnspan=2)
res6 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res6.grid(column=0,row=12,columnspan=2)
res7 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res7.grid(column=0,row=13,columnspan=2)
res8 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res8.grid(column=0,row=14,columnspan=2)
res9 = Label(v,text='                                                                   ',font=('Arial 15'),bg=('#F0F0F0'),anchor='w')
res9.grid(column=0,row=15,columnspan=2)

actualizar()

#--------------------------------------------- Funcion de calculos -------------------------------------------------
def calculos():
    capa = capacitor.current()            #tipo de capacitor
    dielec = dielectrico.current()        #tipo de dielectrico
    k = 3.40                              #constante Dielectrica
    e = 8.85e-12                          #epsilon
    pi = math.pi

    
    if capa==0:            #Placas paralelas
        if caja1.get()=='' or caja2.get()=='' or caja3.get()=='' or caja4.get()=='':
            messagebox.showinfo('ERROR','Por favor, ingrese un valor en las cajas.')
        else:
            try:
                largo = float(caja1.get())                       #largo de placa
                ancho = float(caja2.get())                       #ancho de placas
                distancia = float(caja3.get())                   #espacio entre placas
                voltaje = float(caja4.get())                     #voltaje
            except:
                messagebox.showinfo('ERROR','Por favor, ingrese un número en cada espacio.')
            else:
                if largo <= 0 or ancho <= 0 or distancia <= 0 or voltaje <= 0:
                    messagebox.showinfo('ERROR','Por favor, asegurese que los valores sean mayores a 0.')
                else:
                    area = largo*ancho

                    if dielec==0: #sin dielectrico
                        capacit = (area*e)/distancia            #Capacitancia
                        crg = capacit*voltaje                   #Carga
                        energy = (capacit*voltaje**2)/2         #Energía

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='                                                                         ')
                        res5.config(text='                                                                         ')
                        res6.config(text='                                                                         ')
                        res7.config(text='                                                                         ')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    elif dielec==1: #medio dielectrico
                        capA = (area*e)/(2*distancia)                               #capacitancia en la parte sin dielectrico
                        capD = (k*area*e)/(2*distancia)                             #capacitancia en la parte con dielectrico
                        capacit = capD + capA                                       #Capacitancia total
                        cog = (area*e)/distancia                                    
                        crg = cog*voltaje                                           #Carga
                        energy = (cog*voltaje**2)/4 + (capacit*(voltaje/k)**2)/4    #Energía almacenada
                        libA = (2*crg)/((k+1)*(area))                               #Carga liberada del aire
                        libP = (2*crg*k)/((k+1)*(area))                             #Carga liberada del plexiglas
                        lig = ((k-1)/(k+1))*((2*crg)/area)                          #Carga ligada

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libA = np.format_float_scientific(libA, precision = 2, exp_digits=2)
                        libP = np.format_float_scientific(libP, precision = 2, exp_digits=2)
                        lig = np.format_float_scientific(lig, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre del aire es '+str(libA)+'C/m²')
                        res5.config(text='La carga libre del plexiglas es '+str(libP)+'C/m²')
                        res6.config(text='La carga ligada es '+str(lig)+'C/m²')
                        res7.config(text='                                                                         ')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    else:           #dielectrico completo
                        capacit = (k*area*e)/distancia              #Capacitancia
                        cog = (area*e)/distancia                    
                        crg = cog*voltaje                           #Carga
                        energy = (capacit*(voltaje/k)**2)/2         #Energía almacenada
                        libP = crg/area                             #Carga libre del dielectrico
                        lig = libP*(1-(1/k))                        #Carga ligada

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libP = np.format_float_scientific(libP, precision = 2, exp_digits=2)
                        lig = np.format_float_scientific(lig, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre es '+str(libP)+'C/m²')
                        res5.config(text='La carga ligada es '+str(lig)+'C/m²')
                        res6.config(text='                                                                         ')
                        res7.config(text='                                                                         ')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    grafica(capa,dielec,largo,ancho,distancia)

    elif capa==1:     #esfera
        if caja1.get()=='' or caja2.get()=='' or caja3.get()=='':
            messagebox.showinfo('ERROR','Por favor, ingrese un valor en las cajas.')
        else:
            try:
                ra = float(caja1.get())                       #radio interno
                rb = float(caja2.get())                       #radio externo
                voltaje = float(caja3.get())                  #voltaje
            except:
                messagebox.showinfo('ERROR','Por favor, ingrese un número en cada espacio.')
            else:
                if ra <= 0 or rb <= 0 or voltaje <= 0:
                    messagebox.showinfo('ERROR','Por favor, asegurese que los valores sean mayores a 0.')
                elif ra >= rb:
                    messagebox.showinfo('ERROR','Por favor, asegurese que el radio exterior sea mayor al menor.')
                else:
                    if dielec==0:       #sin dielectrico
                        capacit = ((ra*rb)*(4*pi*e))/(rb-ra)                #Capacitancia
                        crg = capacit*voltaje                               #Carga
                        energy = (capacit*(voltaje**2))/2                   #Energía almacenada

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='                                                                         ')
                        res5.config(text='                                                                         ')
                        res6.config(text='                                                                         ')
                        res7.config(text='                                                                         ')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    elif dielec==1:       #medio dielectrico
                        capA = ((ra*rb)*(2*pi*e))/(rb-ra)                               #capacitancia en la parte sin dielectrico
                        capD = (k*(ra*rb)*(2*pi*e))/(rb-ra)                             #capacitancia en la parte con dielectrico
                        capacit = capD + capA                                           #capacitancia total
                        cog = ((ra*rb)*(4*pi*e))/(rb-ra)                                
                        crg = cog*voltaje                                               #Carga
                        energy = (capacit*voltaje**2)/4+(capacit*(voltaje/k)**2)/4      #Energía acumulada
                        libRaSup = crg/((2*pi*ra**2)*(1+k))                             #Carga libre Ra superior
                        libRbSup = crg/((2*pi*rb**2)*(1+k))                             #Carga libre Rb superior
                        libRaInf = (crg*k)/((2*pi*ra**2)*(1+k))                         #Carga libre Ra inferior
                        libRbInf = (crg*k)/((2*pi*rb**2)*(1+k))                         #Carga libre Rb inferior
                        ligRa = ((k-1)/(k+1))*(crg/(2*pi*ra**2))                        #Carga ligada Ra
                        ligRb = ((k-1)/(k+1))*(crg/(2*pi*rb**2))                        #Carga ligada Rb

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libRaSup = np.format_float_scientific(libRaSup, precision = 2, exp_digits=2)
                        libRbSup = np.format_float_scientific(libRbSup, precision = 2, exp_digits=2)
                        libRaInf = np.format_float_scientific(libRaInf, precision = 2, exp_digits=2)
                        libRbInf = np.format_float_scientific(libRbInf, precision = 2, exp_digits=2)
                        ligRa = np.format_float_scientific(ligRa, precision = 2, exp_digits=2)
                        ligRb = np.format_float_scientific(ligRb, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre del aire Ra superior es '+str(libRaSup)+'C/m²')
                        res5.config(text='La carga libre del aire Rb superior es '+str(libRbSup)+'C/m²')
                        res6.config(text='La carga libre del aire Ra inferior es '+str(libRaInf)+'C/m²')
                        res7.config(text='La carga libre del aire Rb inferior es '+str(libRbInf)+'C/m²')
                        res8.config(text='La carga ligada del plexiglas Ra inferior es '+str(ligRa)+'C/m²')
                        res9.config(text='La carga ligada del plexiglas Rb inferior es '+str(ligRb)+'C/m²')
                                                
                    else:      #dielectrico completo
                        capacit = (k*(ra*rb)*(4*pi*e))/(rb-ra)                  #Capacitancia
                        cog = ((ra*rb)*(4*pi*e))/(rb-ra)                        
                        crg = cog*voltaje                                       #Carga
                        energy = (capacit*(voltaje/k)**2)/2                     #Energía almacenada
                        libRa = crg/(4*pi*ra**2)                                #Carga liberada Ra
                        libRb = crg/(4*pi*rb**2)                                #Carga liberada Rb
                        ligRa = libRa*(1-1/k)                                   #Carga ligada Ra
                        ligRb = libRb*(1-1/k)                                   #Carga ligada Rb

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libRa = np.format_float_scientific(libRa, precision = 2, exp_digits=2)
                        libRb = np.format_float_scientific(libRb, precision = 2, exp_digits=2)
                        ligRa = np.format_float_scientific(ligRa, precision = 2, exp_digits=2)
                        ligRb = np.format_float_scientific(ligRb, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre del aire Ra es '+str(libRa)+'C/m²')
                        res5.config(text='La carga libre del aire Rb es '+str(libRb)+'C/m²')
                        res6.config(text='La carga ligada del plexiglas Ra es '+str(ligRa)+'C/m²')
                        res7.config(text='La carga ligada del plexiglas Rb es '+str(ligRb)+'C/m²')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    grafica(capa,dielec,ra,rb,0)

    else:  #cilindro
        if caja1.get()=='' or caja2.get()=='' or caja3.get()=='' or caja4.get()=='':
            messagebox.showinfo('ERROR','Por favor, ingrese un valor en las cajas.')
        else:
            try:
                ra = float(caja1.get())                       #radio interno
                rb = float(caja2.get())                       #radio externo
                largo = float(caja3.get())                    #largo del cilindro
                voltaje = float(caja4.get())                  #voltaje
            except:
                messagebox.showinfo('ERROR','Por favor, ingrese un número en cada espacio.')
            else:
                if ra <= 0 or rb <= 0 or voltaje <= 0 or largo <= 0:
                    messagebox.showinfo('ERROR','Por favor, asegurese que los valores sean mayores a 0.')
                elif ra >= rb:
                    messagebox.showinfo('ERROR','Por favor, asegurese que el radio exterior sea mayor al menor.')
                else:
                    if dielec==0:   #sin dielectrico
                        capacit = (2*pi*largo*e)/(ln(rb/ra))        #Capacitancia
                        crg = capacit*voltaje                       #Carga
                        energy = (capacit*voltaje**2)/2             #Energía acumulada

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)


                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='                                                                         ')
                        res5.config(text='                                                                         ')
                        res6.config(text='                                                                         ')
                        res7.config(text='                                                                         ')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    elif dielec==1:         #medio dielectrico
                        capA = ((pi*largo*e))/(ln(rb/ra))                   #capacitancia en la parte sin dielectrico
                        capD = (k*pi*largo*e)/(ln(rb/ra))                 #capacitancia en la parte con dielectrico
                        capacit = capD + capA                               #capacitancia total
                        cog = (2*pi*largo*e)/(ln(rb/ra))                    
                        crg = cog*voltaje                                   #Carga
                        energy = (cog*(voltaje**2))/4 + (capacit*(voltaje/k)**2)/4 #Energía acumulada
                        libRaSup = crg/((2*pi*ra*largo*(k+1))/2)                    #carga liberada Ra superior
                        libRbSup = crg/((2*pi*rb*largo*(k+1))/2)                    #carga liberada Rb superior
                        libRaInf = (crg*k)/((2*pi*ra*largo*(k+1))/2)                #carga liberada Ra inferior
                        libRbInf = (crg*k)/((2*pi*rb*largo*(k+1))/2)                #carga liberada Rb inferior
                        ligRa = libRaInf*(1-1/k)                                    #carga ligada Ra
                        ligRb = libRbInf*(1-1/k)                                    #carga ligada Rb


                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libRaSup = np.format_float_scientific(libRaSup, precision = 2, exp_digits=2)
                        libRbSup = np.format_float_scientific(libRbSup, precision = 2, exp_digits=2)
                        libRaInf = np.format_float_scientific(libRaInf, precision = 2, exp_digits=2)
                        libRbInf = np.format_float_scientific(libRbInf, precision = 2, exp_digits=2)
                        ligRa = np.format_float_scientific(ligRa, precision = 2, exp_digits=2)
                        ligRb = np.format_float_scientific(ligRb, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre del aire Ra superior es '+str(libRaSup)+'C/m²')
                        res5.config(text='La carga libre del aire Rb superior es '+str(libRbSup)+'C/m²')
                        res6.config(text='La carga libre del aire Ra inferior es '+str(libRaInf)+'C/m²')
                        res7.config(text='La carga libre del aire Rb inferior es '+str(libRbInf)+'C/m²')
                        res8.config(text='La carga ligada del plexiglas Ra inferior es '+str(ligRa)+'C/m²')
                        res9.config(text='La carga ligada del plexiglas Rb inferior es '+str(ligRb)+'C/m²')
                        
                    else:     #dielectrico completo
                        capacit = (k*2*pi*largo*e)/(ln(rb/ra))               #Capacitancia
                        cog = (2*pi*largo*e)/(ln(rb/ra))                     
                        crg = cog*voltaje                                    #Carga
                        energy = (capacit*(voltaje/k)**2)/2                  #Energía acumulada
                        libRa = crg/(2*pi*ra*largo)                          #Carga liberada Ra
                        libRb = crg/(2*pi*rb*largo)                          #Carga liberada Rb
                        ligRa = libRa*(1-1/k)                                #Carga ligada Ra
                        ligRb = libRb*(1-1/k)                                #Carga ligada Rb

                        #------------------------ Notación cientifica -----------------------------------
                        capacit = np.format_float_scientific(capacit, precision = 2, exp_digits=2)
                        crg = np.format_float_scientific(crg, precision = 2, exp_digits=2)
                        energy = np.format_float_scientific(energy, precision = 2, exp_digits=2)
                        libRa = np.format_float_scientific(libRa, precision = 2, exp_digits=2)
                        libRb = np.format_float_scientific(libRb, precision = 2, exp_digits=2)
                        ligRa = np.format_float_scientific(ligRa, precision = 2, exp_digits=2)
                        ligRb = np.format_float_scientific(ligRb, precision = 2, exp_digits=2)

                        #--------------------------- Respuestas escritas -----------------------------------
                        res1.config(text='La capacitancia es '+str(capacit)+'F')
                        res2.config(text='La carga es '+str(crg)+'C')
                        res3.config(text='La energía almacenada es '+str(energy)+'J')
                        res4.config(text='La carga libre del aire Ra es '+str(libRa)+'C/m²')
                        res5.config(text='La carga libre del aire Rb es '+str(libRb)+'C/m²')
                        res6.config(text='La carga ligada del plexiglas Ra es '+str(ligRa)+'C/m²')
                        res7.config(text='La carga ligada del plexiglas Rb es '+str(ligRb)+'C/m²')
                        res8.config(text='                                                                         ')
                        res9.config(text='                                                                         ')

                    grafica(capa,dielec,ra,rb,0)

#-------------------------------------------------- Botón -------------------------------------------------
bt1 = Button(v,text='Calcular',bd=4,bg='lightgreen',font=('Arial 17 bold'),width=20,command=calculos)
bt1.grid(column=1,row=5,columnspan=2)

v.mainloop()