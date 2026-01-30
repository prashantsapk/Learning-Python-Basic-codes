#  A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  
#  Repeat program 4 for a list of such words to be censored. 

list = ["Fuck","Donkey","Sex","Dumb"]

with open("Hi-score.txt","r")as f:
    a=f.read() # a reads the file and stores the contains of it
    
for i in list:
        a = a.replace(i,"#####")
    # I have do something here so that, instead of temporary
    # the data can be easily stored and doesn't sores temporary

       

with open("Hi-score.txt","w") as f:
        f.write(a)

    