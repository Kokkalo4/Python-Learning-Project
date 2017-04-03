#String Manipulation.
#Here we will use some string manipulation commands as described on 30 days of Python Cheat Sheet that can be found [here](https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/PythonCheatSheet.md)

#1) Strings.
text = "Some string, with some stuff."

text2 = "Yet, another string here."

text3 = "Concatenation combines strings like \"" + text + "\" and \"" + text2  + "\""
print(text3)

#2) String Formating:
#2.1) Add a new line: Use \n to add a new line.
text = 'Often\nYou need a new line'
print(text)

#2.2) Add tab:
text = 'Often a \t tab is needed.'
print(text)

#2.3) Escaped Single Quote. Use \'
text = 'Sometimes it\'s your quote sometimes it isn\'t'
print(text)

#2.4) Escaped Double Quote. Use \''
text = "Sometimes it\'s a \"Quote from someone else\""
print(text)

#2.5) Escape Linebreak. Use \
text = "Sometimes you need to have \
a inline break that isn't a linebreak."
print(text)

#2.6) Lowercase entire string. Use .lower() function:
text = "Some string, with some stuff."
text.lower()
print(text)

#2.7) Uppercase entire string. Use .upper() function:
text = "Some string, with some stuff."
text.upper()
print(text)

#2.8) Capitalize string with the use of both .lower() and .upper() functions.Here we simply capitalize the first character of the string:
lower_cased = "this sentence needs to be capitalized."
cap_string = lower_cased[0].upper() + lower_cased[1:]
print(cap_string)

#2.9) Break up string. To break up a string we use the .split() function:
text = "Some string, with some stuff."
print(text.split())
print(text.split(","))

#2.10) Count String length. To count the length of the string use the len() function:
text_length = len("Some string, with some stuff.")
print(text_length)

text = "Some other length"
text_length2 = len(text)
print(text_length2)

#3) String Substitution:
#3.1) Format with Keyword Variables:
text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)

text = "This is another {variable_a} formatted string with \
multiple variables like {a} {b} {c}.".format(
    variable_a="variable based", 
    a="some random", b="replacement", c="text")
print(text)

text = """So, {name}, the best part is formated strings you don't have to order it. 
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously {name}, this is some fun formatting.""".format(
            name="Jerry", 
            var_a="Variable 1", 
            var_b="Variable 2")
print(text)

#3.2) Format with Arguements:
text = "This is {0} formatted string".format("argument based")
print(text)

text = "This is another {0} formatted string \
with multiple variables like {1} {2} {3}.".format(
    "variable based", 
    "some random", 
    "replacement", 
    "text"
    )
print(text)

text = """So, {0}, the best part is formated strings you don't have to order it. 
And these argument replacements, ({1}, {2}, {0}) can be reused over and over.
Seriously {0}, this is some fun formatting.""".format(
            "Jerry", 
            "Variable 1", 
            "Variable 2")
print(text)

#3.3) Substitution. To do substitution use the %s function:
text = "This is %s formatted string" %("replacement")
print(text)

text = "The %%s format string is not as %s, but still very %s." %("robust", "useful")
print(text)

#3.4) Float Substitution(Move decimal places).To perform float substitution use the %f function:
text = "0 decimal places: %.0f" %(20)
print(text)


text = "2 decimal places: %.2f" %(20)
print(text)

text = "10 decimal places: %.10f" %(20)
print(text)

text = "400 decimal places: %.400f" %(20)
print(text)

#4) Date Substitution:
#In order to get the date we need to import the datetime package.
import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%-m/%-d/%y')
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)

#5) Working with files:
file_obj = open(file_name, "<mode>")

Mode 	Description
"r" 	Read only. Default mode.
"rb" 	Read only in binary format
"r+" 	Read and write
"rb+" 	Read and write in binary format
"w" 	Write only. Overwrites existing file or creates a new file.
"wb" 	Write only in binary format. Overwrites existing file or creates a new file.
"w+" 	Read and write. Overwrites existing file or creates a new file.
"wb+" 	Read and write in binary format. Overwrites existing file or creates a new file.
"a" 	Append to existing file or creates new file.
"ab" 	Append to existing file or creates new file in binary format.
"a+" 	Read and append. Overwrites existing file or creates a new file.
"ab+" 	Read and append in binary format. Overwrites existing file or creates a new file.


#Now following up all of the above, we are going to create some string substitution functions:
#The function we are going to do will use 2 lists and a text string, and what it will actually do is it will format a generic text to be in response of certain person:

default_names = ["Justin", "John", "Emilee", "Jim", "Ron", "Sandra", "Veronica","Whitney"]
default_amounts = [123.32,94.23,124.32,323.4,23,323.122323,32.4,99.99]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it.Just as a 
reminder the purchase total was ${total}.
Have a great one!

Team CFE
"""

#Create the function:
def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		for name in names:
			new_msg = unf_message.format(
				name = name,
				date = "some date",
				total = 129.99
				)
			print(new_msg)

make_messages(default_names,default_amounts)
#The above function runs through all the names in the list and prints the formatted message with a different name everytime it prints. So as an output we have 8 printouts of the message with 8 different
#names that are the contents of the list default_names. But as we see this function has some problems. We have on each iteration a fixed amount and instead of a date we have the string "some date".
#In order to fix this we have to do the following adjustments to the above function:


#Create the fixed function:
#NOTE: for this function to work, we need to have names and amounts lists of equal lengths or the function will produce an ERROR:
def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		for name in names:
			new_msg = unf_message.format(
				name = name,
				date = "some date",
				total = amounts[i]
				)
			i += 1
			print(new_msg)

make_messages(default_names,default_amounts)

#Above function with same decimal places: 
def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		for name in names:
			new_amount = "%.2f" %(amounts[i])
			new_msg = unf_message.format(
				name = name,
				date = "some date",
				total = new_amount
				)
			i += 1
			print(new_msg)

make_messages(default_names,default_amounts)

#make_messages function with dates fixed. The output message will imply that all purchases were done today:
#To do so we have to import the datetime package: BEST PRACTICE IS TO LOAD IT AT THE START OF A SCRIPT.

import datetime

default_names = ["Justin", "John", "Emilee", "Jim", "Ron", "Sandra", "Veronica","Whitney"]
default_amounts = [123.32,94.23,124.32,323.4,23,323.122323,32.4,99.99]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it.Just as a 
reminder the purchase total was ${total}.
Have a great one!

Team CFE
"""

def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		today = datetime.date.today()
		text = "{today.day}/{today.month}/{today.year}".format(today=today)
		for name in names:
			new_amount = "%.2f" %(amounts[i])
			new_msg = unf_message.format(
				name = name,
				date = text,
				total = new_amount
				)
			i += 1
			print(new_msg)

 