import os
import os.path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import re
import time
from mostFreq import freq_dist_word


query = input("enter Query: ")
url_path = "https://www.google.co.in/search?q="+query+" filetype:pdf"
path_dir = "pdfData/"


def getPdf(url):
    try:
        if not os.path.exists(path_dir):
            os.makedirs('pdfData')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        docs_url = []

        for element in soup.find_all('div', attrs={'class': 'g'}):
            if element.find('span', {'class': 'mime'}):
                link = (element.find('a').get('href').replace("/url?q=",
                                                              "").split('&sa')[0])
                if ".pdf" in link:
                    docs_url.append(link)
        counter = 0
        print(len(docs_url))
        for doc in docs_url:
            counter += 1
            filename = os.path.join('pdfData/', str(counter)+".pdf")
            if not os.path.exists((filename)):
                req = Request(str(doc), headers={'User-agent': 'Mozilla/5.0'})
                time.sleep(5)
                res = (urlopen(req).read())
                # data = re.sub('[^A-Za-z0-9]+', ' ', res)
                with open(filename, 'wb+') as f:
                    f.write(res)
                print(counter, ".pdf")
            else:
                print('already exist')
    except:
        print("not found")


getPdf(url_path)
print("-----------------------")
freq_dist_word()
