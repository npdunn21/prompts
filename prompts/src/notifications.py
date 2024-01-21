import datetime
import os
import smtplib
from email.mime.text import MIMEText


_MAP_DAY_INT_TO_STR_DAY_OF_THE_WEEK = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def send_email(prompts: list[str]):
    from_email: str = os.getenv("SERVICE_EMAIL")
    from_password: str = os.getenv("SERVICE_EMAIL_PASSWORD")
    to_email: str = os.getenv("MY_EMAIL")

    subject: str = f"Journaling Prompt {datetime.datetime.today()}"
    message: str = (f"Today is {_MAP_DAY_INT_TO_STR_DAY_OF_THE_WEEK[datetime.datetime.today().weekday()]}. <br> The "
                    f"suggested journal prompts for today are: <br> {prompts[0]} <br> {prompts[1]} <br> {prompts[2]}")

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
