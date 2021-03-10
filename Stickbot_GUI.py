from tkinter import *


Stickbot = Tk()  # creates a tkinter object (GUI)
Stickbot.title("Stick-Bot Interactive Interface") # the title of the program/GUI

#Stickbot.geometry("600x400")# this can be used to change the screen resoultion of the GUI.
#Stickbot.config(bg='red')


# The main tital of the display screen
Stickbot_title = Label(Stickbot, text="Stick Bot", width=50, borderwidth=5)
Stickbot_title.grid(row=0, column = 0, columnspan=8, padx= 10, pady=10)
Stickbot_title.config(bg='lightgreen')

def buttons_random():
    return 0
    

# Creating variable's buttons.

button_CO2 = Button(Stickbot, text="CO2 Level", padx=10, pady=10, command=buttons_random).grid(row=1, column=0, columnspan=2)
button_Temperature = Button(Stickbot, text="Temperature Level", padx=10, pady=10, command=buttons_random).grid(row=2, column=0, columnspan=2)
button_PHlevel = Button(Stickbot, text="PH Level", padx=10, pady=10, command=buttons_random).grid(row=3, column=0, columnspan=2)
button_Oxygen = Button(Stickbot, text="Oxygen", padx=10, pady=10, command=buttons_random).grid(row=4, column=0, columnspan=2)
button_Wipedata = Button(Stickbot, text="Wipe Data", padx=10, pady=10, command=buttons_random).grid(row=5, column=0, columnspan=2)
button_Exit = Button(Stickbot, text="EXIT", padx=10, pady=10, command=buttons_random).grid(row=6, column=0, columnspan=2)

# font detail for text.
Font_tuple = ("Comic Sans MS", 20, "bold")
 
# update error log space
updateErrorLog = Message(Stickbot, text="Updates and Error log")
updateErrorLog.grid(row=1, column=3, columnspan=2, rowspan=5)
updateErrorLog.config(bg='lightgreen')
updateErrorLog.configure(font=Font_tuple)

# graph location
updateErrorLog = Message(Stickbot, text="Graph goes here")
updateErrorLog.grid(row=1, column=5, columnspan=4, rowspan=3)
updateErrorLog.config(bg='lightgreen')
updateErrorLog.configure(font=Font_tuple)

# Crop health location
updateErrorLog = Message(Stickbot, text="CROP HEALTH")
updateErrorLog.grid(row=4, column=5, columnspan=4, rowspan=2)
updateErrorLog.config(bg='lightgreen')
updateErrorLog.configure(font=Font_tuple)










Stickbot.mainloop()