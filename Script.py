import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import numpy as np

email_user = 'emaro03@gmail.com'
email_password = 'ikjglmdnfjbcffuj'

archivos = {r'C:\Users\Owner\Documents\GitHub\ENNOVA\Archivos de ejemplo\ejemplo1.txt': 'emaro03@gmail.com', r'C:\Users\Owner\Documents\GitHub\ENNOVA\Archivos de ejemplo\ejemplo2.txt': 'emaro03@gmail.com'}

for archivo, mails in archivos.items():
    email_send = (mails)
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ",".join(email_send)
    msg['Subject'] = 'Correo electrónico de prueba'

    body = 'Este sería el cuerpo del correo'
    msg.attach(MIMEText(body,'html'))

    part = MIMEBase('application','octet-stream')
    part.set_payload((open(archivo,'rb')).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(archivo)))
    msg.attach(part)

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(email_user,email_password)
    mail.sendmail(email_user, email_send, msg.as_string())
    mail.quit()