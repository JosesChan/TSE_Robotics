import tkinter as tk
import time
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tkinter.scrolledtext as st
from time import strftime
import tkinter

import matplotlib.pyplot as plt


#LARGEFONT = ("Comic Sans MS", 30, "bold")
mediumfont = ("Comic Sans MS", 20, "bold")
smallfont = ("Comic Sans MS", 15, "bold")

cropHeath = 40
c02_score = None
temperature_score = None
ph_score = None
oxygen_score = None


def c02(): # This checks all the imported values against the correct mesuerments to make sure they are in the bounds stated and creates 1 part of the score for the overall crop health graph. 
 
  global c02_score
  c02_score = 0 # Overall c02 score. 
  c02_input = 1200, 1100, 1000, 1000, 2000, 5, 76, 3, 54, 3, 45, 2, 4, 2, 43, 2, 70, 8,19, 20 # To be replaced with the imported variable name. 

  for x in c02_input:
   if x <= 1300 and x >= 1000:
     print ("Green")
     c02_score += 1

   elif x > 1310 and x < 1001:
      print ("Red")

   else:
     print ("Red")
 

  if c02_score == 24:
    c02_score += 1



def c02chart(): # Creates the graph to show all of the readings taken over the last stated time period.


 c02x = 2, 3, 4, 5, 6, 7, 8, 9, 1 # To be replaced with the imported variable name. 
 c02y = 5, 3, 2, 5, 6, 7, 8, 9, 2 # To be replaced with the imported variable name. 
 xpoints = c02x
 ypoints = c02y

 plt.plot(xpoints, ypoints, 'o')

 plt.xlabel("Time")
 plt.ylabel("Measurement (PPM)")
 plt.title("C02 graph")
 plt.show()

def temperature(): # This checks all the imported values against the correct mesuerments to make sure they are in the bounds stated and creates 1 part of the score for the overall crop health grawater. 
 
  global temperature_score
  temperature_score = 0 # Overall water score. 
  temperature_input = 1200, 1100, 1000, 1000, 2000, 5, 76, 3, 54, 3, 45, 2, 4, 2, 43, 2, 70, 8,19, 20 # To be replaced with the imported variable name. 

  for x in temperature_input:
   if x <= 78 and x >= 70:
     print ("Green")
     temperature_score += 1

   elif x > 78 and x < 70:
      print ("Red")

   else:
     print ("Red")
 

  if temperature_score == 24:
    temperature_score += 1
  


def temperaturechart(): # Creates the grawater to show all of the readings taken over the last stated time period.

 import matplotlib.pyplot as plt

 temperaturex = 2, 3, 4, 5, 6, 7, 8, 9, 1 # To be replaced with the imported variable name. 
 temperaturey = 5, 3, 2, 5, 6, 7, 8, 9, 2 # To be replaced with the imported variable name. 
 xpoints = temperaturex
 ypoints = temperaturey

 plt.plot(xpoints, ypoints, 'o')

 plt.xlabel("Time")
 plt.ylabel("Measurement (PPH)")
 plt.title("Temperature graph")
 plt.show()

temperature() # Calls the water function.
print("temperature score = ", temperature_score, "/ 25") # Displays the water score out of 25.

def ph(): # This checks all the imported values against the correct mesuerments to make sure they are in the bounds stated and creates 1 part of the score for the overall crop health graph. 
 
  global ph_score
  ph_score = 0 # Overall ph score. 
  ph_input = 1200, 1100, 1000, 1000, 2000, 5, 76, 3, 54, 3, 45, 2, 4, 2, 43, 2, 70, 8,19, 20 # To be replaced with the imported variable name. 

  for x in ph_input:
   if x <= 8.3 and x >= 5.5:
     print ("Green")
     ph_score += 1

   elif x > 8.4 and x < 5.5:
      print ("Red")

   else:
     print ("Red")
 

  if ph_score == 24:
    ph_score += 1
  


def phchart(): # Creates the graph to show all of the readings taken over the last stated time period.

 import matplotlib.pyplot as plt

 phx = 2, 3, 4, 5, 6, 7, 8, 9, 1 # To be replaced with the imported variable name. 
 phy = 5, 3, 2, 5, 6, 7, 8, 9, 2 # To be replaced with the imported variable name. 
 xpoints = phx
 ypoints = phy

 plt.plot(xpoints, ypoints, 'o')

 plt.xlabel("Time")
 plt.ylabel("Measurement (PH)")
 plt.title("PH graph")
 plt.show()

