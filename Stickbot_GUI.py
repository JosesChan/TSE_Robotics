import tkinter as tk
import time
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tkinter.scrolledtext as st 
import tkinter as tk
from time import strftime


LARGEFONT = ("Comic Sans MS", 30, "bold")
mediumfont =("Comic Sans MS", 20, "bold")
smallfont =("Comic Sans MS", 15, "bold")

cropHeath = 40



class Stickbot(tk.Tk):
    	
	
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "left", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)


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

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.change_frame(Mainpage)

	# to display the current frame passed as
	# parameter
	def change_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()



# first window frame startpage

class Mainpage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		style = ttk.Style()

		style.theme_use('default')
		
	
		# label of frame/ Title of the page. plus the location using grid
		Stickbot_title = Label(self, text="         Stick Bot - Main Menu", width=30, borderwidth=5, font = mediumfont, background='lightgreen', foreground='black')

		Stickbot_title.grid(row = 0, column = 0, padx = 10, pady = 10)

		#  creating buttons and assigning them to their respective frames/page.
		button_CO2 = ttk.Button(self, text ="CO2 Level",
		command = lambda : controller.change_frame(CO2))
		button_CO2.grid(row = 1, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Temperature = ttk.Button(self, text ="Temperature Level",
		command = lambda : controller.change_frame(Temperature))
		button_Temperature.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

		button_PHLevel = ttk.Button(self, text ="PH Level",
		command = lambda : controller.change_frame(PH))
		button_PHLevel.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Oxygen = ttk.Button(self, text ="Oxygen Level",
		command = lambda : controller.change_frame(Oxygen))
		button_Oxygen.grid(row = 4, column = 0, columnspan=2, padx = 10, pady = 10)

		button_exit = ttk.Button(self, text ="EXIT",
		command = self.close)
		button_exit.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10)

		# Crop health
		crophealth_title = Label(self, text= '''Crop's overall health''', font= smallfont, foreground='black', background='cyan')
		crophealth_title.grid(row=4, column= 5)
		style = ttk.Style()
		style.theme_use('default')
		style.configure("black.Horizontal.TProgressbar", background='green')

		progress_Bar = Progressbar(self, length=200, style='black.Horizontal.TProgressbar')

		progress_Bar['value'] = cropHeath

		progress_Bar.grid(row=4, column=5, rowspan=2)

		healthdigit = "Crop's Health : " + str(cropHeath) + "/100"

		clock_label = Label(self, text= healthdigit, background="cyan", foreground="black", borderwidth=7, font = smallfont, relief='flat')
		clock_label.grid(row=3, column=5)


	
	def close(self):
         self.master.quit()
		
	


# window frame for CO2 stats 

class CO2(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		# label of frame/ Title of the page. plus the location using grid
		Stickbot_title = Label(self, text="       Carbon Dioxide - Stats", width=30, borderwidth=5, font = mediumfont, background='lightgreen', foreground='black')

		Stickbot_title.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)


		#  creating buttons and assigning them to their respective frames/page.
		button_mainmenu = ttk.Button(self, text ="Main Menu",
		command = lambda : controller.change_frame(Mainpage))
		button_mainmenu.grid(row = 1, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Temperature = ttk.Button(self, text ="Temperature Level",
		command = lambda : controller.change_frame(Temperature))
		button_Temperature.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

		button_PHLevel = ttk.Button(self, text ="PH Level",
		command = lambda : controller.change_frame(PH))
		button_PHLevel.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Oxygen = ttk.Button(self, text ="Oxygen Level",
		command = lambda : controller.change_frame(Oxygen))
		button_Oxygen.grid(row = 4, column = 0, columnspan=2, padx = 10, pady = 10)

		button_exit = ttk.Button(self, text ="EXIT",
		command = self.close)
		button_exit.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10)


		updateErrorLog = st.ScrolledText(self, width = 30, height = 8, font = ("Times New Roman", 15)) 
  
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
		graphLocation = Message(self, text="Graph Health ")
		graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)
		graphLocation.config(background='lightgreen')
		graphLocation.configure(font=mediumfont)



	def close(self):
         self.master.quit()

		


# window frame for Temperature stats 

