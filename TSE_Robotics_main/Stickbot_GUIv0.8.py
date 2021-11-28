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
import sys
import matplotlib.pyplot as plt

# LARGEFONT = ("Comic Sans MS", 30, "bold")
mediumfont = ("Comic Sans MS", 20, "bold")
smallfont = ("Comic Sans MS", 15, "bold")

cropHealth = 0
c02_score = 0
temperature_score = 0
ph_score = 0
oxygen_score = 0
fileYlist = []
timeHour_x = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
oxygenError = ""
tempError = ""
pHError = ""
co2Error = ""


# list to store values from files globally
def readfile(fileName):
    # Function that will take the file wanting to be read
    fileYlist.clear()
    file = fileName  # assign the filename to a local variable
    try:
        oFile = open(file, "r")
    except FileNotFoundError:
        print("Filename;" + file + " is not found")
        input("press any key to exit....")
        sys.exit()
    # try block to accept error of file not being found
    rFile = oFile.readlines()
    for newline in rFile:
        text_split = newline.split(",")
        for text in text_split:
            fileYlist.append(text)
    # reads the file and splits it via a comma and adds it to the global lists.
    oFile.close()


def c02():  # This checks all the imported values against the correct measurements to make sure they are
    # in the bounds stated and creates 1 part of the score for the overall crop health graph.

    global c02_score, co2Error
    c02_score = 0  # Overall c02 score.
    readfile("co2.csv")

    for x in range(len(fileYlist)):
        if 1300 >= int(fileYlist[x]) >= 1000:
            print("Green")
            c02_score += 1

        elif int(fileYlist[x]) > 1310 or int(fileYlist[x]) < 1000:
            print("Red")
            if int(fileYlist[x]) > 1310:
                co2Error = co2Error + "\n" + "co2 level is ABOVE optimal at: \n" + str(x) + ":00:00"
            elif int(fileYlist[x]) < 1000:
                co2Error = co2Error + "\n" + "co2 level is BELOW optimal at: \n" + str(x) + ":00:00"

    if c02_score == 24:
        c02_score += 1


def c02chart():  # Creates the graph to show all of the readings taken over the last stated time period.
    ypoints = []
    for x in range(len(fileYlist)):
        ypoints.append(int(fileYlist[x]))

    plt.plot(timeHour_x, ypoints, 'r--')

    plt.xlabel("Time(Hour)")
    plt.ylabel("Measurement (PPM)")
    plt.title("C02 graph")
    plt.show()


def temperature():  # This checks all the imported values against the correct measurements to make sure
    # they are in the bounds stated and creates 1 part of the score for the overall crop health graph.

    global temperature_score, tempError
    temperature_score = 0  # Overall water score.
    readfile("temperature.csv")

    for x in range(len(fileYlist)):
        if 25 >= float(fileYlist[x]) >= 21:
            print("Green")
            temperature_score += 1
        elif float(fileYlist[x]) > 25 or float(fileYlist[x]) < 21:
            print("Red")
            if float(fileYlist[x]) > 25:
                tempError = tempError + "\n" + "Temperature level is ABOVE optimal at: \n" + str(x) + ":00:00"
            elif float(fileYlist[x]) < 21:
                tempError = tempError + "\n" + "Temperature level is BELOW optimal at: \n" + str(x) + ":00:00"

    if temperature_score == 24:
        temperature_score += 1


def temperaturechart():  # Creates the graph to show all of the readings taken over the last stated time period.

    ypoints = []
    for x in range(len(fileYlist)):
        ypoints.append(float(fileYlist[x]))

    plt.plot(timeHour_x, ypoints)

    plt.xlabel("Time")
    plt.ylabel("Measurement (Celsius)")
    plt.title("Temperature graph")
    plt.show()


