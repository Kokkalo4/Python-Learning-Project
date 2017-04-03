#Conditionals.
#Help us control the flow of a program.

#Conditional Expressions.
#1) Boolean Values. (True or False). Syntax: True/False.
True
False
print(True==True)

"justin" == "Justin"

obj_a = True
obj_b = False
obj_a == True #Not when we assign we use = BUT when we compare we use ==

name = "justin"
name == True

lista = [1,2,3]
listb = [1,2,3]
listc = [4,5,6]
print(lista == listb)
print(lista == listc)
print(lista != listc) # != means not equal.

#To get the inverse of an of object type not in front of the object.
not lista

#To compare the opposite of an object with another object use.
print(not obj_a == obj_b)
#use is as well.
print(not obj_a is obj_b)

#Compare the length of an object with a number.
name = "justin"
name
print(len(name))
print(len(name)==6) #do the comparison.
print(len(name) >= 6) #can also use <> signs as well for comparison.

#Can do some maths with booleans.
print(100-32 != 93)
print(5+5== 10)
print(10/2==5)
print(3**3 == 9) #** means raise to the power
print(50%2 == 0) #% is the modulo(remainder)


#2) Running Conditional statements in Loops.
list_a = [1,2,3]

for i in list_a:
    print(i)
for i in list_a:
    print(i**2) #raises i to 2nd power.

for i in list_a:
    if (i**2)%3 == 0:
        print("your number is 9")
        print(i) #use modulo inside a condition.

for i in list_a:
    if i == 2:
        print("yup it's two")
    elif i == 1:
        print("something different")
    else:
        print(i)


#New list and we want to check this time which of the items in the list are
#numbers.
list_d = ["Justin", "Apple", "Food", 3231, "Another", 390122]
list_e = []
#isinstance() function checks if something is True. 
for i in list_d:
    print(i)
isinstance(3,int) #in this case it checks if the 4th item in the list is integer.
                  #REMEMBER python starts counting from 0 for 1st item.
isinstance("Justin", str) #would return True since "Justin" is string.
isinstance("Justin", int) #would return False since "Justin" is not integer.

for i in list_d:
    if isinstance(i,int):
        list_e.append(i)
print(list_e)
#The above function searches through list_d finds integers and copies them
#to the empty list_e. The items that were copied in list_e remain to list_d as
#well.

x = 0
list_d[x] #gives 1st item since x = 0
list_d[x+1] #gives 2nd item since x is now 1.

for item in list_d:
    print(list_d[x])
    x += 1 #x = x + 1
#The above function goes through every object in list_d and prints it.

#Next we are going to go through list_d again but in this case we are going to
#find the integers on this list, remove them from list_d and copy them to list_e
#First we empty list_e and reset x.
x = 0
list_e = []
list_d = ["Justin", "Apple", "Food", 3231, "Another", 390122]

for item in list_d:
    if isinstance(item, int):
        list_e.append(item)
        list_d.pop(x)
    x += 1
#So now if we check through list_d and list_e we see that list_d contains only
#strings while list_e now has the integer values.
list_d
list_e



