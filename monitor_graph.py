import psutil
import time
import matplotlib.pyplot as plt

pid = int(input("Enter PID: "))
process = psutil.Process(pid)

print(f"Monitoring process: {pid}")

write_data = []
time_data = []

prev_write = 0

for i in range(10):
    try:
        io = process.io_counters()
        write_bytes = io.write_bytes
        read_bytes = io.read_bytes

        diff = write_bytes - prev_write

        print(f"\nIteration {i+1}")
        print(f"Read Bytes: {read_bytes}")
        print(f"Write Bytes: {write_bytes}")

        if diff > 500:
            print("🚀 High I/O activity")
        elif diff < 100:
            print("⚠️ Inefficient small writes")
        else:
            print("✅ Normal I/O")

        write_data.append(write_bytes)
        time_data.append(i)

        prev_write = write_bytes
        time.sleep(1)

    except:
        print("Process ended")
        break

# 📊 GRAPH (IMPORTANT)
plt.plot(time_data, write_data)
plt.xlabel("Time (seconds)")
plt.ylabel("Write Bytes")
plt.title("Process I/O Monitoring")
plt.show()

print("\nMonitoring completed")