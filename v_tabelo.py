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
