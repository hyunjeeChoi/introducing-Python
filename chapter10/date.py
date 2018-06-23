from datetime import date

now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    output.write(now_str)

with open('today.txt', 'rt') as input:
    today_string = input.read()


import os
os.listdir('..')
