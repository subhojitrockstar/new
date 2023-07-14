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
fruits = ("apple", "banana", "cherry",1,2)
# (a,b,c) = fruits
# (*a,) = fruits
# print(a)
# loop Tuples
# for a in fruits:
# for b in range(len(fruits)):
#     # print(len(a))
#     # print(a)
#     print(b)
i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1