from tkinter import *
from math import *

#Ventana
ventana =Tk()
ventana.title("Calculadora")
ventana.geometry("392x600")
ventana.configure(background="gray")

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) #VISUALIZAR LA OPERACION EN LA PANTALLA
    
def clear():
    global operador
    operador=("")
    input_text.set("Hola Juanito")

def operacion():
    global operador
    try:
        opera=str(eval(operador))#REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#MUESTRA EL RESULTADO

ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
clear()
B=Button

#Botones
B(ventana,text="0",width=ancho_boton,height=alto_boton,command= lambda:btnClik(0)).place(x=107,y=480)
B(ventana,text="1",width=ancho_boton,height=alto_boton,command= lambda:btnClik(1)).place(x=17,y=420)
B(ventana,text="2",width=ancho_boton,height=alto_boton,command= lambda:btnClik(2)).place(x=107,y=420)
B(ventana,text="3",width=ancho_boton,height=alto_boton,command= lambda:btnClik(3)).place(x=197,y=420)
B(ventana,text="4",width=ancho_boton,height=alto_boton,command= lambda:btnClik(4)).place(x=17,y=360)
B(ventana,text="5",width=ancho_boton,height=alto_boton,command= lambda:btnClik(5)).place(x=107,y=360)
B(ventana,text="6",width=ancho_boton,height=alto_boton,command= lambda:btnClik(6)).place(x=197,y=360)
B(ventana,text="7",width=ancho_boton,height=alto_boton,command= lambda:btnClik(7)).place(x=17,y=300)
B(ventana,text="8",width=ancho_boton,height=alto_boton,command= lambda:btnClik(8)).place(x=107,y=300)
B(ventana,text="9",width=ancho_boton,height=alto_boton,command= lambda:btnClik(9)).place(x=197,y=300)
B(ventana,text="π",width=ancho_boton,height=alto_boton,command= lambda:btnClik("pi")).place(x=107,y=240)
B(ventana,text=",",width=ancho_boton,height=alto_boton,command= lambda:btnClik(".")).place(x=197,y=240)
B(ventana,text="+",width=ancho_boton,height=alto_boton,command= lambda:btnClik("+")).place(x=287,y=420)
B(ventana,text="-",width=ancho_boton,height=alto_boton,command= lambda:btnClik("-")).place(x=287,y=360)
B(ventana,text="*",width=ancho_boton,height=alto_boton,command= lambda:btnClik("*")).place(x=287,y=300)
B(ventana,text="/",width=ancho_boton,height=alto_boton,command= lambda:btnClik("/")).place(x=287,y=240)
B(ventana,text="√",width=ancho_boton,height=alto_boton,command= lambda:btnClik("//")).place(x=17,y=480)
B(ventana,text="(",width=ancho_boton,height=alto_boton,command= lambda:btnClik("(")).place(x=17,y=180)
B(ventana,text=")",width=ancho_boton,height=alto_boton,command= lambda:btnClik(")")).place(x=107,y=180)
B(ventana,text="%",width=ancho_boton,height=alto_boton,command= lambda:btnClik("%")).place(x=197,y=480)
B(ventana,text="In",width=ancho_boton,height=alto_boton,command= lambda:btnClik("log")).place(x=17,y=240)
B(ventana,text="C",width=ancho_boton,height=alto_boton,command=clear).place(x=197,y=180)
B(ventana,text="EXP",width=ancho_boton,height=alto_boton,command= lambda:btnClik("**")).place(x=287,y=180)
B(ventana,text="=",width=ancho_boton,height=alto_boton,command= operacion).place(x=287,y=480)

#Cristal
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="white",justify="right").place(x=10,y=60)


ventana.mainloop()