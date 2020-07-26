import requests
import re
from bs4 import BeautifulSoup

#Nur für ARD Börsenseite!
#url = "https://kurse.boerse.ard.de/ard/kurse_einzelkurs_uebersicht.htn?i=9408435" # Tesla


def getpreis(url):
    page=requests.get(url)

    soup= BeautifulSoup(page.text, 'html.parser')
    preis=str(soup.find(class_='leftfloat big'))

    preis=preis.replace("<span class=\"leftfloat big\" title=\"aktueller Wert\">" , "")

    #Währung herausfinden (geht nur Dollar und Euro)
    if (preis.find('€') != -1):
        waehrung = "€"
        preis=preis.replace("€</span>" , "")#Euro etc entfernen
    elif (preis.find('$') != -1):
        waehrung = "$"
        preis=preis.replace(".","") #Beim Dollar den Tausender-Punkt entfernen
        preis=preis.replace("$</span>" , "")#Dollar etc entfernen

    preis=preis.replace("\xa0" , "")
    preis=preis.replace("," , ".")

    print(preis+waehrung)

getpreis("https://kurse.boerse.ard.de/ard/kurse_einzelkurs_uebersicht.htn?i=107741")