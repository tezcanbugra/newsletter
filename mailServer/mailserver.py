import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()


sender_email = os.getenv("SENDER_EMAIL")


def send_email(message, receiver):

    passw = os.getenv('EMAIL_PASS')

    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, passw)
        for rec in receiver:
            server.sendmail(sender_email, rec, message)