def ph():  # This checks all the imported values against the correct measurements to make sure they are
    # in the bounds stated and creates 1 part of the score for the overall crop health graph.

    global ph_score, pHError
    ph_score = 0  # Overall ph score.
    readfile("pH.csv")

    for x in range(len(fileYlist)):
        if 8.3 >= float(fileYlist[x]) >= 5.5:
            print("Green")
            ph_score += 1

        elif float(fileYlist[x]) > 8.3 or float(fileYlist[x]) < 5.5:
            print("Red")
            if float(fileYlist[x]) > 8.3:
                pHError = pHError + "\n" + "pH level is ABOVE optimal at: \n" + str(x) + ":00:00"
            elif float(fileYlist[x]) < 5.5:
                pHError = pHError + "\n" + "pH level is BELOW optimal at: \n" + str(x) + ":00:00"

    if ph_score == 24:
        ph_score += 1


def phchart():  # Creates the graph to show all of the readings taken over the last stated time period.

    ypoints = []
    for x in range(len(fileYlist)):
        ypoints.append(float(fileYlist[x]))

    plt.plot(timeHour_x, ypoints, 'b--')

    plt.xlabel("Time")
    plt.ylabel("Measurement (pH)")
    plt.title("pH graph")
    plt.show()


def oxygen():  # This checks all the imported values against the correct measurements to make sure they
    # are in the bounds stated and creates 1 part of the score for the overall crop health graph oxygen.

    global oxygen_score, oxygenError
    oxygen_score = 0  # Overall oxygen score.
    readfile("oxygen.csv")

    for x in range(len(fileYlist)):
        if 6 >= float(fileYlist[x]) >= 5:
            print("Green")
            oxygen_score += 1

        elif float(fileYlist[x]) > 6 or float(fileYlist[x]) < 5:
            print("Red")
            if float(fileYlist[x]) > 1310:
                oxygenError = oxygenError + "\n" + "Oxygen level is ABOVE optimal at: \n" + str(x) + ":00:00"
            elif float(fileYlist[x]) < 1000:
                oxygenError = oxygenError + "\n" + "Oxygen level is BELOW optimal at: \n" + str(x) + ":00:00"

    if oxygen_score == 24:
        oxygen_score += 1


def oxygenchart():  # Creates the graph oxygen to show all of the readings taken over the last stated time period.

    ypoints = []
    for x in range(len(fileYlist)):
        ypoints.append(float(fileYlist[x]))

    plt.plot(timeHour_x, ypoints, 'b--')

    plt.xlabel("Time")
    plt.ylabel("Measurement (MG/L)")
    plt.title("OXYGEN graph")
    plt.show()


def scoreCalc():
    global cropHealth
    cropHealth = ph_score + temperature_score + oxygen_score + c02_score


c02()  # calls the carbon dioxide function.
temperature()  # Calls the temperature function.
ph()  # Calls the ph function.
oxygen()  # Calls the oxygen function.

scoreCalc()


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

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_CO2 = ttk.Button(self, text="CO2 Level",
                                command=lambda: [controller.change_frame(CO2)])
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
        self.crophealth_title = Label(self, text='''Crop's overall health''', font=smallfont, foreground='black',
                                      background='brown')
        self.crophealth_title.grid(row=3, column=3)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("black.Horizontal.TProgressbar", background='green')

        self.progress_Bar = Progressbar(self, length=200, style='black.Horizontal.TProgressbar')

        self.progress_Bar['value'] = cropHealth
        self.progress_Bar.grid(row=3, column=3, rowspan=2)

        self.healthintext = Label(self, text=str(cropHealth) + "/100", foreground="black", borderwidth=2,
                                  font=smallfont, relief='flat')
        self.healthintext.grid(row=4, column=3)

        self.button_Healthreset = ttk.Button(self, text="Update Health",
                                             command=lambda: [scoreCalc(), self.update_health()])
        self.button_Healthreset.grid(row=5, column=3)

        # Clock widget

        self.current_Time = ''
        self.current_time2 = "Time: " + time.strftime('%H:%M:%S')

        self.clock = Label(self, text=self.current_time2, font=mediumfont, background='White', foreground='black')

        self.clock.grid(row=2, column=3)

        self.clock_Tick()  # after the first call, the function itself calls itself --
        # every 200 millisecond to refresh the time

    def clock_Tick(self):
        self.current_time2 = "Time: " + time.strftime('%H:%M:%S')
        self.clock.configure(text=self.current_time2)
        self.clock.after(200, self.clock_Tick)

    def close(self):
        self.master.quit()

    def update_health(self):
        if cropHealth == 40:
            self.style.configure("black.Horizontal.TProgressbar", background='green')
            self.healthintext.configure(text=str(cropHealth) + "/100")
            self.progress_Bar['value'] = cropHealth
            self.configure(background='white')
        elif cropHealth < 25:
            self.style.configure("black.Horizontal.TProgressbar", background='red')
            self.healthintext.configure(text=str(cropHealth) + "/100")
            self.progress_Bar['value'] = cropHealth
            self.configure(background='brown')
        elif 25 < cropHealth < 40:
            self.style.configure("black.Horizontal.TProgressbar", background='orange')
            self.healthintext.configure(text=str(cropHealth) + "/100")
            self.progress_Bar['value'] = cropHealth
            self.configure(background='white')


