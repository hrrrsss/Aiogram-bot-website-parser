import sqlite3
import os

from bs4 import BeautifulSoup
import requests

from common.counter_of_cars import count_of_auto_in_db
from common.check_link_in_db import check_link
# from common.selenium_pars_number import search_number
from database.connect_db.add_data_car import add_auto


count_of_auto = count_of_auto_in_db()

folder = 'parsing/cars_html'
count_of_file = len([f for f in os.listdir(folder)])


links = check_link()

for num in range(count_of_file):
    with open(f'parsing/cars_html/car_{count_of_auto}.html', encoding='utf-8') as file:

        src = file.read()
        soup = BeautifulSoup(src, 'lxml')


        model_class = soup.find_all(class_="h1title word-break")
        city_class = soup.find_all(class_="board-view-user-mobile mt20 mb20")
        mileage_class = soup.find_all(class_="list-properties-span2")
        price_class = soup.find_all(class_="board-view-price price-currency")
        description_class = soup.find_all(class_="word-break mb20")
        number = 222

        model = [m.get_text(strip=True) for m in model_class][0]
        city = [c.get_text(strip=True, separator=" ") for c in city_class][0]
        mileage = mileage_class[-1].get_text(strip=True)
        price = price_class[0].get_text(strip=True)
        description = description_class[0].get_text(separator=' ', strip=True)

        add_auto(model, city, mileage, price, description, links[num], number)

        count_of_auto += 1