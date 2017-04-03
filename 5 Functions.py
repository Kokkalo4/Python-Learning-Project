#First we create 2 lists mixed with strings, decimal integers and strings.
items = ["Mic","Phone",323.12,3123.123,"Justin","Bag","Cliff Bars",134]

#Next we are going to perform some actions on lists.
#1)Sort Lists for Strings.
str_items = ["Abc","JM","ED","AD","aaa","bb"]
str_items
str_items.sort()
str_items #.sort() functions sorts the list in alphabetical order. First uppercase
#characters then lowercase characters.
#To sort with alphabetically we do:
str_items.sort(key=str.lower)
#To perform the above function in reverse we do:
str_items.sort(key=str.lower, reverse = True)

#To sort the list above to a new list without messing with the original list:
str_items = ["Abc","JM","ED","AD","aaa","bb"]
new_items = sorted(str_items) #Sorted performs the original sort as was done with
#.sort() function.
new_items
#Of course additional parameters can be added as was done above with .sort()
new_items = sorted(str_items,key=str.lower)
new_items = sorted(str_items,key=str.lower, reverse = True)

#2)Sorting lists with numbers.
#Sorting numbers with the same idea as above.
int_items = [123,13.23,3213,323.23,9942]
#Sort from smaller to larger:
int_items.sort()
int_items
#Sort from larger to smaller:
int_items.sort(reverse=True)
int_items

#To sort the above list to a new list without messing the original list works as
#well with the sorted() function as above:
new_items = sorted(int_items)
new_items
new_items = sorted(int_items, reverse = True)

#3) Numbers in lists:
#adding all numbers in a list:
sum(int_items)
#view the length of items:
len(int_items)
#get the average:
total = sum(int_items)
average = total/len(int_items)
average

#Working with functions on Python:
#First we create a list containing mixed floats , integers and strings. Then, we create 2 empty lists where one will be used to stored string values and the other will be used to store integer and float values:
items = ["Mic","Phone",323.12,3123.123,"Justin","Bag","Cliff Bars",134]
str_items = []
num_items = []

#The function below runs through the first list and separates integers and floats from string values and puts them to the list according to their type:
for i in items:
	if isinstance(i, float) or isinstance(i, int):
		num_items.append(i)
	elif isinstance(i, str):
		str_items.append(i)
	else:
		pass 
print(str_items)
print(num_items)


#Create our first Function: The function we are going to create will do exactly what the above commands do but more automated.
#First we define the name of the function and we declare that it will take inside some lists:
def parse_lists(some_list):
	str_list_items = []
	num_list_items = []
	for i in some_list:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass 
 	return str_list_items, num_list_items

#We call the function called parse_lists on the list called items:
print(parse_lists(items))

#The function above can also be done when we have in the list another list or other things too.
#The parse_lists() function we created above won't do anything on the items2 list because we haven't defined it to do anything.
items2 = ["Mic","Phone",323.12,3123.123,"Justin","Bag","Cliff Bars",134, [12312, "aaaa", "dasasdsa", 312412.12424]]
print(parse_lists(items2))


#Sum function:
#As we saw above we can use sum() function to get the sum of the numbers in a list:
sum([948,944120,412412])

#Now we can define another function that will deal with numerics:
#This function will check a list and will bring us back the sum of all the floats and integers in it:

def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i
	return total

#Now we test our function with a list that does not include only numbers:
items3 = ["Joe", "Bob", 2131, 2412, "me" , "ro", 124.2 , 412.1, "buew"]
sum(items3)
my_sum(items3)
#The function we created above will filter out the contents of the list and will sum only floats and integers leaving out any string values. On the contrary the sum() function will return an error.
#Once again this is done on the top level of a list. If there was a list inside the first list it wouldn't do anything with it.

#Average function:
#This function will get the average of the items in a list:
#in order to do so we have to create 2 functions: The first will count only the items that are floats and integers in a list and the second one will be the function that will get us the average:

def count_nums(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += 1
	return total

def my_avg(my_num_list):
	the_sum = my_sum(my_num_list)
	num_of_items = count_nums(my_num_list)
	return the_sum/ (num_of_items*1.0)

my_avg(items3)

#CONCLUSION:
# *To define function use the def.
# *Then give a function name.
# *Then pass parameters or arguements inside parenthesis of the function name.
# *Then write the main body of the function and define everything that the function will do.
# *To call the function: Use the defined name and import the list you will use within the parenthesis following the name.