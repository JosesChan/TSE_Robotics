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

oxgenchart() # calls the oxygen chart function.

  

