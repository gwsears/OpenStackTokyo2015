import csv
import requests
from bs4 import BeautifulSoup

url ='https://openstacksummitoctober2015tokyo.sched.org/speaker/vestival'
page = requests.get(url, auth=('user', 'pass'))
html = page.text
print(html)
bsObj = BeautifulSoup(html)
print(bsObj.h1)
# we want the contents of this div tag: div id="sched-page-me-profile-about"
print(bsObj.find("div",{"id":"sched-page-me-profile-about"}))