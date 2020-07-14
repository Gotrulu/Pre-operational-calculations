import numpy as np
import tkinter as tk
from tkinter import *
from math import pi
from matplotlib import pyplot
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import seaborn as sns
import pandas as pd
   
#data del cable que se va a trabajar

cables = ["Rochester 1H314K - 5/16in", "Camesa 1N32PTZ - 5/16 in", "Rochester 1H220A - 7/32in", "Rochester 1H226K - 7/32"]
diametro = [0.3125, 0.3125, 0.21875, 0.21875] # diametro de los cables
cbs = [12400, 12000, 6100, 4800] #Punto de Ruptura (lbs)
weigh = [190, 194, 94, 96] #Peso del Cable (lbs/Kft)
wirebs = [471, 442, 234, 190 ] #Punto de Ruptura Alambre (lbs)
mt = [500, 500, 300, 500] #Máxima Temperatura (°F)ñ
especificaciones_cable = [cables, diametro, cbs, weigh, wirebs, mt] #lista especificaciones del cable    

def abrirventana2():
	
	raiz.withdraw()
	#---------------------------------------------------------#
	raiz2 = tk.Toplevel()
	raiz2.geometry("1000x500+20+20")
	raiz2.resizable(True,True)
	raiz2.config(background="slate gray")
	raiz2.title("Profundidad vs tensiones")
	raiz2.iconbitmap("cabezaelectrica.ico")#Llamar un icono para la raiz
	
	#---------------------------------------------------------#
	miFrame2=Frame(raiz2, width=1000, height=500 )
	miFrame2.grid(row=2,column=0, sticky="e", padx=2, pady=2, columnspan=3)
	miFrame2.config(bg="orange")#le damos un color al frame
	miFrame2.config(bd=40)#le damos un grosor al borde
	miFrame2.config(cursor="hand2")
	#miFrame2.pack()
	#---------------------------------------------------------#
	proVsten=Label(miFrame2, text="Profundidad vs tensiones:", bg="orange", fg="white", font=('Arial', 12))
	proVsten.grid(row=1,column=1, sticky="e", padx=2, pady=2)
	#proVsten.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
	#---------------------------------------------------------#
	button1=Button(raiz2, text="Salir programa", command=raiz2.destroy)
	button1.config(cursor="hand1")
	#button1.pack(side=tk.BOTTOM)
	button1.grid(row=3,column=0, padx=2, pady=2)
	#---------------------------------------------------------#
	imagen=PhotoImage(file="logosummum001.png")#llamamos la imagen del logo de Summum
	logo=Label(raiz2,image=imagen, bg="slate gray")#.place(x=0,y=0)	
	#logo.pack()
	logo.grid(row=1,column=2, padx=2, pady=2)
	#----------------------------------------------------------#
	numeroCable=StringVar()
	cableLabel=Label(miFrame2, text="Seleccione el tipo de cable:", bg="orange", fg="white", font=('Arial', 12))
	cableLabel.grid(row=0,column=2, sticky="e", padx=2, pady=2)
	cuadroCable=Entry(miFrame2, textvariable=numeroCable, width=3)
	cuadroCable.grid(row=1,column=2, padx=2, pady=2)
	cuadroCable.config(background="black", fg="#03f943", justify="center", font=('Arial', 14))
	#-----Pulsaciones teclado para obtener el cable------------- 
	def numeroPulsado(num):
		numeroCable.set(num)
	#--------------------menu de selección de cable------------#
	varOpcion=IntVar()
	boton1=Radiobutton(miFrame2, text="1.", variable=varOpcion, value=1, command=lambda:numeroPulsado("1"), bg="orange", fg="black", font=('Arial', 14))
	boton1.deselect()
	boton1.grid(row=0,column=0, sticky="e", padx=10, pady=2) 
	cableLabel=Label(miFrame2, text="Si es Rochester 1H314K - 5/16in", bg="orange", fg="white", font=('Arial', 12))
	cableLabel.grid(row=0,column=1, sticky="w", padx=2, pady=2)

	boton2=Radiobutton(miFrame2, text="2.", variable=varOpcion, value=2, command=lambda:numeroPulsado("2"), bg="orange", fg="black", font=('Arial', 14))
	boton2.deselect()
	boton2.grid(row=1,column=0, sticky="e", padx=10, pady=2) 
	cableLabel=Label(miFrame2, text="Si es Camesa 1N32PTZ - 5/16 in", bg="orange", fg="white", font=('Arial', 12))
	cableLabel.grid(row=1,column=1, sticky="w", padx=2, pady=2)

	boton3=Radiobutton(miFrame2, text="3.", variable=varOpcion, value=3, command=lambda:numeroPulsado("3"), bg="orange", fg="black", font=('Arial', 14))
	boton3.deselect()
	boton3.grid(row=2,column=0, sticky="e", padx=10, pady=2) 
	cableLabel=Label(miFrame2, text="Si es Rochester 1H220A - 7/32in", bg="orange", fg="white", font=('Arial', 12))
	cableLabel.grid(row=2,column=1, sticky="w", padx=2, pady=2)

	boton4=Radiobutton(miFrame2, text="4.", variable=varOpcion, value=4, command=lambda:numeroPulsado("4"), bg="orange", fg="black", font=('Arial', 14))
	boton4.deselect()
	boton4.grid(row=3,column=0, sticky="e", padx=10, pady=2) 
	cableLabel=Label(miFrame2, text="Si es Rochester 1H226K - 7/32", bg="orange", fg="white", font=('Arial', 12))
	cableLabel.grid(row=3,column=1, sticky="w", padx=2, pady=2)
	
	#------configuramos la etiqueta y el cuadro donde se ingresa la profundidad---------------#

	profundidad=StringVar()#definimos la varible para entar en el entry de profundidad
	profundidadLabel= Label(miFrame2, text="Ingrese la maxima profundidad en ft:", bg="orange", fg="white", font=('Arial', 12))
	profundidadLabel.grid(row=4,column=1, sticky="e", padx=2, pady=2)
	cuadroProfundidad=Entry(miFrame2, textvariable=profundidad)#asignamos la vaible profundidad al Entry del cuadro de profundidad
	cuadroProfundidad.grid(row=4,column=2, padx=2, pady=2, sticky="w")

	#---------Configuramos la etiqueta y el cuadro donde se ingresa la el delta rango de ------------#
	
	profundidadRan=StringVar()
	ranLabel=Label(miFrame2, text="Ingrese el delta de rango de la profundidad:", bg="orange", fg="white", font=('Arial', 12))
	ranLabel.grid(row=5,column=1, sticky="e", padx=2, pady=2)
	cuadroRan=Entry(miFrame2, textvariable=profundidadRan)
	cuadroRan.grid(row=5,column=2, padx=2, pady=2, sticky="w")

	#-----------------------------------------------------#

	pesoHerr=StringVar()
	herLabel=Label(miFrame2, text="Ingrese el peso de la herramienta en (lbs):", bg="orange", fg="white", font=('Arial', 12))
	herLabel.grid(row=6,column=1, sticky="e", padx=2, pady=2)
	cuadroHer=Entry(miFrame2, textvariable=pesoHerr)
	cuadroHer.grid(row=6,column=2, padx=2, pady=2, sticky="w")

	
	#---------Configuramos la etiqueta y el cuadro donde se ingresa el factor de boyancia ------------#
	
	factorboyancia=StringVar()
	boyLabel=Label(miFrame2, text="Ingrese el factor de boyancia:", bg="orange", fg="white", font=('Arial', 12))
	boyLabel.grid(row=7,column=1, sticky="e", padx=2, pady=2)
	cuadroBoy=Entry(miFrame2, textvariable=factorboyancia)
	cuadroBoy.grid(row=7,column=2, padx=2, pady=2, sticky="w")



	#configuramos un boton para calcular el rango de tensiones			
	
	def calRtensiones():
		
	   
		
		p=float(cuadroProfundidad.get())
		dp=int(cuadroRan.get())
		ph=float(cuadroHer.get())
		tc=int(cuadroCable.get())
		fb=float(cuadroBoy.get())

		rango=np.arange(0, p+2, step=dp)
		tensionVsprofundidad=pd.DataFrame(data=rango, columns=["Profundidad (ft)"])

		def pvst(pesoCable,profundidad,pesoh):
				t=((pesoCable*profundidad)/1000)+pesoh
				return t

		def ptbf(pesoCable,profundidad,pesoh,bf):
				tf=(((pesoCable*profundidad)/1000)+pesoh)*bf
				return tf
		
		tensionVsprofundidad["Tension subiendo (lbs)"]=tensionVsprofundidad["Profundidad (ft)"].apply(lambda x: pvst((especificaciones_cable[3] [tc-1]),x,ph))
		tensionVsprofundidad["Tension bajando (lbs)"]=tensionVsprofundidad["Profundidad (ft)"].apply(lambda x: ptbf((especificaciones_cable[3] [tc-1]),x,ph,fb))
		print(tensionVsprofundidad)
		table = Text(raiz2)
		table.insert(INSERT, tensionVsprofundidad.to_string())
		table.grid(row=2,column=3, sticky="e", padx=2, pady=2)
		profundida=tensionVsprofundidad["Profundidad (ft)"]
		
	botoncalRtensiones=Button(miFrame2, text="Calcular rango de tensiones", command=calRtensiones)
	botoncalRtensiones.grid(row=8,column=0, sticky="e", padx=2, pady=2)
	
	def grafRtensiones():
		
		p=float(cuadroProfundidad.get())
		dp=int(cuadroRan.get())
		ph=float(cuadroHer.get())
		tc=int(cuadroCable.get())
		fb=float(cuadroBoy.get())

		rango=np.arange(0, p+2, step=dp)
		tensionVsprofundidad=pd.DataFrame(data=rango, columns=["Profundidad (ft)"])

		def pvst(pesoCable,profundidad,pesoh):
				t=((pesoCable*profundidad)/1000)+pesoh
				return t

		def ptbf(pesoCable,profundidad,pesoh,bf):
				tf=(((pesoCable*profundidad)/1000)+pesoh)*bf
				return tf
		
		tensionVsprofundidad["Tension subiendo (lbs)"]=tensionVsprofundidad["Profundidad (ft)"].apply(lambda x: pvst((especificaciones_cable[3] [tc-1]),x,ph))
		tensionVsprofundidad["Tension bajando (lbs)"]=tensionVsprofundidad["Profundidad (ft)"].apply(lambda x: ptbf((especificaciones_cable[3] [tc-1]),x,ph,fb))
			
		bajando=tensionVsprofundidad["Tension bajando (lbs)"]
		subiendo=tensionVsprofundidad["Tension subiendo (lbs)"]
		profundida=tensionVsprofundidad["Profundidad (ft)"]
		plt.figure(figsize=(9, 3))
		plt.subplot(121)
		plt.plot(profundida, bajando)
		plt.grid(True)
		plt.xlabel("Profundidad (ft)")
		plt.ylabel("Tensión (lbs)")
		plt.legend(["Tensión en (lbs)"])
		plt.subplot(122)
		plt.plot(profundida, subiendo)
		plt.suptitle('PROFUNDIDAD VS TENSIONES')
		plt.legend(["Tensión en (lbs)"])
		plt.xlabel("Profundidad (ft)")
		plt.ylabel("Tensón (lbs)")
		plt.grid(True)
		plt.show()

	botonGrafica=Button(miFrame2, text="Graficar rango de tensiones", command=grafRtensiones)
	botonGrafica.grid(row=8,column=1, sticky="e", padx=2, pady=2)
	raiz2.mainloop()




	
	


