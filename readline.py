
a = open("Hi-score.txt")
# b = a.read()
# print(b)

# c= a.readline() # line by line so it already read line 1 so the readlines is showing remaning line 
# #in list
# print(c)

# d = a.readlines() # read all lines but on list
# print(d)

# you can also use loop for readline


b=a.readline()

while(b!=""):
  print(b)
  b=a.readline()

a.close()