import os, time, sys
from selenium import webdriver
from urllib import request

refreshed_times = 0
url = str(sys.argv[1])
timer = int(sys.argv[2])
driver = webdriver.Firefox() #(Chrome/Firefox) - make sure you have the web driver installed!

driver.get(url)

while True:
    time.sleep(timer)
    driver.refresh()

    refreshed_times = refreshed_times + 1

    os.system("cls" if os.name=="nt" else "clear")

    print(f"{url} refreshes every {timer} seconds")
    print("refreshed times: ", refreshed_times)
    print()
    print("Press CTRL+C or close the browser/terminal window to stop.")
