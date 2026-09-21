import time

from monitoring.health_check import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_network_usage,
    get_system_load,
    get_uptime,
    get_process_count,
)

from monitoring.alerts import (
    check_cpu,
    check_memory,
    check_disk
)

from monitoring.reports import generate_report


def log_message(message):
    with open("logs/infrawatch.log", "a") as file:
        file.write(message + "\n")


def main():
    # Start monitoring cycle
    log_message("InfraWatch monitoring started")

    # Collect system metrics
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    network = get_network_usage()
    load = get_system_load()
    uptime = get_uptime()
    processes = get_process_count()
    log_message(
        f"Metrics collected - CPU: {cpu}%, "
        f"Memory: {memory}%, "
        f"Disk: {disk}%"
        f"Network Sent: {network['sent_mb']:.2f} MB, "
        f"Network Received: {network['received_mb']:.2f} MB, "
        f"Load: {load['1_min']:.2f}, "
        f"Processes: {processes}"
  )




    # Check for alerts
    alerts = []

    cpu_alert = check_cpu(cpu)
    if cpu_alert:
        alerts.append(cpu_alert)

    memory_alert = check_memory(memory)
    if memory_alert:
        alerts.append(memory_alert)

    disk_alert = check_disk(disk)
    if disk_alert:
        alerts.append(disk_alert)

    # Generate health report
    report = generate_report(cpu,memory,disk,network,load,uptime,processes)
    print(report)

    # Display and log alerts
    if alerts:
        print("Alerts:")

        for alert in alerts:
            print("-", alert)
            log_message(f"Alert detected: {alert}")

    else:
        print("Alerts: None")
        log_message("No alerts detected")

    # Finish monitoring cycle
    log_message("InfraWatch monitoring completed")


if __name__ == "__main__":
    while True:
        main()
        time.sleep(15)
