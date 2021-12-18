import time
from datetime import datetime
from selenium import webdriver
from urllib import request
from pythonping.executor import ResponseList
from pythonping import ping

url = input("Enter the URL: ")
refreshrate = int(input("Enter the refresh rate (seconds): "))
driver = webdriver.Chrome() #you can change your desired browser webdriver by switching out Chrome for Firefox for example (MAKE SURE YOUR HAVE THE PARTICULAR WEBDRIVER INSTALLED) 
driver.get("https://"+url)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
rl = ping(url, size=30, count=10)
print()
print("[%s]" % (current_time), "page loaded in %dms" % (rl.rtt_avg_ms))
print()

while True:
    time.sleep(refreshrate)
    driver.refresh()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    rl = ping(url, size=30, count=10)
    print("[%s]" % (current_time), "page refreshed in %dms" % (rl.rtt_avg_ms))
