 Intrusion Detection System (IDS) using Python

Overview
This project is a real-time Intrusion Detection System (IDS) that monitors Windows Event Logs, detects suspicious activities, and displays alerts through a graphical dashboard.

It is designed to simulate basic Security Operations Center (SOC) monitoring.

 Features
- Real-time log monitoring  
- Event classification (INFO, WARNING, CRITICAL, SECURITY)  
- Pattern-based detection (repeated events)  
- GUI dashboard using Tkinter  
- Live event and alert counters  
- Timestamped logs  
- Deduplication of repeated events  


 Technologies Used
- Python  
- Tkinter (GUI)  
- pywin32 (Windows Event Logs)  
- Windows OS  

 How It Works
1. Reads Windows Event Logs (System logs)  
2. Extracts Event ID, Source, and Timestamp  
3. Applies detection rules:
   - System crash detection  
   - Network issue detection  
   - TPM security events  
4. Tracks repeated events (pattern detection)  
5. Displays results in a GUI dashboard with alerts  


 How to Run

1. Install dependencies
 bash
pip install pywin32
