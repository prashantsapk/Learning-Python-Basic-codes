def printname():
    print("HELLO WORLD")


if __name__ == "__main__": # the code that doesn't need to be executed
#     # for another file or when the another is running we use this
#     # because __name__="__main__" is only for current file this file
#     # other wise if runned in another file it will be __name__ = "module"
 printname()
 print(__name__)

