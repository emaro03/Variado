# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

email_user = 'ealmonter@ennova.com.do'
email_password = '70o27Rfnq01f'

clientes = {'Emanuel': 'emaro03@gmail.com', 'Rayniel': 'emanuel.almonte@hotmail.com'}
archivos = {'ejemplo1.txt': 'emaro03@gmail.com', 'ejemplo2.txt': 'emanuel.almonte@hotmail.com'}

for usuario, mails in archivos.items():
    email_send = (mails)
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ",".join(email_send)
    msg['Subject'] = 'PRUEBA'+ ' ' + usuario

    body = 'dafsdfdsafdsaf' + ' ' + usuario
    msg.attach(MIMEText(body,'html'))

    part = MIMEBase('application','octet-stream')
    part.set_payload((open(usuario,'rb')).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(usuario)))
    msg.attach(part)

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(email_user,email_password)
    mail.sendmail(email_user, email_send, msg.as_string())
    mail.quit()


# %%


