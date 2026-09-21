
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
