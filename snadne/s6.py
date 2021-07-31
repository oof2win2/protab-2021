# Import all the packages!

from bs4 import BeautifulSoup;
import requests

baseURL = "http://i.protab.cz/zadani/S6/"

allURLs = []
hashes = []

def requestPage(url, i):
    i = i + 1

    # If we were here already, exit
    if url in allURLs:
        print("Was here at " + str(allURLs.index(url)))
        final = ""
        for hash in hashes:
            final += (chr(len(hash)))
        print(final)
        return

    # Add to all URLs
    allURLs.append(url)

    print(str(i) + ": " + str(url))

    # Auth
    auth = dict(sessionid="dkqr5andb7cklrizwl14e3wvxm9ff4bh")

    # Request the URL
    page = requests.get(url, cookies=auth)

    souped = BeautifulSoup(page.text, "html.parser")

    # Add the page hash to the array
    hashes.append(souped.select("iframe")[-1]["src"].split("/")[-1].replace(".html", ""))

    if i == 1:
        nextURL = "http://i.protab.cz"+souped.select("iframe")[-1]["src"]
    else:
        nextURL = "http://i.protab.cz/static/ulohy/01f/"+souped.select("iframe")[-1]["src"]
    requestPage(nextURL, i)

requestPage(baseURL, 0)