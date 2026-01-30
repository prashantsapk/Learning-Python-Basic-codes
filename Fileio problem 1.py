# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

f = open("Hi-score.txt")
read = f.read()
print(type(read))
print(read)
c=read.replace("Donkey","#####") # you can't direct execute read.replace() function on string, you need to save it on variable
# string are immutable
print("Type of f is ",type(f)) # we need to convert this into string or ??
f.close()
print(read)

if ("Donkey" in read):
    print("There is donkey and now its replaced by #####")
    f1=open("Hi-score.txt","w")
    f1.write(c)
    f1.close()
else:
    print("There is no slang language")
    

