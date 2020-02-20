import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

INFO = []
REQUEST_URL = []
first_names = []
last_names = []
types = []
status = []
restaurants = []
tickets = []
dates = []
rows = zip(first_names, last_names, types, status, restaurants, tickets, dates)

with open('addresses.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    for row in readCSV:
        info = row[3]
        INFO.append(info)
        request_url = row[4]
        REQUEST_URL.append(request_url)
        
with open('meal_data.csv', 'a') as foo:
    foo = csv.writer(foo, delimiter=',', lineterminator='\n')

    total = len(REQUEST_URL)
    print(total)
    i = 1275

    URL = "URL"
    path = 'path'

    driver = webdriver.Chrome(executable_path = path)
    driver.get(URL)
    time.sleep(2)
    driver.find_element_by_id("login-username").send_keys("username")
    driver.find_element_by_id("login-password").send_keys("password")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print("Logged in!")
    time.sleep(2)
    
    while i < total:
        driver.get(REQUEST_URL[i])
        time.sleep(2)

        data = driver.find_elements_by_tag_name('td')
        length = (len(data)/7)
        j = 0

        while j < length:
##            print(data[j].text)
            types.append(data[0+(j*7)].text)
            status.append(data[1+(j*7)].text)
            restaurants.append(data[2+(j*7)].text)
            tickets.append(data[5+(j*7)].text)
            dates.append(data[6+(j*7)].text)
            j+= 1
            
        time.sleep(2)
        
        driver.get(INFO[i])
        time.sleep(2)
        info = driver.find_elements_by_class_name('property-value')
        number = len(info)
        z = 0
        while z < length:
##            print(info[z].text)
            first_names.append(info[0].text)
            last_names.append(info[1].text)
            z+= 1
        print(i, info[0].text, info[1].text)
        i += 1

    print(first_names, last_names, types, status, restaurants, tickets, dates)
    for row in rows:
        foo.writerow(row)
driver.quit()
