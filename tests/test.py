import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re


def findmusic(txt):
    r = search(txt,num=5,stop=5,pause=2)
    urls = []
    for url in r:
        if len(urls)>0:
            break
        else:
            print(url)
            r = requests.get(url).text
            bs = BeautifulSoup(r,'html.parser')
            bs = bs.find_all('a')
            for i in bs:
                try:
                    urls.append((re.search(r'^(https?|ftp|file):\/\/(www.)?(.*?)\.(mp3)$',string=str(i['href'])).group(0),i['title']))
                except KeyError:
                    urls.append((re.search(r'^(https?|ftp|file):\/\/(www.)?(.*?)\.(mp3)$',string=str(i['href'])).group(0),'دانلود'))
                except:
                    pass
                finally:
                    continue
    return urls                
            
    
