
# InfraWatch

### Linux Infrastructure Monitoring System

InfraWatch is a Linux infrastructure monitoring system designed to monitor system health, collect infrastructure metrics, visualize performance data, detect resource threshold violations, and generate automated health reports.

The project combines a Python-based monitoring layer using `psutil` with **Node Exporter, Prometheus, and Grafana** to provide system monitoring and visualization.

**Tech Stack:** Python • psutil • Linux • Node Exporter • Prometheus • Grafana • systemd

---

## Overview

Linux systems continuously generate information about CPU, memory, disk, network activity, system load, uptime, and running processes.

InfraWatch provides an automated monitoring workflow that collects these metrics, visualizes them through Grafana, checks selected resources against configurable thresholds, records alerts, and generates system health reports.

The project uses two complementary monitoring paths:

* **Python + psutil** for direct system monitoring, threshold checks, alerts, logging, and health reports.
* **Node Exporter + Prometheus + Grafana** for continuous metric collection and visualization.

The monitoring components are configured to run as Linux `systemd` services, allowing the system to operate continuously in the background.

---

## Problem Statement

Monitoring Linux infrastructure manually makes it difficult to continuously track resource utilization and identify abnormal system conditions.

CPU, memory, disk, network activity, and system load can change continuously. Without automated monitoring, identifying high resource utilization and maintaining a record of system health can become difficult.

InfraWatch addresses this by automating metric collection, visualization, threshold-based checks, alert logging, and health report generation.

---

## Objectives

* Monitor CPU, memory, and disk utilization.
* Monitor network activity and system load.
* Monitor system uptime and running processes.
* Collect Linux system metrics continuously.
* Visualize infrastructure metrics using Grafana.
* Store time-series metrics using Prometheus.
* Detect high CPU, memory, and disk utilization.
* Generate timestamped alerts for threshold violations.
* Generate structured Linux health reports.
* Maintain monitoring and alert logs.
* Run monitoring components continuously using Linux `systemd`.
  

## Architecture

InfraWatch uses two complementary monitoring paths on the Linux system.

```text
                         Ubuntu Linux System
                                  |
                    +-------------+-------------+
                    |                           |
                    v                           v
             Node Exporter                Python + psutil
                 Port 9100                      |
                    |                    +-------+-------+
                    v                    |       |       |
               Prometheus               v       v       v
                 Port 9090           Alerts  Reports  Logs
                    |
                    v
                 Grafana
                 Port 3000
                    |
                    v
            Monitoring Dashboard
```

### Monitoring Pipeline

```text
Linux System
     |
     v
Node Exporter
     |
     v
Prometheus
     |
     v
Grafana
     |
     v
Dashboard
```

Node Exporter exposes Linux system metrics, Prometheus collects and stores these metrics as time-series data, and Grafana uses Prometheus as a data source to visualize the metrics.

### Python Monitoring Pipeline

```text
Linux System
     |
     v
Python + psutil
     |
     +----> CPU / Memory / Disk
     |
     +----> Network Activity
     |
     +----> System Load
     |
     +----> Uptime
     |
     +----> Running Processes
     |
     +----> Threshold Checks
                 |
                 +----> Alerts
                 |
                 +----> Health Reports
                 |
                 +----> Logs
```

The Python monitoring layer directly collects system information using `psutil`. CPU, memory, and disk usage are evaluated against configured thresholds. When a threshold is exceeded, InfraWatch records a timestamped alert.

---

## How It Works

### 1. System Metric Collection

The Linux system generates information about resource utilization and system activity.

InfraWatch collects the following metrics:

* CPU utilization
* Memory utilization
* Disk utilization
* Network data sent
* Network data received
* 1-minute system load
* 5-minute system load
* 15-minute system load
* System uptime
* Running process count

### 2. Node Exporter

Node Exporter collects Linux system-level metrics and exposes them in a format that Prometheus can scrape.

Node Exporter runs on:

```
localhost:9100
```

### 3. Prometheus

Prometheus periodically scrapes metrics exposed by Node Exporter and stores them as time-series data.

The current scrape interval is:

```
15 seconds
```

### 4. Grafana

Grafana connects to Prometheus and queries the collected time-series data using PromQL.

The InfraWatch dashboard visualizes:

* CPU usage
* Memory usage
* Disk usage
* Network receive traffic
* Network transmit traffic
* System load
* System uptime

Grafana runs on:

```
http://localhost:3000
```

### 5. Python Monitoring

The Python monitoring application uses `psutil` to directly collect system metrics.

The main monitoring loop runs every:

```
15 seconds
```

The collected values are passed to the health-check, alert, logging, and reporting components.

### 6. Threshold Checks

InfraWatch currently applies thresholds to:

* CPU usage
* Memory usage
* Disk usage

The configured threshold is:

