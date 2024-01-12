import schedule
import time

from notifications import send_email
from prompt_generator import generate_prompt


def job():
    prompts: list[str] = generate_prompt()
    send_email(prompts)
    return


schedule.every().day.at("07:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
