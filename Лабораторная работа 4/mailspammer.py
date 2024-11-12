import smtplib
from email.mime.text import MIMEText

sender = "zhizhevzhizhnik@gmail.com"
receiver = "zhizhevzhizhnik@gmail.com"
subject = "Test email"
body = "SMTPlib message"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender, "rvnh geof rajy tdbx")

server.sendmail(sender, receiver, msg.as_string())
server.quit()