ph() # Calls the ph function.
print("PH score = ", ph_score, "/ 25") # Displays the ph score out of 25.

def oxygen(): # This checks all the imported values against the correct mesuerments to make sure they are in the bounds stated and creates 1 part of the score for the overall crop health graph oxygen. 
 
  global oxygen_score
  oxygen_score = 0 # Overall oxgen score. 
  oxygen_input = 1200, 1100, 1000, 1000, 2000, 5, 76, 3, 54, 3, 45, 2, 4, 2, 43, 2, 70, 8,19, 20 # To be replaced with the imported variable name. 

  for x in oxygen_input:
   if x <= 6 and x >= 5:
     print ("Green")
     oxygen_score += 1

   elif x > 6.1 and x < 4.9:
      print ("Red")

   else:
     print ("Red")
 

  if oxygen_score == 24:
    oxygen_score += 1
  


def oxygenchart(): # Creates the graph oxygen to show all of the readings taken over the last stated time period.

 import matplotlib.pyplot as plt

 oxygenx = 2, 3, 4, 5, 6, 7, 8, 9, 1 # To be replaced with the imported variable name. 
 oxygeny = 5, 3, 2, 5, 6, 7, 8, 9, 2 # To be replaced with the imported variable name. 
 xpoints = oxygenx
 ypoints = oxygeny

 plt.plot(xpoints, ypoints, 'o')

 plt.xlabel("Time")
 plt.ylabel("Measurement (MG/L)")
 plt.title("OXYGEN graph")
 plt.show()

oxygen() # Calls the oxgen function.
print("OXYGEN score = ", oxygen_score, "/ 25") # Displays the oxygen score out of 25.


class Stickbot(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Mainpage, CO2, Temperature, PH, Oxygen):
            frame = F(container, self)

            # initializing frame of that object from
            # Mainpage  and so on respectively with
            # for loop

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.change_frame(Mainpage)

    # to display the current frame passed as
    # parameter
    def change_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame Mainpage

class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        style = ttk.Style()

        style.theme_use('default')

        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="         Stick Bot - Main Menu", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_CO2 = ttk.Button(self, text="CO2 Level",
                                command=lambda: controller.change_frame(CO2))
        button_CO2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button_Temperature = ttk.Button(self, text="Temperature Level",
                                        command=lambda: controller.change_frame(Temperature))
        button_Temperature.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_PHLevel = ttk.Button(self, text="PH Level",
                                    command=lambda: controller.change_frame(PH))
        button_PHLevel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button_Oxygen = ttk.Button(self, text="Oxygen Level",
                                   command=lambda: controller.change_frame(Oxygen))
        button_Oxygen.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_exit = ttk.Button(self, text="EXIT",
                                 command=self.close)
        button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Crop health
        crophealth_title = Label(self, text='''Crop's overall health''', font=smallfont, foreground='black',
                                 background='cyan')
        crophealth_title.grid(row=4, column=5)
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='green')

        progress_Bar = Progressbar(self, length=200, style='black.Horizontal.TProgressbar')

        progress_Bar['value'] = cropHeath

        progress_Bar.grid(row=4, column=5, rowspan=2)

        healthdigit = str(cropHeath) + "/100"

        healthintext = Label(self, text=healthdigit, foreground="black", borderwidth=2,
                             font=smallfont, relief='flat')
        healthintext.grid(row=5, column=5)

        # Clock widget

        self.current_Time = ''
        self.current_time2 = "Current Time: " + time.strftime('%H:%M:%S')

        self.clock = Label(self, text=self.current_time2, font=mediumfont, background='cyan', foreground='black')

        self.clock.grid(row=2,column=5)

        self.clock_Tick() #after the first call, the function itself calls intself every 200 milisecond to referesh the time
    
    def clock_Tick(self): 
        self.current_time2 = "Current Time: " + time.strftime('%H:%M:%S')
        self.clock.configure(text=self.current_time2)
        self.clock.after(200, self.clock_Tick) 

    def close(self):
        self.master.quit()


# window frame for CO2 stats 

