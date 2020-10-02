import time
import os

print("Hello World!")
print("env secret:", os.getenv('SECRET'))
print("chars of env secret:")
for c in os.getenv('SECRET'):
  print(c)
print("Working...")
time.sleep(5)
print("Work finished!")
