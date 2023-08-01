# Analiza Tour de France 2023
V okviru projektne naloge za predmet Uvod v programiranje sem analizirala rezultate Tour de France 2023.

Podatke sem zajemala iz strani [Pro Cycling Stats](https://www.procyclingstats.com/race/tour-de-france/2023) in jih uredila z uporabo [zajem.py](zajem.py) ter shranila v .csv datoteke s pomočjo [v_tabelo.py](v_tabelo.py).

V mapi *spletme-strani* so shranjene spletne strani iz katerih so bili zajeti podatki, ločeni v dve podmapi glede na tip spletne strani. 

V mapi *csv_datoteke* so shranjene sledeče datoteke:
- 21 datotek *etapa(št).csv* za št med 0 in 20, ki vsebujejo id in čas posameznega kolesarja na določeni etapi
- *kolesarji.csv*, ki vsebuje za vsakega kolesarja id, ime in priimek, državo, tip kolesarja, ekipo, starost, težo, višino in točke v vsaki od kategorij (ODR, GC, TT, Sprint, Climber)
- *podatki_o_etapah.csv*, ki vsebuje za vsako etapo številko etape, povprečno hitrost zamgovalca, težavnost, točke terena in skupni vzpon