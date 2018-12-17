import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

user_name = input("Enter email user name:")
password = input("Enter email password:")
recipient = input("Enter recipient address:")
msg = MIMEMultipart()
msg['From'] = user_name
msg['To'] = recipient
msg['Subject'] = "This is a test email"
body = 'This is a test of Python email.'
msg.attach(MIMEText(body, 'plain'))
debuglevel = True

try:
    server = smtplib.SMTP('mail.hover.com', 587)
    #server.set_debuglevel(debuglevel)
    server.starttls()
    server.login(user_name, password)
    text = msg.as_string()
    server.sendmail(user_name, recipient, text)
    server.close()
    print ("Success - email sent!")

except:
    print ('something went wrong')