class Temperature(tk.Frame): 
	def __init__(self, parent, controller):
    		
		tk.Frame.__init__(self, parent)
		# label of frame/ Title of the page. plus the location using grid
		Stickbot_title = Label(self, text="       Carbon Dioxide - Stats", width=30, borderwidth=5, font = mediumfont, background='lightgreen', foreground='black')

		Stickbot_title.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)


		#  creating buttons and assigning them to their respective frames/page.
		button_mainmenu = ttk.Button(self, text ="CO2 Level",
		command = lambda : controller.change_frame(CO2))
		button_mainmenu.grid(row = 1, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Temperature = ttk.Button(self, text ="Main Menu",
		command = lambda : controller.change_frame(Mainpage))
		button_Temperature.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

		button_PHLevel = ttk.Button(self, text ="PH Level",
		command = lambda : controller.change_frame(PH))
		button_PHLevel.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Oxygen = ttk.Button(self, text ="Oxygen Level",
		command = lambda : controller.change_frame(Oxygen))
		button_Oxygen.grid(row = 4, column = 0, columnspan=2, padx = 10, pady = 10)

		button_exit = ttk.Button(self, text ="EXIT",
		command = self.close)
		button_exit.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10)


		updateErrorLog = st.ScrolledText(self, width = 30, height = 8, font = ("Times New Roman", 15)) 
  
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
		graphLocation = Message(self, text="Graph Health ")
		graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)
		graphLocation.config(background='lightgreen')
		graphLocation.configure(font=mediumfont)



	def close(self):
         self.master.quit()


# window frame for PH stats 

class PH(tk.Frame):
    	def __init__(self, parent, controller):
    		
		tk.Frame.__init__(self, parent)
		# label of frame/ Title of the page. plus the location using grid
		Stickbot_title = Label(self, text="       Carbon Dioxide - Stats", width=30, borderwidth=5, font = mediumfont, background='lightgreen', foreground='black')

		Stickbot_title.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)


		#  creating buttons and assigning them to their respective frames/page.
		button_mainmenu = ttk.Button(self, text ="CO2 Level",
		command = lambda : controller.change_frame(CO2))
		button_mainmenu.grid(row = 1, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Temperature = ttk.Button(self, text ="Temperature Level",
		command = lambda : controller.change_frame(Temperature))
		button_Temperature.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

		button_PHLevel = ttk.Button(self, text ="Main Menu",
		command = lambda : controller.change_frame(Mainpage))
		button_PHLevel.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Oxygen = ttk.Button(self, text ="Oxygen Level",
		command = lambda : controller.change_frame(Oxygen))
		button_Oxygen.grid(row = 4, column = 0, columnspan=2, padx = 10, pady = 10)

		button_exit = ttk.Button(self, text ="EXIT",
		command = self.close)
		button_exit.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10)


		updateErrorLog = st.ScrolledText(self, width = 30, height = 8, font = ("Times New Roman", 15)) 
  
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
		graphLocation = Message(self, text="Graph Health ")
		graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)
		graphLocation.config(background='lightgreen')
		graphLocation.configure(font=mediumfont)



	def close(self):
         self.master.quit()
    	
    	

# window frame for Oxygen stats 

class Oxygen(tk.Frame):
    	def __init__(self, parent, controller):
    		
		tk.Frame.__init__(self, parent)
		# label of frame/ Title of the page. plus the location using grid
		Stickbot_title = Label(self, text="       Carbon Dioxide - Stats", width=30, borderwidth=5, font = mediumfont, background='lightgreen', foreground='black')

		Stickbot_title.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)


		#  creating buttons and assigning them to their respective frames/page.
		button_mainmenu = ttk.Button(self, text ="CO2 Level",
		command = lambda : controller.change_frame(Mainpage))
		button_mainmenu.grid(row = 1, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Temperature = ttk.Button(self, text ="Temperature Level",
		command = lambda : controller.change_frame(Temperature))
		button_Temperature.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

		button_PHLevel = ttk.Button(self, text ="PH Level",
		command = lambda : controller.change_frame(PH))
		button_PHLevel.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

		button_Oxygen = ttk.Button(self, text ="Main Menu",
		command = lambda : controller.change_frame(Mainpage))
		button_Oxygen.grid(row = 4, column = 0, columnspan=2, padx = 10, pady = 10)

		button_exit = ttk.Button(self, text ="EXIT",
		command = self.close)
		button_exit.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10)


		updateErrorLog = st.ScrolledText(self, width = 30, height = 8, font = ("Times New Roman", 15)) 
  
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
		graphLocation = Message(self, text="Graph Health ")
		graphLocation.grid(row=1, column=5, columnspan=4, rowspan=3)
		graphLocation.config(background='lightgreen')
		graphLocation.configure(font=mediumfont)



	def close(self):
         self.master.quit()
    	
    	






# Driver Code
application = Stickbot()
application.title("Stick-Bot Interactive Interface")
application.mainloop()

