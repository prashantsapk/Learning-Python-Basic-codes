a = open("Hi-score.txt")
b=a.read()
print(b)
a.close()

# you can use with statement to do same stuffs

with open("Hi-score.txt") as c:
    d = c.read()
    print(d)

    # you don't need to close file here easy.