from monitoring.config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD
from datetime import datetime


def save_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] {message}"

    with open("alerts/alerts.log", "a") as file:
        file.write(alert_message + "\n")

    return alert_message


def check_cpu(cpu):
    if cpu > CPU_THRESHOLD:
        message = f"High CPU usage: {cpu}%"
        return save_alert(message)

    return None


def check_memory(memory):
    if memory > MEMORY_THRESHOLD:
        message = f"High memory usage: {memory}%"
        return save_alert(message)

    return None


def check_disk(disk):
    if disk > DISK_THRESHOLD:
        message = f"High disk usage: {disk}%"
        return save_alert(message)

    return None
