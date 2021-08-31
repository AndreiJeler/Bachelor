import smtplib

from env.environmentSingleton import EnvironmentSingleton
from email.message import EmailMessage
import imghdr


class EmailService:

    @staticmethod
    def send_activation(to_email, name):
        instance = EnvironmentSingleton.get_instance()
        gmail_user = instance["GMAIL_EMAIL"]
        gmail_pass = instance["GMAIL_PASSWORD"]

        sent_from = "Fitness app"
        to = to_email

        subject = 'Welcome to the app'

        msg = EmailMessage()

        msg['Subject'] = subject
        msg['From'] = sent_from
        msg['To'] = to
        msg.set_content("Welcome to the app " + name + " !!!")

        with open("resources/images/welcome.jpg", 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',
                           subtype=imghdr.what(None, img_data))

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_pass)
            # server.sendmail(sent_from, to, email_text)
            server.send_message(msg)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')

    @staticmethod
    def send_temp_password(to_email, password):
        instance = EnvironmentSingleton.get_instance()
        gmail_user = instance["GMAIL_EMAIL"]
        gmail_pass = instance["GMAIL_PASSWORD"]

        sent_from = "Fitness app"
        to = to_email

        subject = 'Password changed'

        msg = EmailMessage()

        msg['Subject'] = subject
        msg['From'] = sent_from
        msg['To'] = to
        msg.set_content(
            "Your password was changed, your temporary password is " + password
            + ". Please change it in the app as soon as possible!")

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_pass)
            # server.sendmail(sent_from, to, email_text)
            server.send_message(msg)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
