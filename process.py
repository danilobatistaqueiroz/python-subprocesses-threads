import subprocess
import time
process = subprocess.Popen(["./child.py", "run", ""], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
i = 1
while i < 4:
  print(process.stdout.readline())
  time.sleep(1)
  i+=1
out = process.communicate(input=b'abc')[0]
print(out)
time.sleep(3)