import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your Name here'
email['to'] = 'Receivers mail here'
email['subject'] = 'Test for automated Email Sender'

email.set_content(html.substitute({'name': 'Receivers name'}), 'html')
  
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yourmailhere@gmail.com', 'YourPasswordHere')
    smtp.send_message(email)