import smtplib

sender = "aneese421@gmail.com"
receiver = "muhammadanees7284@gmail.com"
password = "Dell5401silver"
subject = "Python Email Test"
body = "I wrote an Email through Python."

# header
message = f''' From: {sender}
To: {receiver}\n
Subject: {subject}\n
{body}
'''

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")