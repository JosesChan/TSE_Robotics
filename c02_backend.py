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

 import matplotlib.pyplot as plt

 c02x = 2, 3, 4, 5, 6, 7, 8, 9, 1 # To be replaced with the imported variable name. 
 c02y = 5, 3, 2, 5, 6, 7, 8, 9, 2 # To be replaced with the imported variable name. 
 xpoints = c02x
 ypoints = c02y

 plt.plot(xpoints, ypoints, 'o')

 plt.xlabel("Time")
 plt.ylabel("Measurement (PPM)")
 plt.title("C02 graph")
 plt.show()

c02() # Calls the c02 function.
print("C02 score = ", c02_score, "/ 25") # Displays the c02 score out of 25.

c02chart() # calls the c02chart function.
