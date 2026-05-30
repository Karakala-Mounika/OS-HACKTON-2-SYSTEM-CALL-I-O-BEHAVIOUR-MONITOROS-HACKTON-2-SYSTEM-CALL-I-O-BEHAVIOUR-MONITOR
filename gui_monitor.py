import psutil
import time
import tkinter as tk
from tkinter import messagebox
import threading   # ✅ IMPORTANT

def monitor_process(pid):
    try:
        process = psutil.Process(pid)
    except:
        output.insert(tk.END, "Invalid PID\n")
        return

    prev_write = 0

    for i in range(10):
        try:
            io = process.io_counters()
            write_bytes = io.write_bytes
            diff = write_bytes - prev_write

            result = f"Iteration {i+1} | Write: {write_bytes}\n"

            if diff > 500:
                result += "🚀 High I/O\n"
            elif diff < 100:
                result += "⚠️ Small writes\n"
            else:
                result += "✅ Normal\n"

            output.insert(tk.END, result + "\n")
            output.see(tk.END)

            prev_write = write_bytes
            time.sleep(1)

        except:
            output.insert(tk.END, "Process ended\n")
            break

def start_monitor():
    try:
        pid = int(entry.get())
    except:
        messagebox.showerror("Error", "Enter valid PID")
        return

    output.delete(1.0, tk.END)

    # ✅ Run in background thread
    thread = threading.Thread(target=monitor_process, args=(pid,))
    thread.start()

# GUI Window
root = tk.Tk()
root.title("I/O Monitor Tool")

tk.Label(root, text="Enter PID:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Start Monitoring", command=start_monitor).pack()

output = tk.Text(root, height=15, width=50)
output.pack()

root.mainloop()