import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import os

def send_email(file_name):
    email_sender = 'mail.test.for.exmpl@gmail.com'
    email_pass = 'hbtvlzlkzgnelwcr'
    email_reciver = 'gnom51764@gmail.com'

    # grinjou9061@gmail.com

    subject = 'TEST'
    body = "TEST"

    msg = MIMEMultipart()
    em = EmailMessage()

    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        with open(f"shared/components/documents/pdfDocs/{file_name}", "rb") as f:
            file = MIMEApplication(f.read())
            msg.attach(file)

        file.add_header('content-disposition', 'attachment', filename=file_name)
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_reciver, msg.as_string())

