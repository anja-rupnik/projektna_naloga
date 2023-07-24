import requests



def prenesi_stran(url, ime):
    odziv = requests.get(url)
    if odziv.status_code == 200:
        with open(ime, "w", encoding='utf-8') as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")