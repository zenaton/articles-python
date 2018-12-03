import smtplib

from email.mime.text import MIMEText

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskSendEmailCampaign(Task, Zenatonable):

    def __init__(self, email_recipients, city):
        self.email_recipients = email_recipients
        self.city = city

    def handle(self):
        sender_user = '<Enter your gmail address here>'
        sender_password = '<Enter your gmail password here>'

        subject = '50% OFF Bahamas!'
        body = "Freezing in {}? It's the right time to plan vacations in Bahamas!".format(self.city.split(',')[0])

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_user
        formatted_recipients = ', '.join(self.email_recipients)
        message['To'] = formatted_recipients

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_user, sender_password)
        server.sendmail(sender_user, self.email_recipients, message.as_string())
        server.close()
        print('Sent Email Campaign to {}'.format(formatted_recipients))
        return True
