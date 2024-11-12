import smtplib
from email.mime.text import MIMEText

sender = "notmyemail@gmail.com"
receiver = "notmyemail@gmail.com"
subject = "Test email"
body = "SMTPlib message"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender, "nott myyy appp keyy")

server.sendmail(sender, receiver, msg.as_string())
server.quit()
