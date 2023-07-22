import requests
import os

st_strani = 21
for stran in range(st_strani):
    url = f"https://www.procyclingstats.com/race/tour-de-france/2022/stage-{stran+1}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        ime = os.path.join("spletne-strani", "stages", "stran-{}.html".format(stran))
        with open(ime, "w", encoding='utf-8') as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")

import re

kolesarji = []
čas_etape = []
for e in range(21):
    čas_etape.append([])
    ime = os.path.join("spletne-strani", "stages", "stran-{}.html".format(e))
    with open(ime, encoding='utf-8') as dat:
        besedilo = dat.read()
        i = 0
        for najdba in re.finditer(r'data-nation="(?P<država>.*?)">.*?"gc hide".*?"bibs hide" >(?P<id>\d+?)</td>.*?"fs10 clr999">(?P<tip>.*?)</span>.*?<a href="rider/(?P<ime>.*?)">.*?"showIfMobile riderteam">(?P<ekipa>.*?)</span>.*?"age hide" >(?P<starost>\d+?)</td>.*?<td class="time ar" >(?P<h>\d*?):(?P<min>\d*?):(?P<s>\d*?)<', besedilo):
            topčas = najdba["h"], najdba["min"], najdba["s"]
            if e == 0:
                kolesarji.append({"ime": najdba["ime"], "id": najdba["id"], "država": najdba["država"], "tip": najdba["tip"], "ekipa": najdba["ekipa"], "starost": najdba["starost"]})
            čas_etape[e].append({"id": najdba["id"], "h": najdba["h"], "min": najdba["min"], "s": najdba["s"]})
        
        for najdba in re.finditer(
            r'data-nation="(?P<država>.*?)">.*?"gc hide".*?"bibs hide" >(?P<id>\d+?)</td>.*?"fs10 clr999">(?P<tip>.*?)</span>.*?<a href="rider/(?P<ime>.*?)">.*?"showIfMobile riderteam">(?P<ekipa>.*?)</span>.*?"age hide" >(?P<starost>\d+?)</td>.*?"hide">(?P<min>\d*?):(?P<s>\d+?)</div>',
            besedilo
        ):
            i += 1
            if e == 0:
                kolesarji.append({"ime": najdba["ime"], "id": najdba["id"], "država": najdba["država"], "tip": najdba["tip"], "ekipa": najdba["ekipa"], "starost": najdba["starost"]})
            if int(najdba["s"]) + int(topčas[2]) > 59:
                min = 1
                sekunde = int(najdba["s"]) + int(topčas[2]) - 60
            else:
                min = 0
                sekunde = int(najdba["s"]) + int(topčas[2])
            if int(najdba["min"]) + int(topčas[1]) + min > 59:
                ure = 1 + int(topčas[0])
                min = int(najdba["min"]) + int(topčas[1]) + min - 60
            else:
                ure = int(topčas[0])
                min = int(najdba["min"]) + int(topčas[1]) + min
                
            čas_etape[e].append({"id": najdba["id"], "h": ure, "min": min, "s": sekunde})



for kolesar in kolesarji:
    url = f"https://www.procyclingstats.com/rider/{kolesar['ime']}/2022"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        ime = os.path.join("spletne-strani", "kolesarji", "stran-{}.html".format(kolesar['ime']))
        with open(ime, "w", encoding='utf-8') as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")