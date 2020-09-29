import time
import os

print("Hello World!")
print("env secret:", os.getenv('SECRET'))
print("Working...")
time.sleep(5)
print("Work finished!")
