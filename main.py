import win32evtlog
import time
import winsound

server = 'localhost'
log_type = 'System'

print("🚨 Smart IDS with Pattern Detection Running...\n")

# Store event counts
event_counter = {}

while True:
    handle = win32evtlog.OpenEventLog(server, log_type)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    events = win32evtlog.ReadEventLog(handle, flags, 0)

    for event in events[:10]:
        event_id = event.EventID & 0xFFFF
        source = event.SourceName

        # Count occurrences
        if event_id not in event_counter:
            event_counter[event_id] = 0
        event_counter[event_id] += 1

        # 🔍 Detection Rules
        if event_id in [41, 566, 6008]:
            print("🚨 SYSTEM CRASH DETECTED!")

        elif event_id == 4199:
            print("⚠️ NETWORK ISSUE DETECTED!")

        elif event_id == 17:
            print("🔐 TPM SECURITY EVENT")

        # 🔥 Pattern Detection (NEW)
        if event_counter[event_id] >= 5:
            print(f"🚨 REPEATED EVENT DETECTED! Event ID: {event_id}")
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            event_counter[event_id] = 0   # reset

        print("Event ID:", event_id, "| Source:", source)
        print("-" * 50)

    time.sleep(5)