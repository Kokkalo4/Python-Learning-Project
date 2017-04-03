#Class Basics:

#Define a class and run through it:
class Dog():
	name = "Jon"
	color = "Brown"

#To see what is inside class Dog we type:
Dog
#or
Dog()
#Note when we use Dog when creating a class that becomes an object:

instance = Dog()
obj = Dog()

#Now that we have named instance after our class we can get: 
#Name with:
instance.name
#Color with:
instance.color

#REMEMBER: WHEN WE CHANGE AN INSTANCE OF A CLASS IT DOES NOT AFFECT THE CLASS ITSELF, eg if we change the instance.name to "Bob" it wont change to Dog() name to "Bob" too.

#Based on what we did above, we are going to merge what we did above with a function.
class Dog():
	name = "Jon"
	color = "Brown"

	def get_color(self):
		return self.color

obj = Dog()
obj.get_color()

#Not that on the function we set a variable self but when we printed out the obj.get_color() function we didnt specify anything in the parenthesis. That is because the obj is always refered to the specific class it 
#is merged with.
#If we type Dog.get_color() it will return an error because we didnt specify anything in the parenthesis. 
#We can change the attributes of an instance as follows:
obj.color = "white"
obj.get_color()



#Inheritance:
#First we are going to create a class named Animals and then we are going to have the class dog inherit from the class animals:
class Animal():
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"

	def get_color(self):
		return self.color

	def make_noise(self):
		return self.noise

dog = Animal()
dog.get_color()
dog.make_noise()
#We can change what we have created on Animal() on the instance level(in this case dog = Animal()) but we might want to apply this on the whole range of things:
#In order to do that we inherit the animal class we created above into the Dog() class we have below:
class Dog(Animal):
	name = "Jon"

jon = Dog()
dog.color = "white"
dog.name = "Jon Snow"
#So what happens is that Dog() class inherits all the unspecified attributes from the Animal class specified above. IMPORTANT: Dog() inherits from Animals() but nothing is changed on Animals() specified above.
#Also, what is created inside Dog() overrides what is specified inside of Animals().
dog.size
dog.hair
dog.noise


