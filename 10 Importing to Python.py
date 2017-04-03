#We can Import previously created functions or modules for use by using the following commands:
#Note that they need to be on the same level as the ones where we are trying to import them.
#Some examples are the following:
from py_day_test import some_rando, make_messages

from py_day_mod.make_messages import MessageUser

from random.whatever import anything

#Then we can continue adding values.
#An example is after loading the previous exercise from 9 Converting Function to Class we can continue to import users:
obj = MessageUser()
obj.add_user("Abc", 123.32, email='hello@teamcfe.com')
obj.add_user("jOhn", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)
obj.get_details()

print(obj.make_messages())

