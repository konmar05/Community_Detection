import requests
from bs4 import BeautifulSoup

def getData():

    db = open("database.txt", "a")

    links = set()
    result = requests.get("https://www.bundesliga.com/en/bundesliga/player")
    soup = BeautifulSoup(result.content, "html.parser")
    for a in soup.find_all('a', href=True):
       # print("Found the URL:", a['href'])
       if "player" in a['href']:
           links.add(a['href'])
    print(links)
    # db.write(str(links))

    for link in links:
        db.write("\n")
        print(link)
        db.write(link)
        result = requests.get("https://www.bundesliga.com" + link)
        soup = BeautifulSoup(result.content, "html.parser")
        for entry in soup.find_all("p", class_="vitaparagraph ng-star-inserted"):
            for part in entry.text.split("for "):
                # print(part)
                if "from" in part:
                    print(part.split(" from "))
                    db.write(str(part.split(" from ")))
            break
