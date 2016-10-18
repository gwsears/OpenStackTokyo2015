import csv
import requests
from bs4 import BeautifulSoup

#First lets get the urls we'll use from the csv.
urls = open('urls.txt', 'r')
urlList = []
for line in urls:
    urlList.append(line)
print(urlList)

#start a csv file for output
outputTitle = 'SpeakerBlurbs.csv'
csvFile = open(outputTitle, 'w+', encoding='utf-8', newline='')
outputWriter = csv.writer(csvFile)
outputWriter.writerow(['URL','Blurb'])

#Now lets process each URL one by one
for url in urlList:
    urlClean = url.strip()
    print(urlClean)
    page = requests.get(urlClean, auth=('user', 'pass'))
    html = page.text
    bsObj = BeautifulSoup(html)
    blurb = bsObj.find("div",{"id":"sched-page-me-profile-about"})
    outputWriter.writerow([urlClean,blurb])