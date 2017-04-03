#Converting Function to Class:
#We are going to convert a previously created function to class.
#This is going to be dynamic since we are going to do so by selecting names and amounts from a list:
#To do so we do the following:

import datetime

class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
            } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []


#EXPLANATION OF CODE ABOVE:
#1) define a class that contains 2 empty lists as attributes of the class and a string base_message
#2) In order to add users we have the function below the class that contains a dictionary that will have 3 different keys with 3 different values. The first value will be the name, the second will be the amount
#and the third will be the date.

#Next we add users to the list:
obj = MessageUser()
obj.add_user("Justin", 123.32, email="hello@teamcfe.com") #we can only e-mail this user and not the others because only this user has e-mail.
obj.add_user("John", 94.23)
obj.add_user("Emilee", 124.32)
obj.add_user("Jim", 323.4)
obj.add_user("Ron", 23)
obj.add_user("Sandra", 323.122323)
obj.add_user("Veronica", 32.4)
obj.add_user("Whitney", 99.99)

obj.get_details()
obj.make_messages()



