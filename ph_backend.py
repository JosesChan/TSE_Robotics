
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

phchart() # calls the phchart function.

  

