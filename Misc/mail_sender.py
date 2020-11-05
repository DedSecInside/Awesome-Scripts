from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    """
    Return list of the contacts

    Args:
        filename: (str): write your description
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Reads a template from a file.

    Args:
        filename: (str): write your description
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

ADDRESS = "example@gmail.com"
PASSWORD = "example"

# set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(ADDRESS, PASSWORD)

# read email contacts and content
names, emails = get_contacts('mycontacts.txt')
message_template = read_template('message.txt')

# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']=ADDRESS
    msg['To']=email
    msg['Subject']="This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    
    del msg



