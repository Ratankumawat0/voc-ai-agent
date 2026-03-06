import schedule
import time
from main import run_agent

schedule.every().week.do(run_agent)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)