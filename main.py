from datetime import date, datetime, timedelta

import requests
from bs4 import BeautifulSoup

from database import *
from files import *
from webhook import *

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
today = datetime.now().strftime('%d')
url = f"https://pcampus.edu.np/{year}/{month}/{today}/"

def scraper():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    body = soup.find('body', class_="error404 group-blog")
    titles = []
    files_link = []

    if(not body):
        return
    
    titles_html = soup.find_all('h2', class_="entry-title")
    for title in titles_html:
        title = title.find('a').get_text()
        titles.append(title)

    files_html = soup.find_all('div', class_="entry-content")
    for file in files_html:
        link = file.find('a').get('href') if file.find('a') != None else url
        files_link.append(link)

    return(titles, files_link)

args = scraper()
if(args):
    titles = args[0]
    links = args[1]    

    if (links):
        readFromDB()

        for index, link in enumerate(links):
            filename = link.split("/")[-1]

            # filename is present in database then just continue
            if (titles[index] in open("sent_notice.txt", "r").read()):
                continue

            # sends pdf embedded message with preview images
            if (filename.__contains__(".pdf")):
                create_files(link, filename)
                status = embedWebHook(link, titles[index])
                if (status != 200):
                    continue
                addToDB(titles[index])

            # sends image embedded message
            elif (filename.__contains__(".jpg") or filename.__contains__(".jpeg")):
                status = imgWebhook(link, titles[index])
                if (status != 200):
                    continue
                addToDB(titles[index])

            # sends text embedded message
            else:
                status = textWebhook(url, titles[index])
                if (status != 200):
                    continue
                addToDB(titles[index])

            # deletes files from docs and images folder
            del_files()

updateDB()
