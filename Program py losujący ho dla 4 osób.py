import random

# Lista uczestników
uczestnicy = ['Emil', 'Fryderyk', 'Maciej', 'Sławek']

# Dni tygodnia, w których odbywa się Home Office
dni_ho = ['Wtorek', 'Środa', 'Czwartek']

# Harmonogram Home Office
harmonogram_ho = {}

# Wykluczanie uczestników, którzy mają pracę stacjonarną o 6:00
for uczestnik in uczestnicy:
    if uczestnik == 'Fryderyk':
        harmonogram_ho['Wtorek'] = [uczestnik]
        harmonogram_ho['Środa'] = [uczestnik]
    elif uczestnik == 'Maciej':
        harmonogram_ho['Czwartek'] = [uczestnik]
    else:
        for dzien in dni_ho:
            harmonogram_ho[dzien] = []
            
# Losowanie harmonogramu
for dzien in dni_ho:
    if dzien == 'Wtorek' or dzien == 'Środa' or dzien == 'Czwartek':
        dostepni = [uczestnik for uczestnik in uczestnicy if uczestnik not in harmonogram_ho.get(dni_ho[dni_ho.index(dzien)-1],[])]
        if len(dostepni) == 0:
            dostepni = uczestnicy.copy()
            dostepni.remove(harmonogram_ho.get(dni_ho[dni_ho.index(dzien)-1])[0])
        wybrany = random.choice(dostepni)
        harmonogram_ho[dzien].append(wybrany)
    else:
        for uczestnik in uczestnicy:
            harmonogram_ho[dzien].append(uczestnik)

# Wyświetlanie harmonogramu
print('Harmonogram Home Office:')
for dzien in harmonogram_ho:
    print(dzien + ': ' + ', '.join(harmonogram_ho[dzien]))