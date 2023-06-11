from email.message import EmailMessage
from pwd import password
import ssl
import smtplib

#Give sender Email here
email_sender = 'nithes2003@gmail.com'
email_password = password
#Give receiver Email here
email_receiver = ''

subject = "Don't know what to give"

body = """ 

Hello everyone,
Welcome to the email sender project
The sun dipped below the horizon, casting a warm golden 
glow across the tranquil ocean. 
Waves gently lapped against the shore, creating a soothing melody. 
Seagulls soared overhead, their graceful flight 
contrasting with the rugged cliffs that framed the picturesque scene.


"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

