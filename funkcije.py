import requests
import csv


def prenesi_stran(url, ime):
    odziv = requests.get(url)
    if odziv.status_code == 200:
        with open(ime, "w", encoding='utf-8') as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")

def v_csv(ime, kategorije, slovar):
    with open(ime, "w", encoding='utf-8', newline='') as dat:
        writer = csv.DictWriter(dat, fieldnames=kategorije)
        writer.writeheader()
        for element in slovar:
            writer.writerow(element)
