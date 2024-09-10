from django.test import TestCase
from django.core import mail


connection = mail.get_connection()

# Manually open the connection
connection.open()

# Construct an email message that uses the connection
email1 = mail.EmailMessage(
    "Hello",
    "Body goes here",
    "lanalarala@gmail.com",
    ["liraoharak@gmail.com"],
    connection=connection,
)
email1.send()  # Send the email

connection.close()