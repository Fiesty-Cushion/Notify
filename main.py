import requests
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from files import *
from webhook import *
import os

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
yesterday =  str(date.today() - timedelta(days=1)).split('-')[-1]
url = f"https://pcampus.edu.np/{year}/{month}/{yesterday}/"

def scraper():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    body = soup.find('body', class_="error404 group-blog")
    titles = []
    files_link = []

    if(body != None):
        return
    
    if(body == None):
        titles_html = soup.find_all('h2', class_="entry-title")
        for title in titles_html:
            title = title.find('a').get_text()
            titles.append(title)

        files_html = soup.find_all('div', class_="entry-content")
        for file in files_html:
            link = file.find('a').get('href')
            files_link.append(link)

    return(titles, files_link)

args = scraper()
if(args != None):
    #os.system("ls")
    titles = args[0]
    links = args[1]

    if (links != None):
        for index, link in enumerate(links):
            filename = link.split("/")[-1]
            if (filename.__contains__(".pdf")):
                create_files(link, filename)
                status = embedWebHook(link, titles[index])
                if (status != 200):
                    continue
            elif (filename.__contains__(".jpg") or filename.__contains__(".jpeg")):
                status = imgWebhook(url, titles[index])
                if (status != 200):
                    continue
            else:
                status = textWebhook(url, titles[index])
                if (status != 200):
                    continue
            del_files()

    