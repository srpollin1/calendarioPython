from tkinter import *
from tkinter import messagebox
import webbrowser

window = Tk()
window.title("calendario")
window.geometry('1237x94')
window.configure(background="black")
def lunes():
    messagebox.showinfo('Lunes', 'usted entra a las 13:46\n \nIngles Intermedio 1 a las 13:46 hasta 15:15 \n \nProgramacion de base datos a las 15:16 hasta 17:30')
btn = Button(window,text='Lunes', bg="black", fg="medium spring green", font=("Arial Bold", 35),command=lunes)
btn.grid(column=0,row=0)

def martes():
    messagebox.showinfo('Martes', 'usted entra a las 13:46\n \nEstadistica 1 a las 13:46 hasta 15:15 \n \nIngeniería de software a las 15:16 hasta 16:45')
btn = Button(window,text='Martes', bg="black", fg="medium spring green", font=("Arial Bold", 35),command=martes)
btn.grid(column=1,row=0)

def miercoles():
    messagebox.showinfo('Miercoles','usted entra a las 14:31\n \nEtica a las 14:31 hasta 16:00 \n \nDesarrollo de software a las 16:01 hasta 18:15')
btn = Button(window,text='Miercoles', bg="black", fg="medium spring green", font=("Arial Bold", 35),command=miercoles)
btn.grid(column=2,row=0)

def jueves():
    messagebox.showinfo('Jueves','usted entra a las 13:46\n \nProgramación de base de datos a las 13:46 hasta 15:15 \n \nDesarrollo software a las 15:16 hasta 16:45 \n \nIngeniería de software 16:46 hasta 18:15')
btn = Button(window,text='Jueves', bg="black", fg="medium spring green", font=("Arial Bold", 35),command=jueves)
btn.grid(column=3,row=0)

def viernes():
    messagebox.showinfo('Viernes','usted entra a las 13:46\n \nEstadistica 1 a las 13:46 hasta 15:15 \n \nIngles intermedio 1 a las 15:16 hasta 16:46')
btn = Button(window,text='Viernes', bg="black", fg="medium spring green", font=("Arial Bold", 35),command=viernes)
btn.grid(column=4,row=0)
def asistencia():
    webbrowser.open_new(r"https://drive.google.com/drive/u/3/my-drive")
btn = Button(window, text="Drive",  bg="black", fg="medium spring green", font=("Arial Bold", 35),command=asistencia)
btn.grid(column=5, row=0)
window.mainloop()
