
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
