from app import app
import subprocess

@app.task()
def add(x: int, y: int) -> int:
    return x + y

@app.task()
def log_uptime(logfile_name: str) -> None:
    subprocess.run(f"uptime >> {logfile_name}", shell=True)
