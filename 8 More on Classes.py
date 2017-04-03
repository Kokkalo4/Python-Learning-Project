#MORE ON CLASSES:
#Now we have put a second arguement on get color definition and we will see how we are going to make it work with second arguement:
class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self,abc)
		return self.color
	def make_noise(self)
		return self.noise

dog = Animal()
dog.get_color()

#When we try to pass the above code to python we get an error. self on get_color() function is a built in python function and is refered to whatever object we are going to pass that arguement into, in this case 
#dog.
#So in this case when we run the dog.get_color() we receive a message that a positional arguement is missing. This error referes to abc arguement we have specified above(since self is built-in python).
#To avoid this error for every function we are going to create we do the following:
#We first set keyword arguements:

#arg = Positional Arguements
#kwarg = Keyword Arguements
#IF YOU HAVE ARGUEMENTS NOT LINKED TO ANYTHING THEN THEY MUST BE PASSED:
abc = "some string"
def some_funct(arg_1,arg_2,kwarg_1=None, kwarg_2=None):
	print(arg_1,arg_2)
	if kwarg_1 != None:
		print(kwarg_1)

some_funct("abc","dalf",kwarg_1 = "nothing but")

#Another example similar with the above function: 
#This time we assume that we are sending an e-mail:
#This function contrary to the one above has more clear arguements and its easier for us to understand.
email_address = "another@gmail.com"
to_list = ["abc@gmail.com"]
from_list = ["another2@gmail.com","hello@teamcfe.com"]

def send_email(email=email_address,to_list=to_list,from_list=from_list):
	pass

send_email(email="another@gmail.com",to_list=["abc@gmail.com"],from_list=["another2@gmail.com","hello@teamcfe.com"])

#Based on all of the above the correct function to do the first function on line 9 would be:
class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self,abc):
		return self.color + " " + abc
	def make_noise(self):
		return self.noise

dog = Animal()
dog.get_color("red")

#Turning functions to Properties(similar to what we set in the class before creating the function):
#This turns the make_noise into a method:
class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self,abc):
		return self.color + " " + abc
	@property
	def make_noise(self):
		return self.noise

dog = Animal()
dog.get_color("red")

#and we can run:
dog.make_noise
#with the parenthesis.