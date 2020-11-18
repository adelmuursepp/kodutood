import math
sisend = open('nurkesis.txt', 'rt')
valjund = open('nurkeval.txt', 'wt')
tipud = int(sisend.readline())
esimene_kujund = sisend.readline().split()
teine_kujund = sisend.readline().split()

# Teen nurkade x ja y koordinaatidest listi.
esimese_nurgad = []
teise_nurgad = []
for i in range(tipud):
    esimese_nurgad.append([int(esimene_kujund[2*i]), int(esimene_kujund[2*i+1])])
    teise_nurgad.append([int(teine_kujund[2*i]), int(teine_kujund[2*i+1])])


# Teen listid mõlema kujundi küljepikkustest
esimese_kuljed = []
teise_kuljed = []

for i in range(len(esimese_nurgad)):
    kaugus_ruudus = (esimese_nurgad[i-1][0] - esimese_nurgad[i][0])**2 + (esimese_nurgad[i-1][1] - esimese_nurgad[i][1])**2
    esimese_kuljed.append(math.sqrt(kaugus_ruudus))

for i in range(len(teise_nurgad)):
    kaugus_ruudus = (teise_nurgad[i-1][0] - teise_nurgad[i][0])**2 + (teise_nurgad[i-1][1] - teise_nurgad[i][1])**2
    teise_kuljed.append(math.sqrt(kaugus_ruudus))

# Leian võrdeteguri
umbermoot1 = sum(esimese_kuljed)
umbermoot2 = sum(teise_kuljed)
vordetegur = umbermoot1/umbermoot2

# Tuleb kontrollida, kas nad on uldse sarnased.

# Defineerin funktsiooni, mis aitab alustada eri alguspunktidest.
def shuffle_esimene_edasi(list):
    newlist = []
    viimane = list[-1]
    newlist.append(viimane)
    for i in range(len(list)-1):
        newlist.append(list[i])
    return newlist

esimene = esimese_kuljed
sarnased = 0
edasi = 0

# Vaatan läbi, kui mõlemate kujundite nurgad on kirja pandud sama pidi ringis liikudes
while sarnased == 0:
    koik_kuljed_vordeteguriga = 1

    for i in range(len(esimese_kuljed)):
        if (esimene[i]/teise_kuljed[i] - vordetegur) < 0.01:
            continue
        else:
            koik_kuljed_vordeteguriga = 0
            esimene = shuffle_esimene_edasi(esimene)
            edasi += 1
    if koik_kuljed_vordeteguriga == 1:
        sarnased = 1


# Vaatan läbi, kui mõlemate kujundite nurgad on kirja pandud eri pidi ringis liikudes
if esimene == 0:
    esimene = esimese_kuljed
    edasi = 0
while sarnased == 0:
    list_teistpidi = esimene[::-1]
    koik_kuljed_vordeteguriga = 1
    for i in range(len(esimese_kuljed)):
        if (list_teistpidi[i] / teise_kuljed[i] - vordetegur) < 0.01:
            continue
        else:
            koik_kuljed_vordeteguriga = 0
            esimene = shuffle_esimene_edasi(esimene)
            edasi += 1
    if koik_kuljed_vordeteguriga == 1:
        sarnased = 1

# Kirjutan väljundfaili vastuse
if sarnased == 0:
    valjund.write("-1\n")
else:
    valjund.write("{0}\n".format(vordetegur))
    valjund.write("{0}\n".format(edasi+1))
