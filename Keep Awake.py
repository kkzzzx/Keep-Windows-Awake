import ctypes
import time

ES_DISPLAY_REQUIRED = 0x00000002
ES_SYSTEM_REQUIRED = 0x00000001
ES_CONTINUOUS = 0x80000000

print("Windows 11 Awake script is running...")
print("Close this window or press Ctrl+C to stop.")

try:
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )
    
    while True:
        time.sleep(300)

except (KeyboardInterrupt, SystemExit):
    print("\nScript stopped. Allowing the system to sleep again.")
finally:
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)