```
CPU    : 80%
Memory : 80%
Disk   : 80%
```

Network activity, system load, uptime, and process count are monitored and included in reports but do not currently generate alerts.

### 7. Alert Generation

When CPU, memory, or disk usage exceeds its configured threshold, InfraWatch creates a timestamped alert.

Alerts are stored in:

```
alerts/alerts.log
```

Example:

```
[2026-09-21 12:04:00] High CPU usage: 90%
```

### 8. Health Report Generation

After collecting the system metrics, InfraWatch generates a structured health report containing resource utilization, network activity, system load, uptime, process count, and threshold status.

The report is stored in:

```
reports/health_report.txt
```

## Technology Stack

| Technology        | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| **Python**        | Monitoring logic, health checks, alerts, and report generation |
| **psutil**        | Collecting system-level metrics                                |
| **Node Exporter** | Exposing Linux system metrics                                  |
| **Prometheus**    | Collecting and storing time-series metrics                     |
| **Grafana**       | Visualizing infrastructure metrics                             |
| **Ubuntu Linux**  | Monitoring environment                                         |
| **systemd**       | Running monitoring components as background services           |
| **Git / GitHub**  | Version control and project documentation                      |

---

## Features

### System Monitoring

InfraWatch monitors the following Linux system metrics:

* CPU utilization
* Memory utilization
* Disk utilization
* Network data sent
* Network data received
* 1-minute system load
* 5-minute system load
* 15-minute system load
* System uptime
* Running process count

### Threshold-Based Alerting

Configurable thresholds are implemented for:

* CPU usage
* Memory usage
* Disk usage

When a configured threshold is exceeded, InfraWatch generates a timestamped alert and stores it in the alert log.

### Time-Series Monitoring

Prometheus continuously collects metrics exposed by Node Exporter and stores them as time-series data.

This allows infrastructure metrics to be observed over time rather than only as individual readings.

### Grafana Visualization

Grafana provides a dashboard for visualizing:

* CPU usage
* Memory usage
* Disk usage
* Network receive traffic
* Network transmit traffic
* System load
* System uptime

### Automated Health Reports

InfraWatch generates a structured health report containing:

* Current resource utilization
* Network activity
* System load
* System uptime
* Running process count
* Threshold status
* Overall system health status

### Application and Alert Logging

The monitoring application maintains logs of collected metrics, while threshold violations are stored separately in the alert log.

### Background Service Execution

InfraWatch and the supporting monitoring components are configured to run using Linux `systemd`, allowing the monitoring system to operate continuously in the background.


### 9. Continuous Operation

The monitoring components are configured as Linux `systemd` services.

This allows the services to start automatically and continue operating in the background without requiring the monitoring applications to be launched manually each time.

## Project Structure

The project is organized into separate components for monitoring, alerting, logging, reporting, and Prometheus configuration.

```text
infrawatch/
│
├── README.md
├── requirements.txt
│
├── monitoring/
│   ├── main.py
│   ├── health_check.py
│   ├── config.py
│   ├── alerts.py
│   └── reports.py
│
├── alerts/
│   └── alerts.log
│
├── logs/
│   └── infrawatch.log
│
├── reports/
│   └── health_report.txt
│
└── prometheus/
    └── prometheus-3.14.0.linux-amd64/
```

### Directory and File Description

| File / Directory   | Description                                                                             |
| ------------------ | --------------------------------------------------------------------------------------- |
| `monitoring/`      | Contains the Python monitoring application                                              |
| `main.py`          | Main monitoring loop that coordinates metric collection, alerts, logging, and reporting |
| `health_check.py`  | Collects system metrics using `psutil`                                                  |
| `config.py`        | Stores configurable resource thresholds                                                 |
| `alerts.py`        | Performs threshold checks and records alerts                                            |
| `reports.py`       | Generates the system health report                                                      |
| `alerts/`          | Stores threshold-based alert logs                                                       |
| `logs/`            | Stores InfraWatch application logs                                                      |
| `reports/`         | Stores generated system health reports                                                  |
| `prometheus/`      | Contains the Prometheus monitoring setup                                                |
| `requirements.txt` | Lists Python dependencies                                                               |
| `README.md`        | Project documentation                                                                   |

---

## Monitoring Components

InfraWatch consists of several components that work together to provide system monitoring.

### Python Monitoring Application

The Python application is the main custom component of InfraWatch.

It uses `psutil` to collect system-level information directly from the Linux operating system.

The application consists of the following modules:

#### `main.py`

`main.py` acts as the main controller for the monitoring application.

It:

1. Collects system metrics.
2. Performs threshold checks.
3. Records monitoring information.
4. Generates a health report.
5. Displays alert information.
6. Repeats the monitoring cycle at a configured interval.

The current monitoring interval is **15 seconds**.