#---------------------------------------------------------------------------------------#


def cerrarventana():
	miFrame2.destroy()


raiz = tk.Tk()
raiz.title("Calculos preoperacionales")#Poner un titulo a la raiz
raiz.iconbitmap("cabezaelectrica.ico")#Llamar un icono para la raiz
raiz.resizable(True,True)#redimencionar la raiz
#raiz.geometry("1300x600")#le da una dimensión a la raiz
raiz.config(background="slate gray")#le da un color a la raiz
imagen=PhotoImage(file="logosummum001.png")#llamamos la imagen del logo de Summum
logo=Label(raiz,image=imagen, bg="slate gray")#.place(x=0,y=0)	
#logo.pack()
logo.grid(row=0,column=1, padx=2, pady=2)

#frame para el punto debil
miFrame=Frame(raiz, width=1200, height=600 )#construimos un frame y o asignamos a la raiz
#miFrame.pack()
miFrame.grid(row=1,column=0, sticky="e", padx=2, pady=2, columnspan=5)
#miFrame.config(width=1200, height=600)
miFrame.config(bg="orange")#le damos un color al frame
miFrame.config(bd=40)#le damos un grosor al borde
miFrame.config(cursor="hand2")#cuando el cursor se ubica cambia la forma en este caso a una mano

