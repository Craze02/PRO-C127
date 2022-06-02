import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
star_data = []
headers = ["Name","Distance","Mass","Radius"]

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
table = soup.find("table")

temp_list= []

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(temp_list)