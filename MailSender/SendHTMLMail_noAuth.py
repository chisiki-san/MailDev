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
message = '''
<html>
  <head></head>
  <body>
    <h2>This is a test email.</h2>
    <p>MIME Type is text/html.</p>
    <h2>これはテストメールです。</h2>
    <p>MIMEタイプはハイパーテキストです。</p>
  </body>
</html>
'''

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

msg.attach(MIMEText(message, 'html'))

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
#    server.starttls()
#    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    print("Email sent successfully")
