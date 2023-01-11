from csv import writer
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=belts+for+men&sid=reh%2Cro3&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=belts+for+men%7CBelts&requestId=d8f49c0d-d341-4815-a97a-02d18069c737&as-backfill=on"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

ad_list = soup.find_all('div', class_="_1AtVbE col-12-12")

item_name = soup.find_all('div', class_="_2WkVRV")

# for i in item_name:
#     print(i.text)

item_desc = soup.find_all('a', class_="IRpwTa")

# for j in item_desc:
#     print(j.text)


# for i, j in zip(item_name, item_desc):
#     print(i.text + " => " + j.text)
#     print()

item_cost = soup.find_all('div', class_="_30jeq3")
item_mrp = soup.find_all('div', class_="_3I9_wc")
item_dscnt = soup.find_all('div', class_="_3Ay6Sb")


# for i, j, k, l, m in zip(item_name, item_desc, item_mrp, item_cost, item_dscnt):
#     print(i.text + " " + j.text + " " + k.text + " " + l.text + " " + m.text, end='\n')


with open('flip.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Desc', 'Price', 'MRP', 'Dscnt']
    thewriter.writerow(header)