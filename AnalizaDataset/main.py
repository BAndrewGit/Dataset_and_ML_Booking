import pandas as pd


df = pd.read_csv('dataset_booking(Brasov).csv')


frecvente = {}


for col in df.columns:
    if 'facilities' in col:
        for val in df[col]:
            if val not in frecvente:
                frecvente[val] = 1
            else:
                frecvente[val] += 1

frecvente_sortate = sorted(frecvente.items(), key=lambda x: x[1], reverse=True)

for facil, freq in frecvente_sortate:
    print(f'{facil}: {freq}')
