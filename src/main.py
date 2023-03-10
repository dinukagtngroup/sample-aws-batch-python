import sys

from logger import *

print('Hello World!')
count = 0

for i in range(100):
    count += i
print("Count is - " + str(count))

try:
    div = 10/0
except:
    tag_job_failure('Cannot divide by zero.')
    sys.exit()

tag_job_success()

