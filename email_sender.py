from email.message import EmailMessage
import ssl
import smtplib
email_sender = ''
email_password = ''
email_reciver = 'cosipa6772@adosnan.com'

x = 5

while x > 0:
    subject = 'Eloeloelo'
    body = 'no witam serdecznie'
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context ) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_reciver,em.as_string())
    x-= 1