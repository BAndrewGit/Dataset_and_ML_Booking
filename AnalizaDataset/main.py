import pandas as pd

# Încărcați datele
df = pd.read_csv('dataset_booking(Brasov).csv')

# Creați un dicționar pentru a stoca frecvențele
frecvente = {}

# Parcurgeți fiecare coloană de facilități
for col in df.columns:
    # Verificați dacă coloana este o facilitate
    if 'facilities' in col:
        # Adăugați fiecare facilitate la dicționar
        for val in df[col]:
            if val not in frecvente:
                frecvente[val] = 1
            else:
                frecvente[val] += 1

# Sortați facilitățile în funcție de frecvență
frecvente_sortate = sorted(frecvente.items(), key=lambda x: x[1], reverse=True)

# Afișați cele mai frecvente facilități
for facil, freq in frecvente_sortate:
    print(f'{facil}: {freq}')
