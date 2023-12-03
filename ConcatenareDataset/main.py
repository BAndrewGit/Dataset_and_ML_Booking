import pandas as pd

# Lista cu numele fișierelor CSV
fisiere = ['dataset_Constanta.csv', 'dataset_Costinesti.csv', 'dataset_EforieNord.csv', 'dataset_Mamaia.csv',
           'dataset_Mangalia.csv', 'dataset_VamaVeche.csv']

# Inițializăm un DataFrame gol
df_total = pd.DataFrame()

# Parcurgem lista de fișiere și le adăugăm în DataFrame
for fisier in fisiere:
    df = pd.read_csv(fisier)
    df_total = pd.concat([df_total, df])

# Eliminăm duplicatele
df_total = df_total.drop_duplicates()

# Salvăm DataFrame-ul final într-un nou fișier CSV
df_total.to_csv('dataset_Jud_Constanta.csv', index=False)