#### `health_check.py`

`health_check.py` contains functions responsible for collecting system metrics using `psutil`.

The module collects:

```
CPU Usage
Memory Usage
Disk Usage
Network Activity
System Load
System Uptime
Running Process Count
```

#### `config.py`

`config.py` contains the configurable resource thresholds used by the alerting system.

Current values:

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
```

Keeping these values in a separate configuration file allows the thresholds to be changed without modifying the monitoring logic.

#### `alerts.py`

`alerts.py` performs threshold checks for CPU, memory, and disk utilization.

When a value exceeds its configured threshold, the module creates a timestamped alert and writes it to:

```
alerts/alerts.log
```

#### `reports.py`

`reports.py` generates a structured Linux health report.

The report includes:

* Resource utilization
* Network activity
* System load
* System uptime
* Running processes
* Threshold status
* Overall system status

The generated report is stored in:

```
reports/health_report.txt
```

---

### Node Exporter

Node Exporter provides Linux system metrics in a format that Prometheus can collect.

It runs as a Linux service and exposes metrics on:

```
localhost:9100
```

---

### Prometheus

Prometheus collects metrics from Node Exporter and stores them as time-series data.

The current configuration uses a **15-second scrape interval**.

Prometheus is used as the data source for Grafana.

---

### Grafana

Grafana provides the visualization layer of InfraWatch.

It connects to Prometheus and displays infrastructure metrics through a dashboard.

The dashboard currently contains panels for:

* CPU usage
* Memory usage
* Disk usage
* Network receive
* Network transmit
* System load
* System uptime

Grafana runs locally on:

```
http://localhost:3000
```

---

### systemd

Linux `systemd` is used to run the monitoring components as background services.

The current environment includes services for:

```
Node Exporter
Prometheus
Grafana
InfraWatch
```

This allows the monitoring system to continue operating without requiring each application to be manually started from a terminal.

## Alert System

InfraWatch includes a threshold-based alerting mechanism for detecting high resource utilization.

The alerting system currently monitors:

* CPU usage
* Memory usage
* Disk usage

The thresholds are defined in `monitoring/config.py`:

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
```

When a monitored value exceeds its configured threshold, InfraWatch generates a timestamped alert.

### Alert Workflow

```text
System Metrics
      |
      v
Threshold Check
      |
      +---- Within Limit ----> No Alert
      |
      +---- Above Limit -----> Generate Alert
                                      |
                                      v
                              alerts/alerts.log
```

### Example Alert

```text
[2026-09-21 12:04:00] High CPU usage: 90%
```

Alerts are stored in:

```text
alerts/alerts.log
```

The alert system is intentionally implemented as a local log-based mechanism. No external notification service is currently used.

---

## Health Reports

InfraWatch automatically generates a structured health report after each monitoring cycle.

The report provides a snapshot of the current Linux system health.

### Report Information

The report includes:

* Report generation timestamp
* Host information
* Overall system status
* CPU utilization
* Memory utilization
* Disk utilization
* Network data sent
* Network data received
* 1-minute system load
* 5-minute system load
* 15-minute system load
* System uptime
* Running process count
* CPU threshold status
* Memory threshold status
* Disk threshold status

### Health Status

CPU, memory, and disk values are compared with their configured thresholds.

If all three resources are within their configured limits, the report shows:

```
Overall Status : HEALTHY
```

If one or more configured thresholds are exceeded, the report shows:

```
Overall Status : WARNING
```

### Report Location

Generated reports are stored in:

```
reports/health_report.txt
```

The report is overwritten with the latest health information during each monitoring cycle.

---

## Logging

InfraWatch maintains separate logs for general monitoring activity and threshold-based alerts.

### Application Log

The application log records information collected during the monitoring cycle.

Location:

```
logs/infrawatch.log
```

The log can contain information such as:

```
CPU usage
Memory usage
Disk usage
Network activity
System load
Running process count
```

Example:

```
Metrics collected - CPU: 21.4%, Memory: 42.1%, Disk: 31.7%, Network Sent: 125.32 MB, Network Received: 842.51 MB, Load: 0.48, Processes: 186
```

### Alert Log

Threshold violations are recorded separately in:

```
alerts/alerts.log
```

Example:

```
[2026-09-21 12:04:00] High CPU usage: 90%
```

Separating application logs from alert logs makes it easier to distinguish normal monitoring activity from threshold violations.


## Grafana Dashboard

InfraWatch uses Grafana to visualize Linux infrastructure metrics collected by Prometheus.

The dashboard provides a real-time view of system resource utilization and system activity.

### Dashboard Overview

The dashboard contains the following panels:

| Panel            | Description                          |
| ---------------- | ------------------------------------ |
| CPU Usage        | Displays current CPU utilization     |
| Memory Usage     | Displays current memory utilization  |
| Disk Usage       | Displays root filesystem utilization |
| Network Receive  | Displays incoming network traffic    |
| Network Transmit | Displays outgoing network traffic    |
| System Load      | Displays the 1-minute system load    |
| Uptime           | Displays system uptime               |

### Dashboard Layout

The dashboard is organized into three main sections:

```text
┌─────────────────────────────────────────────────────┐
│ CPU Usage │ Memory Usage │ Disk Usage              │
├─────────────────────────────────────────────────────┤
│ Network Receive       │ Network Transmit            │
├─────────────────────────────────────────────────────┤
│ System Load           │ Uptime                      │
└─────────────────────────────────────────────────────┘
```

### Prometheus Queries

Grafana uses PromQL queries to retrieve metrics from Prometheus.

#### CPU Usage

```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

This calculates CPU utilization by measuring the percentage of CPU time that is not idle.

#### Memory Usage

```promql
100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))
```

This calculates the percentage of memory currently being used.

#### Disk Usage

```promql
100 * (1 - (node_filesystem_avail_bytes{mountpoint="/",fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{mountpoint="/",fstype!~"tmpfs|overlay"}))
```

This calculates root filesystem utilization while excluding temporary and overlay filesystems.

#### Network Receive

```promql
rate(node_network_receive_bytes_total{device!="lo"}[5m])
```

This displays the rate of incoming network traffic while excluding the loopback interface.

#### Network Transmit

```promql
rate(node_network_transmit_bytes_total{device!="lo"}[5m])
```

This displays the rate of outgoing network traffic while excluding the loopback interface.

#### System Load

```promql
node_load1
```

This displays the Linux 1-minute system load average.

#### System Uptime

```promql
node_time_seconds - node_boot_time_seconds
```

This calculates the time elapsed since the system booted.

### Dashboard Configuration

The dashboard is configured with:

```text
Data Source      : Prometheus
Time Range       : Last 15 minutes
Refresh Interval : 15 seconds
```

Grafana runs locally on:

```text
http://localhost:3000
```

### Dashboard Screenshot

The final repository will include a screenshot of the completed InfraWatch Grafana dashboard.

![InfraWatch Grafana Dashboard](screenshots/grafana-dashboard.png)


## Installation and Setup

### Prerequisites

Before setting up InfraWatch, the Linux system should have:

* Ubuntu Linux
* Python 3
* Python virtual environment support
* Git
* Node Exporter
* Prometheus
* Grafana

The project is designed to run on a Linux system where the monitoring services can operate continuously in the background.

---

### Clone the Repository

Clone the project repository and enter the project directory:

```bash
git clone <repository-url>
cd infrawatch
```

---

### Create a Python Virtual Environment

InfraWatch uses a Python virtual environment to keep its dependencies isolated from the system Python installation.

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

### Install Python Dependencies

Install the Python dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

The Python monitoring layer uses `psutil` for collecting system-level metrics.

---

### Verify the Python Environment

Check the Python version:

```bash
python --version
```

Verify that `psutil` is available:

```bash
python -c "import psutil; print(psutil.__version__)"
```

---

## Configuration

InfraWatch uses separate configuration files for the Python monitoring application and Prometheus.

### Python Monitoring Configuration

Threshold values are defined in:

```text
monitoring/config.py
```

Current configuration:

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
```

These values determine when InfraWatch generates resource alerts.

For example, if CPU utilization exceeds `80%`, the alerting system generates a CPU warning.

---

### Prometheus Configuration

Prometheus is configured to collect metrics from Node Exporter.

The Prometheus configuration uses a scrape interval of:

```text
15 seconds
```

The monitoring targets include:

```text
Prometheus
Node Exporter
```

Node Exporter is available at:

```text
localhost:9100
```

Prometheus runs on:

```text
localhost:9090
```

---

### Monitoring Interval

The Python monitoring application currently performs a monitoring cycle every:

```text
15 seconds
```

The monitoring workflow is therefore approximately:

```text
Collect Metrics
      ↓
Check Thresholds
      ↓
Write Logs
      ↓
Generate Health Report
      ↓
Wait 15 Seconds
      ↓
Repeat
```

Prometheus independently scrapes Node Exporter every 15 seconds.

The two monitoring paths use the same interval but are independent processes, so their measurements are not guaranteed to occur at exactly the same instant.

---

## Service Configuration

InfraWatch is configured as a Linux `systemd` service so that the monitoring application can run continuously in the background.

The supporting monitoring services are also managed by `systemd`.

The environment contains:

```text
node_exporter
prometheus
grafana-server
infrawatch
```

Check the status of the services using:

```bash
systemctl status node_exporter
systemctl status prometheus
systemctl status grafana-server
systemctl status infrawatch
```

A successfully configured environment should show the required services as active and running.



