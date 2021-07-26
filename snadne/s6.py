from bs4 import BeautifulSoup
import requests

urls: list[str] = []

def requestURL(url: str):
	r = requests.get(f"http://i.protab.cz/static/ulohy/01f/{url}")
	formatted = BeautifulSoup(r.content, features="html.parser")
	returned = formatted.body.find_all("iframe")[1].get("src")
	print(returned)
	if returned in urls:
		print(f"was at {url} already")
		return
	urls.append(returned)
	requestURL(returned)

start = "tridgivgzbxgrzaglrcrcscyrorjjdvheucleyfxnpgidobfgdxphycqzsdruzlcstjovypkkm.html"
requestURL(start)

urls = [url.split(".html")[0] for url in urls]
print(urls)
big = "".join(urls)
print(big)