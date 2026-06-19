# Real-Time Intrusion Detection System (IDS) using Python

## Overview

This project implements a Real-Time Intrusion Detection System (IDS) for Windows systems using Python. The system monitors Windows Event Logs, analyzes system events, detects suspicious activities through rule-based and pattern-based techniques, and displays alerts through a graphical dashboard.

The objective of the project is to demonstrate practical applications of cybersecurity monitoring, log analysis, event classification, and anomaly detection.



## Project Objective

The main objectives of this project are:

* Monitor Windows Event Logs in real time.
* Analyze event information such as Event ID, source, and timestamp.
* Detect suspicious and repeated system events.
* Generate alerts for abnormal activities.
* Provide a graphical interface for monitoring and visualization.
* Demonstrate basic intrusion detection concepts used in cybersecurity operations.



## Features

* Real-time Windows Event Log monitoring
* Rule-based event detection
* Pattern-based anomaly detection
* Event classification
* Timestamped event tracking
* Graphical dashboard using Tkinter
* Event and alert counters
* Duplicate event filtering
* Continuous monitoring of system activity



## Technologies Used

* Python
* Tkinter
* pywin32
* Windows Event Logs
* Git
* GitHub



## System Architecture

Windows Event Logs → Log Reader Module → Detection Engine → Pattern Analysis Module → Alert Generation → GUI Dashboard



## Detection Methodology

### Rule-Based Detection

The system analyzes Windows Event Logs and classifies events based on predefined detection rules. Examples include:

* TPM-related security events
* Network-related events
* Critical system events
* Repeated system anomalies

### Pattern-Based Detection

The IDS tracks event frequencies and generates alerts when the same event occurs repeatedly within a monitoring session. This helps identify potentially abnormal behavior patterns.



## Dashboard Features

The graphical dashboard provides:

* Real-time event display
* Event classification
* Alert notifications
* Total event counter
* Alert counter
* Timestamped log entries
* Continuous monitoring interface



## Installation

### Install Required Dependency

```bash
pip install pywin32
```

### Run the Application

```bash
python gui.py
```


## Project Structure

```text
IDS_Project/
│
├── gui.py
├── main.py
├── log_reader.py
├── requirements.txt
├── README.md
└── screenshots/
    └── dashboard.png
```





### IDS Dashboard

![Dashboard](screenshots/dashboard.png)



## Law Enforcement Relevance

This project demonstrates how system event logs can be monitored and analyzed to identify suspicious activities and abnormal system behavior.

Potential applications include:

* Security monitoring
* Event log analysis
* Incident awareness
* Digital forensics support
* Cybercrime investigation assistance
* Security operations center (SOC) training and demonstrations



## Future Enhancements

Future improvements may include:

* Security log monitoring for authentication events
* Failed login detection
* Network traffic monitoring
* Automated report generation
* Machine learning-based anomaly detection
* Centralized monitoring capabilities
## Conclusion

This project demonstrates the implementation of a Real-Time Intrusion Detection System using Python. By combining Windows Event Log monitoring, event classification, pattern detection, and graphical visualization, the system provides a practical introduction to cybersecurity monitoring and intrusion detection concepts.