#frame para el calculo de Rangos de Tensión
'''
miRangotesion=Frame(raiz)#construimos un frame y o asignamos a la raiz
miRangotesion.pack()
#miRangotesion.config(width="600", height="300")
miRangotesion.config(bg="orange")#le damos un color al frame
miRangotesion.config(bd=40)#le damos un grosor al borde
miRangotesion.config(cursor="hand2")#cuando el cursor se ubica cambia la forma en este caso a una mano
'''

#configuramos la etiqueta y el cuadro donde se ingresa el texto para el cable#


numeroCable=StringVar()

cableLabel=Label(miFrame, text="Seleccione el tipo de cable:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
cableLabel.grid(row=0,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroCable=Entry(miFrame, textvariable=numeroCable, width=3)
#cuadroTexto.place(x=30,y=50)
cuadroCable.grid(row=0,column=1, padx=2, pady=2)
cuadroCable.config(background="black", fg="#03f943", justify="center", font=('Arial', 14))

#-----Pulsaciones teclado para obtener el cable------------- 

def numeroPulsado(num):

	numeroCable.set(num)


# menu de selección de cable
boton1=Button(miFrame, text="1.", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=0,column=2, sticky="e", padx=10, pady=2) 
cableLabel=Label(miFrame, text="1. Si es Rochester 1H314K - 5/16in", bg="orange", fg="white", font=('Arial', 12))
cableLabel.grid(row=0,column=3, sticky="w", padx=2, pady=2)

boton2=Button(miFrame, text="2.", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=1,column=2, sticky="e", padx=10, pady=2) 
cableLabel=Label(miFrame, text="2. Si es Camesa 1N32PTZ - 5/16 in", bg="orange", fg="white", font=('Arial', 12))
cableLabel.grid(row=1,column=3, sticky="w", padx=2, pady=2)

boton3=Button(miFrame, text="3.", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=2,column=2, sticky="e", padx=10, pady=2) 
cableLabel=Label(miFrame, text="3. Si es Rochester 1H220A - 7/32in", bg="orange", fg="white", font=('Arial', 12))
cableLabel.grid(row=2,column=3, sticky="w", padx=2, pady=2)

boton4=Button(miFrame, text="4.", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=2, sticky="e", padx=10, pady=2) 
cableLabel=Label(miFrame, text="4. Si es Rochester 1H226K - 7/32", bg="orange", fg="white", font=('Arial', 12))
cableLabel.grid(row=3,column=3, sticky="w", padx=2, pady=2)






#------configuramos la etiqueta y el cuadro donde se ingresa la profundidad#---------------

profundidad=int()#definimos la varible para entar en el entry de profundidad

profundidadLabel= Label(miFrame, text="Ingrese la maxima profundidad en ft:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
profundidadLabel.grid(row=1,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroProfundidad=Entry(miFrame, textvariable=profundidad)#asignamos la vaible profundidad al Entry del cuadro de profundidad
#cuadroTexto.place(x=30,y=50)
cuadroProfundidad.grid(row=1,column=1, padx=2, pady=2, sticky="w")





#Configuramos 



'''
#configuramos la etiqueta y el cuadro donde se ingresa el texto sufuciente para comentarios#

comentariosLabel= Label(miFrame, text="comentarios:", bg="orange", fg="white")
comentariosLabel.grid(row=3,column=0, sticky="e", padx=2, pady=2)

textoComentario=Text(miFrame, width=36, height=12)
#cuadroTexto.place(x=30,y=50)
textoComentario.grid(row=3,column=1, padx=2, pady=2, sticky="w")
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=3, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

'''


#configuramos el cuadro donde imprimos el resuatdo del punto debil#

puntoDebil=StringVar()

pdLabel=Label(miFrame, text="El punto debil en lb:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
pdLabel.grid(row=5,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroPd=Entry(miFrame, textvariable=puntoDebil)
#cuadroTexto.place(x=30,y=50)
cuadroPd.grid(row=5,column=1, padx=2, pady=2, sticky="w")
#cuadroPass.config(show="*")

#configuramos el cuadro donde imprimos el resuatdo del punto de ruptura #

puntoRuptura=StringVar()

prLabel=Label(miFrame, text="El punto de ruptura en lb:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
prLabel.grid(row=6,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroPr=Entry(miFrame, textvariable=puntoRuptura)
#cuadroTexto.place(x=30,y=50)
cuadroPr.grid(row=6,column=1, padx=2, pady=2, sticky="w")
#cuadroPass.config(show="*")


#configuramos el cuadro donde imprimos el resuatdo del numero de alambres #

numeroAlambres=StringVar()

naLabel=Label(miFrame, text="No. Alambres = (Punto Débil / Punto de Ruptura Alambre):", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
naLabel.grid(row=4,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroNa=Entry(miFrame, textvariable=numeroAlambres)
#cuadroTexto.place(x=30,y=50)
cuadroNa.grid(row=4,column=1, padx=2, pady=2, sticky="w")
#cuadroPass.config(show="*")

#numero de alambre internos
numeroAinternos=StringVar()
naLabel=Label(miFrame, text="No. Alambres internos:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
naLabel.grid(row=5,column=2, sticky="w", padx=30, pady=2)
#miLabel.pack()

cuadroNa=Entry(miFrame, textvariable=numeroAinternos)
#cuadroTexto.place(x=30,y=50)
cuadroNa.grid(row=4,column=2, padx=30, pady=2, sticky="w")
#cuadroPass.config(show="*")

#numero de alambre externos
numeroAexternos=StringVar()
naLabel=Label(miFrame, text="No. Alambres externos:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
naLabel.grid(row=5,column=3, sticky="w", padx=2, pady=2)
#miLabel.pack()

cuadroNa=Entry(miFrame, textvariable=numeroAexternos)
#cuadroTexto.place(x=30,y=50)
cuadroNa.grid(row=4,column=3, padx=2, pady=2, sticky="w")
#cuadroPass.config(show="*")



#configuramos un boton para calcular el punto debil
def calPdebil():
	
   
	tc=int(cuadroCable.get())
	mp=float(cuadroProfundidad.get())

	print(tc)
	print(mp)
	pd=((especificaciones_cable[2] [tc-1])*0.5)-((especificaciones_cable[3] [tc-1]*mp)/1000)#Calculamos el punto debil
	pr=((especificaciones_cable[2] [tc-1])*0.5)#El Punto de Ruptura
	na=pd/(especificaciones_cable[4] [tc-1])#Calculamos el numero de alambres
	print(pd)
	print(pr)
	print(na)
	puntoDebil.set(pd)
	puntoRuptura.set(pr)
	numeroAlambres.set(round(na))
	numeroAinternos.set(3)
	numeroAexternos.set(round(na-3))

   
botoncalPdebil=Button(raiz, text="Calcular punto debil", command=calPdebil)
botoncalPdebil.grid(row=2,column=0, sticky="e", padx=2, pady=2)
#botoncalPdebil.pack(side = LEFT, expand = True)

#-------configuramos la etiqueta y el cuadro donde se ingresa la presión en cabeza#---------------

pcabeza=StringVar()#definimos la varible para entar en el entry de profundidad

presionLabel=Label(miFrame, text="Ingrese la presión en cabeza de pozo en psi:", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
presionLabel.grid(row=2,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroPresion=Entry(miFrame, textvariable=pcabeza)
#cuadroTexto.place(x=30,y=50)
cuadroPresion.grid(row=2,column=1, padx=2, pady=2, sticky="w")


#-------Configuramos la etiqueta y el cuadro donde se ingresa el peso de la herramienta---------------

pherramienta=StringVar()#definimos la varible para entar en el entry de profundidad

pesohLabel=Label(miFrame, text="Ingrese el peso de la herramineta en lb", bg="orange", fg="white", font=('Arial', 12))
#miLabel.place(x=30, y=20)
pesohLabel.grid(row=3,column=0, sticky="e", padx=2, pady=2)
#miLabel.pack()

cuadroPesoh=Entry(miFrame, textvariable=pherramienta)
#cuadroTexto.place(x=30,y=50)
cuadroPesoh.grid(row=3,column=1, padx=2, pady=2, sticky="w")


#-------------------Configuaramos los radio Button

varOpcion=IntVar()
varButton=IntVar()

def menu():

	
	if varOpcion.get()==1:
			print(varOpcion.get())

			#----------Configuramos la segunda parte del programa caculode tensiones

			tensionLabel= Label(miFrame, text="RANGOS DE TENSIÓN", bg="orange", fg="black", font=('Arial', 18))
			#miLabel.place(x=30, y=20)
			tensionLabel.grid(row=7,column=0, padx=2, pady=2, columnspan=4)
			#miLabel.pack()

			#--------Menu Rangos de tensión------------------------------------------------


			#configuramos la grilla donde imprimos los resultados de los rangos de tensión #

			fondoLabel=Label(miFrame, text="En fondo", bg="orange", fg="white", font=('Arial', 12))
			fondoLabel.grid(row=8,column=1, sticky="e", padx=2, pady=2)

			superficieLabel=Label(miFrame, text="En Superficie", bg="orange", fg="white", font=('Arial', 12))
			superficieLabel.grid(row=8,column=2, sticky="w", padx=30, pady=2)
				
			#-------------rango nominal--------------------------
			rNominal=StringVar()
			rangonominalLabel=Label(miFrame, text="Rango Nominal en lb:", bg="orange", fg="white", font=('Arial', 12))
			rangonominalLabel.grid(row=10,column=0, sticky="e", padx=2, pady=2)

			cuadroRangonominal=Entry(miFrame, textvariable=rNominal)
			cuadroRangonominal.grid(row=10,column=1, padx=2, pady=2, sticky="e")

			#------------------rango nominal en superficie-----------------------
			rNominalsup=StringVar()
			cuadroRangonominalsup=Entry(miFrame, textvariable=rNominalsup)
			cuadroRangonominalsup.grid(row=10,column=2, padx=30, pady=2, sticky="w")

			#-------------rango bajo--------------------------
			rBajo=StringVar()
			rangobajoLabel=Label(miFrame, text="Rango Bajo en lb:", bg="orange", fg="white", font=('Arial', 12))
			rangobajoLabel.grid(row=9,column=0, sticky="e", padx=2, pady=2)

			cuadroRangobajo=Entry(miFrame, textvariable=rBajo)
			cuadroRangobajo.grid(row=9,column=1, padx=2, pady=2, sticky="e")

			#------------------rango bajo en superficie-----------------------
			rNominalbsup=StringVar()
			cuadroRangonominalbsup=Entry(miFrame, textvariable=rNominalbsup)
			cuadroRangonominalbsup.grid(row=9,column=2, padx=30, pady=2, sticky="w")

			#-------------rango Alto--------------------------
			rAlto=StringVar()
			rangoaltoLabel=Label(miFrame, text="Rango Alto en lb:", bg="orange", fg="white", font=('Arial', 12))
			rangoaltoLabel.grid(row=11,column=0, sticky="e", padx=2, pady=2)

			cuadroRangoalto=Entry(miFrame, textvariable=rAlto)
			cuadroRangoalto.grid(row=11,column=1, padx=2, pady=2, sticky="e")

			#------------------rango bajo en superficie-----------------------
			rAltosup=StringVar()
			cuadroRangonominalbsup=Entry(miFrame, textvariable=rAltosup)
			cuadroRangonominalbsup.grid(row=11,column=2, padx=30, pady=2, sticky="w")

			#configuramos un boton para calcular el punto debil
			def calRtension():
				
			   
				tc=int(cuadroCable.get())
				mp=float(cuadroProfundidad.get())
				ph=float(cuadroPesoh.get())

				pd=((especificaciones_cable[2] [tc-1])*0.5)-((especificaciones_cable[3] [tc-1]*mp)/1000)#Calculamos el punto debil
				na=pd/(especificaciones_cable[4] [tc-1])#Calculamos el numero de alambres
				rangonominal=(especificaciones_cable[4] [tc-1])*round(na)*0.92
				tensionnormal=((especificaciones_cable[3] [tc-1]*mp)/1000)+ph
				rns=(rangonominal+tensionnormal)
				rb=rangonominal*0.85
				rbs=rb+tensionnormal
				ra=rangonominal*1.15
				ras=ra+tensionnormal
				
				print(pd)
				print(na)
				print(rangonominal)
				print(tensionnormal)
				print(rns)
				print(rb)
				print(rbs)
				print(ra)
				print(ras)

				rNominal.set(round(rangonominal,3))
				rNominalsup.set(round(rns,3))
				rBajo.set(round(rb,3))
				rNominalbsup.set(round(rbs,3))
				rAlto.set(round(ra,3))
				rAltosup.set(round(ras,3)) 
				
			botonRangostension=Button(raiz, text="Calcular rangos de tensión", command=calRtension)
			botonRangostension.grid(row=2,column=1, padx=2, pady=2)
			#botonRangostension.pack(side = LEFT, expand = True)

	elif varOpcion.get()==2:
		# Ejecutamos la tercera parte del programa Etiqueta para el maximo jalon seguro
		jalonLabel= Label(miFrame, text="CALCULO MÁXIMO JALÓN SEGURO EN SUPERFICIE", bg="orange", fg="black", font=('Arial', 16))
		#miLabel.place(x=30, y=20)
		jalonLabel.grid(row=12,column=0, padx=2, pady=2)


		mSj=StringVar()
		mjsLabel=Label(miFrame, text="El MSJ en lb:", bg="orange", fg="white", font=('Arial', 12))
		mjsLabel.grid(row=12,column=1, sticky="e", padx=2, pady=2)

		cuadroMsj=Entry(miFrame, textvariable=mSj)
		cuadroMsj.grid(row=12,column=2, padx=30, pady=2, sticky="w")

		#configuramos un boton para calcular el maximo jalon seguro

		def calMjalon():
			
		   
			tc=int(cuadroCable.get())
			mp=float(cuadroProfundidad.get())
			ph=float(cuadroPesoh.get())

			pd=((especificaciones_cable[2] [tc-1])*0.5)-((especificaciones_cable[3] [tc-1]*mp)/1000)#Calculamos el punto debil
			na=pd/(especificaciones_cable[4] [tc-1])#Calculamos el numero de alambres
			rangonominal=(especificaciones_cable[4] [tc-1])*round(na)*0.92
			tensionnormal=((especificaciones_cable[3] [tc-1]*mp)/1000)+ph
			
			rb=rangonominal*0.85
			msj=tensionnormal+rb*0.75-ph
			
			
			print(rangonominal)
			print(tensionnormal)
			print(rb)
			print(msj)
			
			mSj.set(round(msj,3))
			
		botonMsj=Button(raiz, text="Calcular el máximo jalon seguro", command=calMjalon)
		botonMsj.grid(row=2,column=2, sticky="w", padx=2, pady=2)
		#botonMsj.pack(side = LEFT, expand = True)
	else: 
		print (varOpcion.get())
		#---------------- Ejecutamos la cuarta parte del programa Etiqueta para el maximo jalon seguro----------------

		pesoLabel= Label(miFrame, text="CALCULO PESO MINIMO DE LA HERRAMIENTA", bg="orange", fg="black", font=('Arial', 16))
		#miLabel.place(x=30, y=20)
		pesoLabel.grid(row=14,column=0, padx=2, pady=2, sticky="e")

		#---------------------
			
		pMh=StringVar()
		pMhLabel=Label(miFrame, text="PMH en lb:", bg="orange", fg="white", font=('Arial', 12))
		pMhLabel.grid(row=14,column=1, sticky="e", padx=2, pady=2)

		cuadropMh=Entry(miFrame, textvariable=pMh)
		cuadropMh.grid(row=14,column=2, padx=30, pady=2, sticky="w")

		#configuramos un boton para calcular el maximo jalon seguro

		def calPmherramienta():
			
		   
			pp=float(cuadroPresion.get())
			tc=int(cuadroCable.get())

			pmh=(((especificaciones_cable[1] [tc-1])**2*pi)/4)*pp+50#Calculamos el punto debil
			
			print(pp)
			print(tc)
			print(pmh)
			
			pMh.set(round(pmh,3))
			
		botonPmh=Button(raiz, text="Calcular el peso Minimo de la herramienta", command=calPmherramienta)
		botonPmh.grid(row=2,column=3, sticky="w", padx=2, pady=2)
		#botonMsj.pack(side = LEFT, expand = True)

#------Radio buton para la opción de rangos de tensión---------------------------------#

opcionTension=Radiobutton(miFrame, text="Calcular rangos de tensión", variable=varOpcion, value=1, command=menu, bg="orange", fg="black", font=('Arial', 14))
opcionTension.deselect()
opcionTension.grid(row=6,column=3, padx=2, pady=2, sticky="w")

#------Radio buton para la opción de rangos de tensión---------------------------------#

opcionMsj=Radiobutton(miFrame, text="Calcular el máximo jalon seguro", variable=varOpcion, value=2, command=menu, bg="orange", fg="black", font=('Arial', 14))
opcionMsj.deselect()
opcionMsj.grid(row=7,column=3, padx=2, pady=2, sticky="w")

#------Radio buton para la opción de rangos de tensión---------------------------------#
opcionPherramienta=Radiobutton(miFrame, text="Calcular el peso de la herramienta", variable=varOpcion, value=3, command=menu, bg="orange", fg="black", font=('Arial', 14))
opcionPherramienta.grid(row=8, column=3, padx=2, pady=2, sticky="w")

#---------------------Realizamos el boton para abrir otra ventana---------#

botonNv=Button(raiz, text="Tensiones Vs Profundidad", command=abrirventana2)
botonNv.grid(row=0,column=4, sticky="w", padx=2, pady=2)



raiz.mainloop()
