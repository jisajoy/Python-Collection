thistuple = ("apple", "banana", "cherry")
print(thistuple)
'''the tuple value cannot be added like this because the tuples are ordered nd unchangeable'''
#thistuple[1] = "orange"
#print(thistuple)

for x in thistuple:
  print(x)

if "apple" in thistuple:
 print("Yes, 'apple' is in the fruits tuple")

print(len(thistuple))

#del thistuple# del makes the tuples delete
#print(thistuple) # so if the tuples doesnot exist it shows error

constTuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(constTuple)# constructor creates the tuple values



'''SETS'''


thisSet = {"keyboard", "mouse", "monitor"}
print(thisSet)

for x in thisSet:
    print(x)

print("keyboard" in thisSet)# retuens true if the value is inside the set

thisSet.add("printer")#using add only one item can be entred in the set
print(thisSet)

thisSet.update(["DVD", "Speaker", "microphone", "keyboard"])# here the item added in an unordered fasion and update is used to add more than one item in the set
print(thisSet)

print(len(thisSet))

thisSet.remove("mouse")
print(thisSet)

thisSet.discard("banana")
print(thisSet)#even if I added the set value as wrong it doesnot produce any error

d = thisSet.pop()
print(d)
print(thisSet)

thisSet.clear()
print(thisSet)# clear all values and retrun an empty constructor of set

#del thisSet
#print(thisSet)#produces error because it tried to print the unknown set

contSet = set(("apple", "banana", "cherry")) # note the double round-brackets
print(contSet)