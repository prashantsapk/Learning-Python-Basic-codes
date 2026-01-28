# Write a python program using function to convert Celsius to Fahrenheit. 
#F=(C×9/5)+32

def temperature():
    a= int(input("Enter the temperature you want in celsius"))
    f=((a * (9/5))+32)
    return f

a = temperature()
print(a)