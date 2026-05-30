import psutil
import time

try:
    pid = int(input("Enter PID: "))
    process = psutil.Process(pid)
except:
    print("Invalid PID")
    exit()

print(f"\nMonitoring process: {pid}")

prev_write = 0
write_history = []

for i in range(10):
    try:
        io = process.io_counters()
        write_bytes = io.write_bytes
        read_bytes = io.read_bytes

        diff = write_bytes - prev_write

        print(f"\nIteration {i+1}")
        print(f"Read Bytes: {read_bytes}")
        print(f"Write Bytes: {write_bytes}")

        # 🔥 SMART ANALYSIS
        if diff > 500:
            print("🚀 High disk write activity")
        elif diff < 100:
            print("⚠️ Inefficient small writes")
        else:
            print("✅ Normal I/O usage")

        write_history.append(write_bytes)

        prev_write = write_bytes
        time.sleep(1)

    except:
        print("Process ended")
        break

# 📄 FINAL REPORT
print("\n===== FINAL REPORT =====")

if write_history:
    total = write_history[-1]

    if total < 1000:
        print("📉 Low disk usage detected")
    elif total < 5000:
        print("📊 Moderate disk usage detected")
    else:
        print("📈 High disk usage detected")

    print(f"Total Bytes Written: {total}")

print("Monitoring completed")