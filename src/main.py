import glob
import os
import sys

from logger import *

print('Hello World!')
count = 0

for i in range(100):
    count += i
print("Count is - " + str(count))


print(os.listdir('/'))
print(os.listdir('/usr'))
print(os.listdir('/usr/local'))
print(os.listdir('/usr/local/bin'))

for f in glob.glob('/', recursive=True):
    print(f)

print('OS Environment', os.environ)
# print('AWS Default Region', os.environ['AWS_DEFAULT_REGION'])

try:
    div = 10/0
except:
    tag_job_failure('Cannot divide by zero.')
    sys.exit()

tag_job_success()

