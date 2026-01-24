# #  Write a program to create a dictionary of Nepali words with values as their English 
# translation. Provide user with an option to look it up! 

a={"Shanti":"Peace","Gham":"sun","Chandrama":"moon"} 
print("Welcome to nepali dictionary, you can check the meaning in english as well")
print("Nepali words are:",a.keys())
b=input("Type the word which meaning you want")
print(a[b])