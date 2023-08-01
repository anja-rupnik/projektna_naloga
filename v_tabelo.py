import os

import zajem
import funkcije

ime = os.path.join("csv_datoteke", "kolesarji.csv")
kategorije = ["ime", "id", "država", "tip", "ekipa", "starost", "teža", "višina", "ODR", "GC", "TT", "Sprint", "Climber"]
funkcije.v_csv(ime, kategorije, zajem.kolesarji)

for e in range(zajem.st_strani):
    ime = os.path.join("csv_datoteke", f"etapa{e}.csv")
    kategorije = ["id", f"čas{e+1}"]
    funkcije.v_csv(ime, kategorije, zajem.čas_etape[e])

ime = os.path.join("csv_datoteke", "podatki_o_etapah.csv")
kategorije = ["št", "avg speed", "dolžina", "strmost", "točke terena", "skupni vzpon", "won how"]
funkcije.v_csv(ime, kategorije, zajem.etape_det)