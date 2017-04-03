Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
#Data Types in Python.
#1) Lists/Arrays.
#Lists are lists of items.
[]

[] #empty list

["something"] #list with 1 item
["something1","something2"] #list containing 2 items.

#in lists you can put strings or numbers.
#You can assign the list to a value:
list1 = ["a string", 123, "another string"]
#Add new items to list with .append() function:
list1.append("new string")
list1

#Remove items from a list with the .pop() function:
list1
list1.pop(2)

list1
#We can get the length of a list with the len() function:
len(list1)
len("a string i have made")

#Selecting items from a list:
list1[0] #Returns first item
list1[1] #Returns second item
list1[2] #Returns third item

#Remove by position.
list2 = ["John","Jack","Dave"]
list2
list2.pop(0) #Removes first item. If done many times will clear the whole list.


#Dictionaries: Dictionaries can hold key - value pairs.
{} #Empty dictionary

{"abc":"a string"} #dictionary with one key-value pair
{"abc":"a string",
 "def":"another string",
 "geh":"a third string",
 "poi":"a fourth string"}
#In a dictionary on the left is the key and on the right is the assigned value of that key. The key has to be a string BUT the value can be anything.
#Setting a new dictionary:
dict1 = {"abc":"a string",
 "def":"another string",
 "geh":"a third string",
 "poi":"a fourth string"}
dict1["abc"] = "another new string" #overwrite existing value in dictionary.
dict1

dict1["0"]="import new value" #add new value to the dictionary.
dict1

#We can get items from dictionary by importing the key.

dict1["abc"]
#In dictionary we can also add a list and a dictionary.
dict1["new_dict"] = {"one":1, "two":2,"three":3}
dict1

dict1["new list"]=[1,2,3,4]
dict1

#Tuples: Tuples are two value pairs.
#Tuples is a mixture of a list and a dictionary.
tup = () #empty tuple
tup = ("abc","abc")
tup

#Tuples can contain tuples.
tup = (
 	("another","other"),
	("the other","ofother"))
#Selecting the values of a tuple is like selecting values from a list.
tup[0]

tup[0][0]

#Add items to a tuple.
tup += ("yetAnother",123) #The items will be added as objects.
tup

tup += (("yetAnother",123),) #The items will be added as a tuple.
tup
