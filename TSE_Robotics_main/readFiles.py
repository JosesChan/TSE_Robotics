  
import sys
# imports functinos that allow the file to exit
fileXlist =[]
fileYlist =[]
#lists to store values from the files
def readfile(fileName):
  #Function that will take the file wanting to be read 
  fileXlist.clear()
  fileYlist.clear()
  file = fileName #assign the filename to a local variable
  counter = 0
  try:
    oFile = open(file,"r")
  except FileNotFoundError:
    print("Filename;"+ file +" is not found")
    input("press any key to exit....")
    sys.exit()
  #try block to accept error of file not being found
  rFile = oFile.readlines()
  for newline in rFile:
    text_split = newline.split(",")
    for text in text_split:
      if counter == 0:
        fileXlist.append(text)
      else:
        fileYlist.append(text)
      counter +=1
    counter = 0
  # reads the file and splits it via a comma and adds it to the global lists.
  oFile.close()

#readfile("file1.csv")
#Testing the read file function
#for i in range((len(fileXlist)-1)):
  #print(str(fileXlist[i])+" , "+str(fileYlist[i]))
#prints all the values