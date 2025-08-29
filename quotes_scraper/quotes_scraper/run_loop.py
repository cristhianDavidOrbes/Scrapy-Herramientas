import time
import os

while True:
    os.system("scrapy crawl waste_ai -O quotes.csv")

    time.sleep(10)
