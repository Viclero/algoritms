import datetime
from urllib.parse import urlparse
import requests
from pathlib import WindowsPath


now = datetime.datetime.now()

then = datetime.datetime(2023, 1, 29, 13, 15, 30)

d = now-then

t = datetime.timedelta(hours=2, minutes=30)
print(now)
print(then)
h = int(d/datetime.timedelta(hours=1))
m = int(d/datetime.timedelta(minutes=1) - h*60)

# print( f'{h}ч {m}мин' )

inp_ll = '1,11,45,3,7,21,8'
print(*map(int, inp_ll.split(',')))
