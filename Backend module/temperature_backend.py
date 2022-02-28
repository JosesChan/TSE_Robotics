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

temperaturechart() # calls the water chart function.

  



