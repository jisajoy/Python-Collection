def my_function():
    print("This is a function")

my_function()

def param_function(fname):
 print("parameter says : " + fname)

param_function("Email")#passing a parameter
param_function("User Name")

def countryCatcher(country = "India"):#assigning a default parameter
    print("My Country is " + country)

countryCatcher("Sweden")
countryCatcher("India")
countryCatcher()

def do_the_math(x):
    return x * x

print(do_the_math(5))
print(do_the_math(6))


''' LAMBDA FUNCTION'''

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 4))# any number of arguments take but only one expression is formed

#lambda  using the function, it will be like an anonymous call

def my_unknown(n):
    return lambda a : a * n

doubleVal = my_unknown(4)

print(doubleVal(5))# if the doubleVal printed the it shows an object when i replace the value of lambda a to 11 then it prints its value

This is a master branch changes
