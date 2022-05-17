from tkinter import *

root=Tk()

miFrame = Frame(root, width=700, height=500)

miFrame.pack()

#------------------Nombre Item------------------------#
textoItem=Label(miFrame, text='Nombre Item:')
textoItem.grid(row=0, column=0, padx=5, pady=2)

cuadroItem=Entry(miFrame)
cuadroItem.grid(row=1, column=0, padx=5, pady=2)



#------------------Link Item------------------------#
textoLink=Label(miFrame, text='Link:')
textoLink.grid(row=0, column=1, padx=5, pady=2)

cuadroLink=Entry(miFrame)
cuadroLink.grid(row=1, column=1, padx=5, pady=2)



#------------------Precio Item------------------------#
textoPrecio=Label(miFrame, text='Precio alarma:')
textoPrecio.grid(row=0, column=2, padx=5, pady=2)

cuadroLink=Entry(miFrame)
cuadroLink.grid(row=1, column=2, padx=5, pady=2)


#------------------Boton suma item--------------------#
botonSumar=Button(miFrame, text='+')
botonSumar.grid(row=1, column=3, padx=5, pady=2)


#------------------Delay entre items------------------#
delayItem=Label(miFrame, text='Delay entre busquedas:')
delayItem.grid(row=0, column=4, padx=5, pady=2)

cuadroDelayItem=Entry(miFrame)
cuadroDelayItem.grid(row=1, column=4, padx=5, pady=2)


#-------------Frecuencia entre registros--------------#
frecuenciaRegistro=Label(miFrame, text='Frecuencia entre registros:')
frecuenciaRegistro.grid(row=2, column=4, padx=5, pady=2)

cuadrofrecuenciaRegistro=Entry(miFrame)
cuadrofrecuenciaRegistro.grid(row=3, column=4, padx=5, pady=2)


#-------------Items sumados--------------#
itemSumado1=Label(miFrame, text='Item1')
itemSumado1.grid(row=2, column=0, padx=5, pady=2)

itemSumado2=Label(miFrame, text='Item2')
itemSumado2.grid(row=3, column=0, padx=5, pady=2)

itemSumado3=Label(miFrame, text='Item3')
itemSumado3.grid(row=4, column=0, padx=5, pady=2)

itemSumado4=Label(miFrame, text='Item4')
itemSumado4.grid(row=5, column=0, padx=5, pady=2)


#-------------Botones a eliminar--------------#
botonEliminar1=Button(miFrame, text='-')
botonEliminar1.grid(row=2, column=3, padx=5, pady=2)

botonEliminar2=Button(miFrame, text='-')
botonEliminar2.grid(row=3, column=3, padx=5, pady=2)

botonEliminar3=Button(miFrame, text='-')
botonEliminar3.grid(row=4, column=3, padx=5, pady=2)

botonEliminar4=Button(miFrame, text='-')
botonEliminar4.grid(row=5, column=3, padx=5, pady=2)



#-------------Textos a ignorar--------------#
textoIgnorar=Label(miFrame, text='Textos a ignorar:')
textoIgnorar.grid(row=7, column=0, padx=5, pady=2)

cuadroIgnorar=Text(miFrame, width=16, height=5)
cuadroIgnorar.grid(row=8, column=0, padx=5, pady=2)


#-------------ID Discord--------------#
textoIdDiscord=Label(miFrame, text='ID Discord:')
textoIdDiscord.grid(row=6, column=2, padx=5, pady=2)

cuadroIgnorar=Entry(miFrame)
cuadroIgnorar.grid(row=7, column=2, padx=5, pady=2, sticky='n')


#-------------Auth Discord--------------#
textoAuthDiscord=Label(miFrame, text='Authorization Discord:')
textoAuthDiscord.grid(row=8, column=2, padx=5, pady=2, sticky='n')

cuadroAuthDiscord=Entry(miFrame)
cuadroAuthDiscord.grid(row=8, column=2, padx=5, pady=2, sticky='')


#------------------Boton Iniciar--------------------#
botonIniciar=Button(miFrame, text='Iniciar')
botonIniciar.grid(row=7, column=4, padx=5, pady=2)


#------------------Boton Iniciar--------------------#
botonDetener=Button(miFrame, text='Detener')
botonDetener.grid(row=8, column=4, padx=5, pady=2)







root.mainloop()