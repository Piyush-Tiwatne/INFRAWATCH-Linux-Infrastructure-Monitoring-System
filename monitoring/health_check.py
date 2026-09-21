import psutil
import time


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent


def get_network_usage():
    network = psutil.net_io_counters()

    return {
        "sent_mb": network.bytes_sent / (1024 * 1024),
        "received_mb": network.bytes_recv / (1024 * 1024)
    }


def get_system_load():
    load = psutil.getloadavg()

    return {
        "1_min": load[0],
        "5_min": load[1],
        "15_min": load[2]
    }


import psutil
import time


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent


def get_network_usage():
    network = psutil.net_io_counters()

    return {
        "sent_mb": network.bytes_sent / (1024 * 1024),
        "received_mb": network.bytes_recv / (1024 * 1024)
    }


def get_system_load():
    load = psutil.getloadavg()

    return {
        "1_min": load[0],
        "5_min": load[1],
        "15_min": load[2]
    }


def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()

    uptime_seconds = current_time - boot_time

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return {
        "days": days,
        "hours": hours,
        "minutes": minutes
    }


def get_process_count():
    process_count = len(psutil.pids())

    return process_count
