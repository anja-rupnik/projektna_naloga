import csv
import os

import zajem

ime = os.path.join("csv_datoteke", "kolesarji.csv")
with open(ime, "w", encoding='utf-8', newline='') as dat:
    writer = csv.DictWriter(dat, fieldnames=[
        "ime",
        "id", 
        "država",
        "tip",
        "ekipa",
        "starost",
        "teža",
        "višina",
        "ODR",
        "GC",
        "TT",
        "Sprint", 
        "Climber"
    ])
    writer.writeheader()
    for kolesar in zajem.kolesarji:
        writer.writerow(kolesar)

for e in range(zajem.st_strani):
    ime = os.path.join("csv_datoteke", f"etapa{e}.csv")
    with open(ime, "w", encoding='utf-8', newline='') as dat:
        writer = csv.DictWriter(dat, fieldnames=[
            "id", 
            f"čas{e+1}"
        ])
        writer.writeheader()
        for čas in zajem.čas_etape[e]:
            writer.writerow(čas)

ime = os.path.join("csv_datoteke", "podatki_o_etapah.csv")
with open(ime, "w", encoding='utf-8', newline='') as dat:
    writer = csv.DictWriter(dat, fieldnames=[
        "št",
        "avg speed",
        "dolžina",
        "strmost",
        "točke terena",
        "višinci", 
        "won how"
    ])
    writer.writeheader()
    for etapa in zajem.etape_det:
        writer.writerow(etapa)