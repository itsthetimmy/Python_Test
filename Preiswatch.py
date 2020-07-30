import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.de/Apple-iPhone-11-64-GB-Schwarz/dp/B07XRR7N5V/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=apple+iphone&qid=1595843393&sr=8-4"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")
preis = soup.find(id="priceblock_ourprice").get_text()

preis=preis.replace("€" , "")
preis=preis.replace("," , ".")

print(preis)