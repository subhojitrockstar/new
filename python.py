# test='test'
# print(test)
# print(type(test))
#
# print(f"This is {test}")
# print(f"This is {10+10}")
# l1 =[1,'Sham']
# t1 =(1,'Sham')
# l1[0]="Sita"
#
# print(l1)
# print(t1)
# a=input("Type a number:")
# print(a)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#  print(i)
# thislist = ["apple", "banana", "cherry"]
# x=0
# while x<(len(thislist)):
#     print(thislist[x])
#     x = x + 1
# test = [1,4]
# test1 = [j*3 for j in test]
# print(test1)
# thislist = ["b", "m", "d", "a", "c"]
# thislist.sort()
# print(thislist)
#
# thislist = [1,3,8,9]
# thislist.sort()
# print(thislist)
#
# thislist = [1,3,4,5]
# thislist.sort(reverse=True)
# print(thislist)
# thislist.copy()
# print(thislist)
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
#
# list1.extend(list2)
# print(list1)

# Python - List Methods

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

#tuple
# tlist=(1,2,3,6,5,9)
# z=(1,2,3,6,5,9)
# # print(type(tlist))
# # print(tlist)
# # print(tlist[0])
# # print(tlist[-1])
# # print(tlist[2:5])
# y= list(tlist)
# y.insert(0,"10")
# y.append("x")
# y.extend(z)
# y.remove(9)
# tlist=tuple(y)
# print(type(tlist))
# print(tlist)
# print(len(tlist))
# Unpack Tuples
# fruits = ("apple", "banana", "cherry")
# fruits2 = ("apple", "banana", "cherry")
# (a,b,c) = fruits
# (*a,) = fruits
# print(a)
# loop Tuples
# for a in fruits:
# for b in range(len(fruits)):
#     # print(len(a))
#     # print(a)
#     print(b)
# i=0
# while i < len(fruits):
#     print(fruits)
#     print(fruits[i])
#     i=i+1
 #join tuple
# x = fruits + fruits2
# print(x)
# print(x*2)#multiply
# print(fruits.count("apple")) #count
# print(fruits.index("apple")) #index
# thisset = {"apple", "banana", "cherry"}#will ignore dublicate value and will print unorderway
# thisset2 = {"apple", "banana", "cherry",1,3}
# # print(thisset)
# # print(len(thisset))
# # print("apple" in thisset)
# # for i in thisset:
# #     print(i)
# # i=0
# # while i < len(thisset):
# #     print(i)
# #     print(thisset)
# #     i=i+1
# thisset.add(1)
# print(thisset)
# thisset.update(thisset2)
# print(thisset)
# n = 6
# for i in range(n):
#     print(i * i)

#remove set
# thisset = {"apple", "banana", "cherry",3}
# thisset2 = {"apple", "banana", "cherry",5}
# # # thisset.remove("apple")
# # thisset.discard(3)
# # thisset.pop()
# # print(thisset)
# # for i in thisset:
# #     print(i)
# set3 = thisset.union(thisset2)
# print(set3)
# fruits = {"apple", "banana", "cherry"}
# # fruits.add("orage")
# # print(fruits)
# # more_fruits = ["orange", "mango", "grapes"]
# # fruits.update(more_fruits)
# # fruits.remove("banana")
# fruits.discard("banana")
# print(fruits)
#python dictionary
# thisdict = {
#   "Car details": {
#     "Brand":"Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
#   },
#     "Car details2": {
#     "Brand": "Hundai",
#     "electric": True,
#     "colors": ["red", "white", "black"]
#   },
#  "year": 2023,
#  }
# print(thisdict)
# print(thisdict["Car details"])
# print(thisdict["Car details2"]["colors"])

# print(thisdict["year"])
# print(thisdict.get("Car details2"))
# print(thisdict.keys())
# print(thisdict.values())
# thisdict["year"]=2024
# print(thisdict["year"])
# thisdict.update({"Car details":"Car is good"})
# print(thisdict["Car details"])

# thisdict.pop("Car details")
# thisdict.popitem()
# print(thisdict)

# for x in thisdict:
#   # print(x)
#   print(thisdict[x])
# for x in thisdict.values():
#   print(x)
# for x in thisdict.keys():
#   print(x)
# for x in thisdict.items():
#   print(x)
# print(thisdict.copy())
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(car.get("model"))
# # car["color"]= "red"
# # print(car)
# car.pop("model")
# print(car)
# car.clear()
# print(car)
# a = 33
# b = 200
# if b < a:
#   print("b is greater than a")
# if b > a:
#     print("Ok")
# else:
#   print("ignore")
# a = 33
# b = 200
# if b < a:
#   print("b is greater than a")
# elif b > a:
#     print("Ok")
# elif b == a:
#     print("ok ok")
# elif b != a:
#     print("ok ok")
# else:
#   print("ignore")
# loops
# a=0
# while a < 10:
#     print("fine",a)
#     a=a+1
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# functions
# def raj(a,b):
#      sum= a + b
#      sum1 = a - b
#      sum2 = a * b
#      print("\n", sum,"\n",sum2,"\n",sum1)
# raj(20,50)
# def raj():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     sum = a + b
#     sum1 = a - b
#     sum2 = a * b
#     print("\n", sum, "\n", sum2, "\n", sum1)
# raj()
# if 5 > 2:print("Five is greater than two!")
# print("Yes") if 5 > 2 else print("No")
# i = 1
# while i < 6:
#     if i == 3:
#       break
#     i += 1
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# def my_function(fname, lname):
#   print(fname)
# def my_function(fname):
#   print(fname + " Refsnes")
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")
#
# def my_function(*kids):
#   print("The youngest child is " + kids[1])
#
# my_function("Emil", "Tobias", "Linus")
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)
#
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")
# mylist=["sb",1,2,3,4,5,6]
# for x in range(len(mylist)):
#     if x==3:
#       break
#     print(x)
# mylist=["sb",1,2,3,4,5,6]
# for x in range(len(mylist)):
#     if x==3:
#       continue
#     print(x)
# list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# 
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# 
# print(newlist)
#recursion
# def re(x):
#   if x==0:
#     print(x)
#   else:
#     print(x)
#     re(x-1)
# re(6)
# Zip
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# num = [1,2,3,4]
# print(list(zip(fruits,num)))
#debugging
# #lambda
# x = lambda a,b: a+b
# print(x(10,20))
#class & object
# class raj:
#     age=""
#     Mobile=""
#     surname=""
# a=raj()
# a.age=29
# a.mobile=977508504
# print("\n",a.age,"\n",a.mobile)
#
# Multiple Inheritance
# class Subhojit:
#     Mobile = ""
#     macbook = ""
#
# class swag:
#         tv = ""
#         fridge = ""
# class Anirban(Subhojit,swag):
#     nokia = ""
# x = Anirban()
# x.macbook = "Apple" # Assign the value "Apple" to the macbook attribute
# x.tv="samsung"
#
# print("\n",x.macbook,"\n",x.tv)  # Output: Apple

# # Multilevel Inheritance
# class Subhojit:
#     Mobile = ""
#     macbook = ""
#
# class swag(Subhojit):
#         tv = ""
#         fridge = ""
# class Anirban(swag):
#     nokia = ""
# x = Anirban()
# y = swag()
# x.macbook = "Apple" # Assign the value "Apple" to the macbook attribute
# x.tv="samsung"
# y.fridge="LG"
#
# print("\n",x.macbook,"\n",x.tv,"\n",y.fridge)
