import time
import os

print("Program started...")
print("PID:", os.getpid())   # 👈 Use this PID in monitor

with open("test.txt", "w") as f:
    for i in range(1000):
        f.write("Hello World\n")
        f.flush()              # Force write
        os.fsync(f.fileno())   # Force OS disk write

        print(f"Writing line {i}")
        time.sleep(0.1)

print("Program finished") 