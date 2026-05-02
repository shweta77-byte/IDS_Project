import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import win32evtlog
import time
import threading

server = 'localhost'
log_type = 'System'

event_counter = {}
seen_events = set()

# Counters
total_events = 0
alert_count = 0

def monitor_logs():
    global total_events, alert_count

    while True:
        handle = win32evtlog.OpenEventLog(server, log_type)

        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(handle, flags, 0)

        for event in events:
            event_id = event.EventID & 0xFFFF
            record_id = event.RecordNumber

            # Skip already processed events
            if record_id in seen_events:
                continue

            seen_events.add(record_id)

            source = event.SourceName
            timestamp = event.TimeGenerated.Format()

            # Update total count
            total_events += 1
            total_label.config(text=f"Total Events: {total_events}")

            # Count occurrences
            if event_id not in event_counter:
                event_counter[event_id] = 0
            event_counter[event_id] += 1

            # Default message
            tag = "info"
            message = f"[INFO] {timestamp} | Event ID: {event_id} | {source}\n"

            # 🔍 Detection rules
            if event_id in [41, 566, 6008]:
                message = f"[CRITICAL] {timestamp} | SYSTEM CRASH DETECTED\nEvent ID: {event_id} | {source}\n"
                tag = "critical"
                alert_count += 1

            elif event_id == 4199:
                message = f"[WARNING] {timestamp} | NETWORK ISSUE DETECTED\nEvent ID: {event_id} | {source}\n"
                tag = "warning"
                alert_count += 1

            elif event_id == 17:
                message = f"[SECURITY] {timestamp} | TPM EVENT\nEvent ID: {event_id} | {source}\n"
                tag = "security"

            # 🔥 Pattern detection
            if event_counter[event_id] >= 5:
                message = f"[ALERT] {timestamp} | REPEATED EVENT DETECTED ({event_id})\n"
                tag = "alert"
                alert_count += 1
                event_counter[event_id] = 0

            # Update alert counter
            alert_label.config(text=f"Alerts: {alert_count}")

            # Add separator
            message += "-" * 60 + "\n"

            # Insert into GUI
            log_box.insert(tk.END, message, tag)
            log_box.yview(tk.END)

        # Limit log size
        if float(log_box.index('end')) > 200:
            log_box.delete("1.0", "50.0")

        time.sleep(5)

# GUI setup
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("800x500")

# 📊 Top dashboard
stats_frame = tk.Frame(root)
stats_frame.pack(fill=tk.X)

total_label = tk.Label(stats_frame, text="Total Events: 0", font=("Arial", 12))
total_label.pack(side=tk.LEFT, padx=10)

alert_label = tk.Label(stats_frame, text="Alerts: 0", font=("Arial", 12))
alert_label.pack(side=tk.RIGHT, padx=10)

# 🖥️ Log display
log_box = ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10))
log_box.pack(fill=tk.BOTH, expand=True)

# 🎨 Color tags
log_box.tag_config("info", foreground="black")
log_box.tag_config("warning", foreground="orange")
log_box.tag_config("critical", foreground="red")
log_box.tag_config("security", foreground="blue")
log_box.tag_config("alert", foreground="purple")

# Run monitoring in background
thread = threading.Thread(target=monitor_logs, daemon=True)
thread.start()

root.mainloop()
