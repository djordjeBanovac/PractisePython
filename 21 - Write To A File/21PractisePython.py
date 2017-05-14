"""Take the code from the How To Decode A 
Website exercise (if you didn’t do it or just 
want to play with some different code, use the 
code from the solution), and instead of printing 
the results to a screen, write the results to 
a txt file. In your code, just make up a name 
for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved."""


from bs4 import BeautifulSoup
import requests


def write_file(alist:list, file_name:str)->None:
    """function writes to a file item from the list. 
    It appends a new line after each item in list"""
    with open(file_name,"w") as fis:
        for item in alist:
            fis.write(item)
            fis.write('\n')


def decode_web_page() ->list:
    """function finds articles on new york times homepage
    and appends them in the list"""
    req = requests.get("https://www.nytimes.com/")
    soup = BeautifulSoup(req.text,"html.parser")
    alist = []
    for item in soup.find_all("h2",{"class":"story-heading"}):
        alist.append(item.text.strip())
    return alist

if __name__ =="__main__":
    file_name = input("Enter file name:")
    nytimes_articles = decode_web_page()
    write_file(nytimes_articles,file_name)