from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

user = "" # input your facebook username
pwd = "" # input your facebook password
user_find = re.compile(r'"/ajax/hovercard/user.php\?id=(\d+)"')


# Try the messaging function, I seem to be running into some problems, give it a go. I don't have test data :(
wall = True
message = True
driver = webdriver.Firefox()
driver.get("https://facebook.com")
driver.find_element_by_id('email').send_keys(user)
driver.find_element_by_id('pass').send_keys(pwd)
driver.find_element_by_id('loginbutton').click()
driver.get("https://www.facebook.com/events/birthdays/")
messenger_link = "https://m.facebook.com/messages/compose/?ids={}"
source = driver.page_source
soup = BeautifulSoup(source, 'lxml')
people = soup.find_all('div', class_='_tzn lfloat _ohe')
wall_elements = driver.find_elements_by_name("message")
empty_dict = []
dict_ = {}
for number in range(0, len(wall_elements)):
    dict_['Name'] = people[number].text
    dict_['Link'] = people[number].a.get('href')
    dict_['Wall'] = wall_elements[number]
    dict_['User'] = user_find.findall(str(people[number]))[0]
    empty_dict.append(dict_)
for peo in empty_dict:
    if wall is True:
        peo['Wall'].send_keys("Happy Birthday! {} :D".format(peo['Name']))
        peo['Wall'].send_keys(u'\ue007')
        time.sleep(5)
for peo in empty_dict:
    if message is True:
        driver.get(messenger_link.format(peo['User']))
        time.sleep(5)
        driver.find_element_by_name('body').send_keys("Happy Birthday! {}".format(peo['Name']))
        driver.find_element_by_name('Send').click()