class CO2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="       Carbon Dioxide - Stats", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_mainmenu = ttk.Button(self, text="Main Menu",
                                     command=lambda: controller.change_frame(Mainpage))
        button_mainmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button_Temperature = ttk.Button(self, text="Temperature Level",
                                        command=lambda: controller.change_frame(Temperature))
        button_Temperature.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_PHLevel = ttk.Button(self, text="PH Level",
                                    command=lambda: controller.change_frame(PH))
        button_PHLevel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button_Oxygen = ttk.Button(self, text="Oxygen Level",
                                   command=lambda: controller.change_frame(Oxygen))
        button_Oxygen.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_exit = ttk.Button(self, text="EXIT",
                                 command=self.close)
        button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        updateErrorLog = st.ScrolledText(self, width=30, height=8, font=("Times New Roman", 15))

        updateErrorLog.grid(row=1, column=3, columnspan=2, rowspan=5, pady=10, padx=10)

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
        updateErrorLog.configure(state='disabled')

       # graph location
        graphLocation = Button(self, text="Graph Health ", command=lambda:[c02(), c02chart()])
        graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)


    def close(self):
        self.master.quit()
    

    


# window frame for Temperature stats 

class Temperature(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="       Temperature - Stats", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_mainmenu = ttk.Button(self, text="CO2 Level",
                                     command=lambda: controller.change_frame(CO2))
        button_mainmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button_Temperature = ttk.Button(self, text="Main Menu",
                                        command=lambda: controller.change_frame(Mainpage))
        button_Temperature.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_PHLevel = ttk.Button(self, text="PH Level",
                                    command=lambda: controller.change_frame(PH))
        button_PHLevel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button_Oxygen = ttk.Button(self, text="Oxygen Level",
                                   command=lambda: controller.change_frame(Oxygen))
        button_Oxygen.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_exit = ttk.Button(self, text="EXIT",
                                 command=self.close)
        button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        updateErrorLog = st.ScrolledText(self, width=30, height=8, font=("Times New Roman", 15))

        updateErrorLog.grid(row=1, column=3, columnspan=2, rowspan=5, pady=10, padx=10)

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
        updateErrorLog.configure(state='disabled')

       # graph location
        graphLocation = Button(self, text="Graph Health ", command=lambda:[temperature(), temperaturechart()])
        graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# window frame for PH stats 

class PH(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="       PH - Stats", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_mainmenu = ttk.Button(self, text="CO2 Level",
                                     command=lambda: controller.change_frame(CO2))
        button_mainmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button_Temperature = ttk.Button(self, text="Temperature Level",
                                        command=lambda: controller.change_frame(Temperature))
        button_Temperature.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_PHLevel = ttk.Button(self, text="Main Menu",
                                    command=lambda: controller.change_frame(Mainpage))
        button_PHLevel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button_Oxygen = ttk.Button(self, text="Oxygen Level",
                                   command=lambda: controller.change_frame(Oxygen))
        button_Oxygen.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_exit = ttk.Button(self, text="EXIT",
                                 command=self.close)
        button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        updateErrorLog = st.ScrolledText(self, width=30, height=8, font=("Times New Roman", 15))

        updateErrorLog.grid(row=1, column=3, columnspan=2, rowspan=5, pady=10, padx=10)

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
        updateErrorLog.configure(state='disabled')

        # graph location
        graphLocation = Button(self, text="Graph Health ", command=lambda:[ph(), phchart()])
        graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# window frame for Oxygen stats 

class Oxygen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="       Oxygen - Stats", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_mainmenu = ttk.Button(self, text="CO2 Level",
                                     command=lambda: controller.change_frame(CO2))
        button_mainmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button_Temperature = ttk.Button(self, text="Temperature Level",
                                        command=lambda: controller.change_frame(Temperature))
        button_Temperature.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_PHLevel = ttk.Button(self, text="PH Level",
                                    command=lambda: controller.change_frame(PH))
        button_PHLevel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button_Oxygen = ttk.Button(self, text="Main Menu",
                                   command=lambda: controller.change_frame(Mainpage))
        button_Oxygen.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_exit = ttk.Button(self, text="EXIT",
                                 command=self.close)
        button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        updateErrorLog = st.ScrolledText(self, width=30, height=8, font=("Times New Roman", 15))

        updateErrorLog.grid(row=1, column=3, columnspan=2, rowspan=5, pady=10, padx=10)

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
        updateErrorLog.configure(state='disabled')


        # graph location
        graphLocation = Button(self, text="Graph Health ", command=lambda:[oxygen(), oxygenchart()])
        graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)


    def close(self):
        self.master.quit()


# Driver Code
application = Stickbot()
application.title("Stick-Bot Interactive Interface")
application.mainloop()
