from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as st 
import tkinter as tk

Stickbot = Tk()  # creates a tkinter object (GUI)
Stickbot.title("Stick-Bot Interactive Interface") # the title of the program/GUI


#Stickbot.geometry("600x400")


# The main tital of the display screen
Stickbot_title = Label(Stickbot, text="Stick Bot", width=60, borderwidth=5)
Stickbot_title.grid(row=0, column = 0, columnspan=8, padx= 10, pady=10)
Stickbot_title.config(bg='lightgreen')

def buttons_random():
    return "What is your name"

def exit_button():
    Stickbot.destroy()

def showMessage():  
    messagebox.showinfo('Confirmation', 'Deatil for chosen is displayed')

def exitMessage():  
    messagebox.showinfo('Thank You!', 'Thanks for using Stick-bot')


# Creating variable's buttons.

button_CO2 = Button(Stickbot, text="CO2 Level", padx=10, pady=10, command=lambda:[showMessage(), buttons_random()]).grid(row=1, column=0, columnspan=2)
button_Temperature = Button(Stickbot, text="Temperature Level", padx=10, pady=10, command=lambda:[showMessage(), buttons_random()]).grid(row=2, column=0, columnspan=2)
button_PHlevel = Button(Stickbot, text="PH Level", padx=10, pady=10, command=lambda:[showMessage(), buttons_random()]).grid(row=3, column=0, columnspan=2)
button_Oxygen = Button(Stickbot, text="Oxygen", padx=10, pady=10, command=lambda:[showMessage(), buttons_random()]).grid(row=4, column=0, columnspan=2)
button_Wipedata = Button(Stickbot, text="Wipe Data", padx=10, pady=10, command=lambda:[showMessage(), buttons_random()]).grid(row=5, column=0, columnspan=2)
button_Exit = Button(Stickbot, text="EXIT", padx=10, pady=10, command=lambda:[exitMessage(), exit_button()]).grid(row=6, column=0, columnspan=2)

# font detail for text.
Font_tuple = ("Comic Sans MS", 20, "bold")

 
# update error log space

# Creating scrolled text area widget with Read only by disabling the state.

updateErrorLog = st.ScrolledText(Stickbot, width = 30, height = 8, font = ("Times New Roman", 15)) 
  
updateErrorLog.grid(row=1, column = 3, columnspan=2, rowspan=5,  pady = 10, padx = 10) 
  
# Inserting Text which is read only 
updateErrorLog.insert(tk.INSERT, 
""" 
All the Errors & Updates are listed here. 
Hi 
Error one == nothing LOL 
Error two == nothing LOL
Error three == nothing LOL
Error four == nothing LOL
Error five == nothing LOL
Error six == nothing LOL
Error seven == nothing LOL
""") 
  
# Making the Log read only 
updateErrorLog.configure(state ='disabled')

# graph location
graphLocation = Message(Stickbot, text="Graph Health ")
graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)
graphLocation.config(bg='lightgreen')
graphLocation.configure(font=Font_tuple)

# Crop health location
cropHeath = 40
style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='green')

bar = Progressbar(Stickbot, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = cropHeath

bar.grid(column=5, row=4, rowspan=2)








Stickbot.mainloop()
