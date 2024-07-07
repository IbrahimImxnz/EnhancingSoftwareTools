import psutil
import smtplib
from email.mime.text import MIMEText

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
EMAIL_TO = 'admin@example.com'
EMAIL_FROM = 'monitor@example.com'
SMTP_SERVER = 'smtp.example.com'

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())

def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    if cpu_usage > CPU_THRESHOLD:
        send_email('CPU Usage Alert', f'CPU usage is at {cpu_usage}%')

    if memory_usage > MEMORY_THRESHOLD:
        send_email('Memory Usage Alert', f'Memory usage is at {memory_usage}%')

if __name__ == "__main__":
    monitor_system()