# window frame for CO2 stats

class CO2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="         Carbon Dioxide - Stats", width=30, borderwidth=5, font=mediumfont,
                               background='lightgreen', foreground='black')

        Stickbot_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #  creating buttons and assigning them to their respective frames/page.
        button_mainmenu = ttk.Button(self, text="Main Menu",
                                     command=lambda: [controller.change_frame(Mainpage)])
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

        updateErrorLog.grid(row=0, column=2, columnspan=2, rowspan=6)

        # Inserting Text which is read only
        updateErrorLog.insert(tk.INSERT, co2Error)
        # Making the Log read only
        updateErrorLog.configure(state='disabled')

        # graph location
        graphLocation = Button(self, text="Click here to open the Graph", command=lambda: [c02(), c02chart()])
        graphLocation.grid(row=5, column=2, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# window frame for Temperature stats

class Temperature(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="           Temperature - Stats", width=30, borderwidth=5, font=mediumfont,
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

        updateErrorLog.grid(row=0, column=2, columnspan=2, rowspan=6)

        # Inserting Text which is read only
        updateErrorLog.insert(tk.INSERT, tempError)
        # Making the Log read only
        updateErrorLog.configure(state='disabled')

        # graph location
        graphLocation = Button(self, text="Click here to open the Graph",
                               command=lambda: [temperature(), temperaturechart()])
        graphLocation.grid(row=5, column=2, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# window frame for PH stats 

class PH(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="                 PH - Stats", width=30,
                               borderwidth=5, font=mediumfont,
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

        updateErrorLog.grid(row=0, column=2, columnspan=2, rowspan=6)

        # Inserting Text which is read only
        updateErrorLog.insert(tk.INSERT, pHError)
        # Making the Log read only
        updateErrorLog.configure(state='disabled')

        # graph location
        graphLocation = Button(self, text="Click here to open the Graph", command=lambda: [ph(), phchart()])
        graphLocation.grid(row=5, column=2, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# window frame for Oxygen stats 

class Oxygen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame/ Title of the page. plus the location using grid
        Stickbot_title = Label(self, text="               Oxygen - Stats", width=30, borderwidth=5, font=mediumfont,
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

        updateErrorLog.grid(row=0, column=2, columnspan=2, rowspan=6)

        # Inserting Text which is read only
        updateErrorLog.insert(tk.INSERT, oxygenError)

        # Making the Log read only
        updateErrorLog.configure(state='disabled')

        # graph location
        graphLocation = Button(self, text="Click here to open the Graph", command=lambda: [oxygen(), oxygenchart()])
        graphLocation.grid(row=5, column=2, columnspan=4, rowspan=3)

    def close(self):
        self.master.quit()


# Driver Code
application = Stickbot()
application.title("Stick-Bot Interactive Interface")
application.mainloop()
