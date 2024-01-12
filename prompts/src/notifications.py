import datetime
import os
import smtplib
from email.mime.text import MIMEText


def send_email(prompts: list[str]):
    from_email: str = os.getenv("SERVICE_EMAIL")
    from_password: str = os.getenv("SERVICE_EMAIL_PASSWORD")
    to_email: str = os.getenv("MY_EMAIL")

    subject: str = f"Journaling Prompt {datetime.datetime.today()}"
    message: str = f"Today is {datetime.datetime.today().weekday()}. The suggested journal prompts for today are: \n 1. {prompts[0]} \n 2. {prompts[1]} \n 3. {prompts[2]}"

    msg: MIMEText = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # Create SMTP session for sending the mail
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    # Login to gmail account
    gmail.login(from_email, from_password)
    # Send mail
    gmail.send_message(msg)
