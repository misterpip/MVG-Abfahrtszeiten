from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

def holeinfo(Abfahrstation):

    u = urllib.request.urlopen("http://www.mvg-live.de/ims/dfiStaticAuswahl.svc?haltestelle=" + Abfahrstation + "&ubahn=checked&tram=checked&bus=checked")
    data = u.read()

    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", { "class" : "departureTable" })

    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 2:
            Ustation = cells[0].find(text=True)
            Time = cells[1].find(text=True)
        
            print("Uhrzeit: ",Time)
            print("U-Bahnstation: ",Ustation)
            print("--------------------------------------\n")
        elif len(cells) == 3:
            Destination = cells[1].find(text=True)
            Destination.lstrip()
            Destination.replace('&nbsp;',"")
            Destination.replace('\n',"")
            print("Linie: ", cells[0].find(text=True))
            print("Ziel: ", Destination[6:])
            print("Abfahrt in: ", cells[2].find(text=True))
            print("\n-------------\n")

holeinfo("Scheidplatz")
