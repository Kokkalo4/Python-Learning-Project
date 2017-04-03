#Here we will create a Python module that will interact with Gmail and will send an e-mail for us:
#After setting up the account with Gmail(a new one just for the occassion) we are starting to work with our script:
#1) Import needed libraries
import smtplib as sm


#2) Importing the credentials that we need to send out an e-mail(these may vary by service)
host = "smtp.gmail.com"
port = 587
username = ".............."
password = ".............."
#Some additional information that will help us below. First is the username(or e-mail address the e-mail will be sent from), the second is the list of e-mails that the e-mail will go to(in this case is the same 
#e-mail that was sent from):
from_email = username
to_list = ["..........."]

#3) Setup a connection to the server:
email_conn = sm.SMTP(host, port)
#Test if we are connected with the following command(If the connection works the output on Python console will inform us about the success of our connection):
email_conn.ehlo()
#Start secure connection:
email_conn.starttls()
#Next we log in to the e-mail.Following the passing of the login command the output on the console should be accepted. Anything other than accepted means that we have an error:
email_conn.login(username, password)
#to quit a connection we can type:
email_conn.quit()

#Now we are ready to send an e-mail:

email_conn.sendmail(from_email, to_list, "Hello there this is an e-mail message")




#Another way that this can be is the following:
from smtplib import SMTP

email_conn2 = SMTP(host, port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username, password)
email_conn2.quit()
email_conn2.sendmail(from_email, to_list, "Hello there this is an e-mail message")

#HANDLING ERRORS(we will examine 2 different errors that might come up) :
#First case is wrong password. This function when there is an error with our password informs us that an error has occured:

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
try:
	ABC.login(username, "wrong password")
	ABC.sendmail(from_email, to_list, "Hello there this is an e-mail message")
except SMTPAuthenticationError:
	print("could not log in")
except:
	print("an error occured")
ABC.quit()


#Sending HTML e-mail messages, enhanced messages with Subject line:


#In order to work with HTML the e-mail we send we need to load additional python packages and then change this line:
email_conn.sendmail(from_email, to_list, "Hello there this is an e-mail message")
#all the rest remains the same:
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib as sm

host = "smtp.gmail.com"
port = 587
username = "................."
password = "................."
from_email = username
to_list = ["..............."]
#Set the message:
try:
	the_msg = MIMEMultipart("alternative")
	the_msg["Subject"] = "Hello There!!"
	the_msg["From"] = from_email
	#the_msg["To"] = to_list[0] #No need to use it in this script since we describe where to send message in the email_conn.sendmail() command(2nd arguement):

	plain_txt = "Testing the message"
	html_txt = """\
	<html>
		<head></head>
		<body>
		<p>Hey!<br>
		Testing this e-mail <b>Message</b>. Made by <a href="http://joincfe.com">Team CFE</a>
		</p>
		</body>
	</html>
	"""
	part_1 = MIMEText(plain_txt, "plain")
	part_2 = MIMEText(html_txt, "html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	#Check the message as string:
	#print(the_msg.as_string())
	email_conn = sm.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except sm.SMTPException:
	print("Error sending message")

















#Sending formatted mails to a set of users:
#Import from Converting function to class.
#In our previous function the user e-mail was optional when it came to importing data. In this we are going to create a place where we will put all the gathered e-mails:
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib as sm

host = "smtp.gmail.com"
port = 587
username = "alexpykok@gmail.com"
password = "superslow3713"
from_email = username
to_list = ["alexpykok@gmail.com"]


class MessageUser():
	user_details = []
	messages = []
	email_messages = []
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
				user_email = detail.get("email")
				if user_email:
					user_data = {
					"email":user_email,
					"message":new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)
			return self.messages
		return []
	def send_mail(self):
		self.make_messages()
		if len(self.email_messages) > 0:
			for detail in self.email_messages:
				user_email = detail["email"]
				user_message = detail["message"]
				try:
					the_msg = MIMEMultipart("alternative")
					the_msg["Subject"] = "Billing Update!!"
					the_msg["From"] = from_email
					the_msg["To"] = user_email
					part_1 = MIMEText(user_message, "plain")
					the_msg.attach(part_1)
					#Check the message as string:
					#print(the_msg.as_string())
					email_conn = sm.SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(username, password)
					email_conn.sendmail(from_email, [user_email], the_msg.as_string())
					email_conn.quit()
				except sm.SMTPException:
					print("Error sending message")
			return True
		return False

obj = MessageUser()

obj.add_user("John", 94.23, email="alexpykok@gmail.com")
obj.add_user("Justin", 123.32, email="alexpykok@gmail.com") 
obj.add_user("Emilee", 124.32, email="alexpykok@gmail.com")
obj.add_user("Jim", 323.4, email="alexpykok@gmail.com")
obj.add_user("Ron", 23, email="alexpykok@gmail.com")
obj.add_user("Sandra", 323.122323, email="alexpykok@gmail.com")
obj.add_user("Veronica", 32.4, email="alexpykok@gmail.com")
obj.add_user("Whitney", 99.99, email="alexpykok@gmail.com")

obj.get_details()
obj.send_mail()










#Using External Template Files with Context Data in Python
#The previous message that we created works fine, BUT it has the main message of the e-mail in-function and therefore cannot connect with any external messages. So what it actually does is simply
#send the e-mail messages from the in-built message inside the function.
#Now we are going to create a very basic python template that will have a link to a template, will check if template exists and then we will have a function that will render it.
#To do so we create a txt file that will include the message and will build a link on(the file is named message.txt).
import os

#method to read message
def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception("This is not a valid template path %s"%(file_path))
	return file_path

file_ = "C:/Users/Alex/Desktop/Python/Udemy - 30 Days of Python/message.txt"

print(get_template_path(file_)) #prints out the file path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()
print(get_template(file_)) #prints out message


#The messages are interactive with script and the means that if we change something inside the file it will change real time on our text as well.
template_text = get_template(file_).format(name="Justin", date="abc",total=None)

def render_context(template_string,context):
	return template_string.format(**context) #Two starts before context means that context is a dictionary.

file_ = "C:/Users/Alex/Desktop/Python/Udemy - 30 Days of Python/message.txt"
template = get_template(file_)
context = {
	"name":"Justin",
	"date":None,
	"total":"4056"
}
print(render_context(template, context))

#SAME WITH THE ABOVE WORKS ALSO WITH HTML DOCUMENTS.