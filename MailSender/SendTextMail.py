import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server
smtp_server = "localhost"
smtp_port = 1025
smtp_username = "testsender01"
smtp_password = "testsender01"

# Set up the email content
sender = "testsender01@localhost"
receiver = "testrecipient@localhost"
subject = "Hello from testsender01"
message = """This is a test email.
MIME Type is text/plain.

これはテストメールです。
MIMEタイプはプレーンテキストです。
"""

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
# SMTP認証を使用しない場合、server.login()は不要
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    print("Email sent successfully")
