import time

from bs4 import BeautifulSoup
import requests

from common.check_link_in_db import check_link
from common.counter_of_cars import count_of_auto_in_db


def second_stage_func():
    links = check_link()

    headers = {
            "Accept": "*/*",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive"
        }


    count = count_of_auto_in_db()

    for link in links:

        req = requests.get(link, headers=headers)
        src = req.text

        with open(f"parsing/cars_html/car_{count}.html", "w", encoding="utf-8") as file:
            file.write(src)

        count += 1

        time.sleep(3)

    return links