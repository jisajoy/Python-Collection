myFruitShop = ("apple", "orange", "grape")
myIter = iter(myFruitShop)

print(next(myIter))
print(next(myIter))
print(next(myIter))

myString = "Android Developement"
myIterString = iter(myString)

print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))
print(next(myIterString))


#this iteration can be done using the for loop also, both have same function in array and string



class IteratorClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 50:
         x = self.a
         self.a += 1
         return x
        else:
            raise StopIteration


myClassObj = IteratorClass()
myIterClassObj = iter(myClassObj)

# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))
# print(next(myIterClassObj))

for x in myIterClassObj:
    print(x)


