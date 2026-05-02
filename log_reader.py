import win32evtlog
import winsound
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
from datetime import datetime

server = 'localhost'
log_type = 'System'   # Change to 'System' if not running as admin

# Open event log
handle = win32evtlog.OpenEventLog(server, log_type)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

# Important Event IDs (Security Monitoring)
IMPORTANT_EVENTS = {
    4624: "Successful Login",
    4625: "Failed Login",
    4688: "Process Created",
    4672: "Admin Privileges Assigned"
}

print("🔍 Monitoring Windows Logs...\n")

events = win32evtlog.ReadEventLog(handle, flags, 0)

for event in events:
    event_id = event.EventID & 0xFFFF   # Fixes weird ID values

    if event_id in IMPORTANT_EVENTS:
        print("=" * 50)
        print("⚠️ ALERT DETECTED!")
        print("Event Type:", IMPORTANT_EVENTS[event_id])
        print("Event ID:", event_id)
        print("Time:", event.TimeGenerated.Format())
        print("Source:", event.SourceName)
        print("=" * 50)

        # 🔊 Sound Alert
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    else:
        # Optional: comment this if you only want alerts
        print("Event ID:", event_id)
        print("Time:", event.TimeGenerated.Format())
        print("Source:", event.SourceName)
        print("-" * 40)