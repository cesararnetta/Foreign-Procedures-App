import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.getenv("MAIL_SENDER")
EMAIL_PASSWORD = os.getenv("APP_MAIL_KEY")

msg = EmailMessage()
msg.set_content('Este es un correo de prueba')
msg['Subject'] = 'Prueba SMTP'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print('Correo enviado')
except Exception as e:
    print('Error:', e)