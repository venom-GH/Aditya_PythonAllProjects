#Prints
def rando():
    print("hello")
    print("world")

#user defined functions with a default value
def rando2(x,y,z="user"):
    print("hello",z)
    print(x,"teaches me comp")
    print(x,"is",y,"years old")

#Calling the function
rando():

name=input("enter your name : ")

#Calling the function with parameters
rando2("sarika",22,name)
