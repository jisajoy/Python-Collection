'''List in collection'''
thisList = ["apple", "banana", "orange"]
print(thisList)
print(thisList[1])
thisList[1] = "berry"
print(thisList)
for x in thisList:
    print(x)
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")
print(len(thisList))
thisList.append("strawberry")
print(thisList)
thisList.insert(2,"Strawberry")
print(thisList)
thisList.remove("Strawberry")
print(thisList)
thisList.pop()
print(thisList)
del thisList[1]
print(thisList)
#del thisList
#print(thisList)#name 'thisList' is not defined(because the list is deleted with the del fuction)

thisList.clear()
print(thisList)#clear the list and prints the empty array


#new list is make with the constructor of list and it works as the same function above
newList = list(("android","java script","ajax", "java", "PHP", "Phython"))
print(newList)


In computing, data is information that has been translated into a form that is efficient for movement or processing. Relative to today's computers and transmission media, data is information converted into binary digital form. It is acceptable for data to be used as a singular subject or a plural subject.
