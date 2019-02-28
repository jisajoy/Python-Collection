class myClass:#class name decalare
    x = 5

p1 = myClass()#class object create
print(p1.x)#accesing the class variable using the object

#class with the initialising of values (like a constructor)

class Person:
    def __init__(mySillyObject, name, age):#here the init represented as a consutructor
        mySillyObject.name = name #self is an object represented instance in object (it contains all the information about the class and its contents)
        mySillyObject.age = age #self acts like 'this' keyword in java
    def my_function(abc):# here the self must be important that the class instance is avaliable in this method
     print("This is my function "+abc.name)
'''About 'self' its not up to the name of the object its up to the position if the position of the object is in the front of the method or constructor the the object must be the instance of the class or saying 'self' '''

p2 = Person("jisa", "24")

print("Name :"+p2.name)
print("Age :"+p2.age)
p2.my_function()


p2.age = "36"#here the value must given as the same type that given in the init method otherwise it modified as another type and get confused
print("NameM :"+p2.name)
print("AgeM :"+p2.age)


