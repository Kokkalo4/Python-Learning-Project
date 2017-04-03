#1) For Loop
#In order to use a for loop we need to have a list or a dictionary. In this
#we will use a list in order to make this simpler.
bag = [10,1231,124323,1243,1342523,123,23442]
bag
#get length of the bag.
len(bag)
#create the for loop.
for item in bag: print(item) #item is a dummy name but we have to include the list
#where the for loop has to look in order to do what is instructed.
#for loop to count the items in bag list.
i = 0
for item in bag:
    i = i + 1
    print(i)
#for loop with if:
for item in bag:
    if item == 10:
    print("yeeeaaaaahhhh")


#2) While Loop
#While checks for condition.
#Syntax: while <condition> == True:
    #Do something.
i = 10
while i < 11:
    print("yup")
    i = i + 1

i = 1
while i < 1000:
    print(i)
    i = i + 1
#BE CAREFUL TO STOP WHILE LOOP BECAUSE IT WONT STOP. Ctrl + C kills function.

