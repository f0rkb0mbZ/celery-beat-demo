from celery import shared_task
import subprocess

@shared_task
def add(x: int, y: int) -> int:
    return x + y

@shared_task
def log_uptime(logfile_name: str) -> None:
    subprocess.run(f"uptime >> {logfile_name}", shell=True)
