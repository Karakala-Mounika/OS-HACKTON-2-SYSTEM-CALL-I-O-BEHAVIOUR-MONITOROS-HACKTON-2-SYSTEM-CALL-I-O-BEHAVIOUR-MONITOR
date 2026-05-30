import psutil
import time
import matplotlib.pyplot as plt

# Input multiple PIDs
pid_input = input("Enter PIDs (comma separated): ")
pid_list = [int(pid.strip()) for pid in pid_input.split(",")]

processes = {}
for pid in pid_list:
    try:
        processes[pid] = psutil.Process(pid)
    except:
        print(f"Invalid PID: {pid}")

# Store data
write_data = {pid: [] for pid in processes}
time_data = list(range(10))
prev_write = {pid: 0 for pid in processes}

print("\nMonitoring multiple processes...\n")

# Monitoring loop
for i in range(10):
    print(f"\nIteration {i+1}")

    for pid, process in processes.items():
        try:
            io = process.io_counters()
            write_bytes = io.write_bytes

            diff = write_bytes - prev_write[pid]

            print(f"PID {pid} → Write: {write_bytes}")

            # 🔥 Analysis per process
            if diff > 500:
                print(f"PID {pid} 🚀 High I/O")
            elif diff < 100:
                print(f"PID {pid} ⚠️ Small writes")
            else:
                print(f"PID {pid} ✅ Normal")

            write_data[pid].append(write_bytes)
            prev_write[pid] = write_bytes

        except:
            print(f"PID {pid} ended")
            write_data[pid].append(0)

    time.sleep(1)

# 📊 Graph for multiple PIDs
for pid in write_data:
    plt.plot(time_data, write_data[pid], label=f"PID {pid}")

plt.xlabel("Time (seconds)")
plt.ylabel("Write Bytes")
plt.title("Multi-Process I/O Monitoring")
plt.legend()
plt.show()

print("\nMonitoring completed")