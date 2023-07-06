import requests

st_strani = 17
na_stran = 100
for stran in range(st_strani):
    url = f"https://plus.cobiss.net/cobiss/si/sl/bib/search/advanced?ax&ti&kw&db=cobib&mat=allmaterials&tyf=1_knj_brailp&max={na_stran}&start={stran * na_stran}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        with open(f"stran-{stran}.html", "w", encoding='utf-8') as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")

