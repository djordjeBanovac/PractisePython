"""Use the BeautifulSoup and requests Python packages 
to print out a list of all the article titles on the New York Times homepage."""

import requests
from bs4 import BeautifulSoup


def decode_times() -> None:
    """function uses BeutifulSoup and requests to decode a web
    page www.nytimes and it lists the article titles only"""
    url = 'https://www.nytimes.com/'
    req = requests.get(url)
    req_html = req.content
    print(req_html)
    soup = BeautifulSoup(req_html,"html.parser")
    counter = 1
    for link in soup.find_all("h2",{"class":"story-heading"}):
            print(counter, link.text.strip())
            counter +=1

if __name__ == '__main__':
    decode_times()
