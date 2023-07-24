import os
import re

import funkcije

st_strani = 21
for stran in range(st_strani):
    url = f"https://www.procyclingstats.com/race/tour-de-france/2022/stage-{stran+1}"
    ime = os.path.join("spletne-strani", "stages_time", "stran-{}.html".format(stran))
    funkcije.prenesi_stran(url, ime)


kolesarji = []
čas_etape = []
for e in range(st_strani):
    čas_etape.append([])
    ime = os.path.join("spletne-strani", "stages_time", "stran-{}.html".format(e))
    with open(ime, encoding='utf-8') as dat:
        besedilo = dat.read()
        
        for najdba in re.finditer(r'data-nation="(?P<država>.*?)">.*?"gc hide".*?"bibs hide" >(?P<id>\d+?)</td>.*?"fs10 clr999">(?P<tip>.*?)</span>.*?<a href="rider/(?P<ime>.*?)">.*?"showIfMobile riderteam">(?P<ekipa>.*?)</span>.*?"age hide" >(?P<starost>\d+?)</td>.*?<td class="time ar" >(?P<h>\d*?):(?P<min>\d*?):(?P<s>\d*?)<', besedilo):
            topčas = najdba["h"], najdba["min"], najdba["s"]
            if e == 0:
                kolesarji.append({"ime": najdba["ime"], "id": najdba["id"], "država": najdba["država"], "tip": najdba["tip"], "ekipa": najdba["ekipa"], "starost": najdba["starost"]})
            čas = int(najdba["h"]) + int(najdba["min"])/60 + int(najdba["s"])/3600
            čas_etape[e].append({"id": najdba["id"], "čas": čas})
        
        for najdba in re.finditer(
            r'data-nation="(?P<država>.*?)">.*?"gc hide".*?"bibs hide" >(?P<id>\d+?)</td>.*?"fs10 clr999">(?P<tip>.*?)</span>.*?<a href="rider/(?P<ime>.*?)">.*?"showIfMobile riderteam">(?P<ekipa>.*?)</span>.*?"age hide" >(?P<starost>\d+?)</td>.*?"hide">(?P<min>\d*?):(?P<s>\d+?)</div>',
            besedilo
        ):
            
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
            čas = ure + min/60 + sekunde/3600    
            čas_etape[e].append({"id": najdba["id"], "čas": čas})



for kolesar in kolesarji:
    url = f"https://www.procyclingstats.com/rider/{kolesar['ime']}/2022"
    ime = os.path.join("spletne-strani", "kolesarji", "stran-{}.html".format(kolesar['ime']))
    funkcije.prenesi_stran(url, ime)


for kolesar in kolesarji:
    ime = os.path.join("spletne-strani", "kolesarji", "stran-{}.html".format(kolesar['ime']))
    with open(ime, encoding='utf-8') as dat:
        besedilo = dat.read()
        
        for najdba in re.finditer(
            r'<b>Weight:</b> (?P<teža>.*?) kg .*?<b>Height:</b> (?P<višina>.*?) m<br />.*?<div class="pnt">(?P<ODR>\d*?)</div>.*?<div class="pnt">(?P<GC>\d*?)</div>.*?<div class="pnt">(?P<TT>\d*?)</div>.*?<div class="pnt">(?P<Spr>\d*?)</div>.*?<div class="pnt">(?P<Clm>\d*?)</div>',
            besedilo
        ):
            kolesar.update({"teža": najdba["teža"], "višina": najdba["višina"], "ODR": najdba["ODR"], "GC": najdba["GC"], "TT": najdba["TT"], "Sprint": najdba["Spr"], "Climber": najdba["Clm"]})
                     