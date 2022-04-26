# Header contains information sent by client to server in order to facilitate communication between them
# and also the server response.
# This part of the code enables automatic collection of information on catalog numbers and prices on the site https://www.noxsensorshop.com/nox-sensor/
# instead of doing it manually by copy and paste method on all pages.

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.noxsensorshop.com/nox-sensor/", headers=headers)
c = r.content

soup=BeautifulSoup(c, "html.parser")

all=soup.find_all("div",{"class":"product-content"})

all[0].find("h3").text

page_nr=soup.find_all("a",{"class":"page-numbers"})[-2].text
print(page_nr,"number of pages found")

l=[]
base_url="https://www.noxsensorshop.com/nox-sensor/page/"
for page in range(1,13):
    #print(page)
    r=requests.get(base_url+str(page)+"/", headers=headers)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"product-content"})
    for item in all:
        d={}
        d["OEN"]=item.find("div",{"class","product-title-wrap"}).find("a").text
        try:
            d["ArticleNumber"]=item.find("div",{"class","product-serial"}).find("span").text
        except AttributeError:
            pass
        d["Price"]=item.find("div",{"class","product-price-wrap"}).find("span").text

        l.append(d)
# for element in l:
#     print(element)

import pandas
df = pandas.DataFrame(l)
df.to_csv("NOx.csv")
