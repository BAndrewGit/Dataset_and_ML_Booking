import pandas as pd

# Lista cu numele fișierelor CSV
fisiere = ['dataset_Jud_Alba.csv', 'dataset_Jud_Arad.csv', 'dataset_Jud_Arges.csv',
           'dataset_Jud_Bacau.csv', 'dataset_Jud_Bihor.csv', 'dataset_Jud_BistritaNasaud.csv',
           'dataset_Jud_Botosani.csv', 'dataset_Jud_Braila.csv', 'dataset_Jud_Brasov.csv',
           'dataset_Jud_Bucuresti.csv', 'dataset_Jud_Buzau.csv', 'dataset_Jud_Calarasi.csv',
           'dataset_Jud_Caras-Severin.csv', 'dataset_Jud_Cluj.csv', 'dataset_Jud_Constanta.csv',
           'dataset_Jud_Covasna.csv', 'dataset_Jud_Dambovita.csv', 'dataset_Jud_Dolj.csv',
           'dataset_Jud_Galati.csv', 'dataset_Jud_Giurgiu.csv', 'dataset_Jud_Gorj.csv',
           'dataset_Jud_Harghita.csv', 'dataset_Jud_Hunedoara.csv', 'dataset_Jud_Ialomita.csv',
           'dataset_Jud_Iasi.csv', 'dataset_Jud_Ilfov.csv', 'dataset_Jud_Maramures.csv',
           'dataset_Jud_Mehedinti.csv', 'dataset_Jud_Mures.csv', 'dataset_Jud_Neamt.csv',
           'dataset_Jud_Olt.csv', 'dataset_Jud_Prahova.csv', 'dataset_Jud_Salaj.csv',
           'dataset_Jud_SatuMare.csv', 'dataset_Jud_Sibiu.csv', 'dataset_Jud_Suceava.csv',
           'dataset_Jud_Teleorman.csv', 'dataset_Jud_Timis.csv', 'dataset_Jud_Tulcea.csv',
           'dataset_Jud_Valcea.csv', 'dataset_Jud_Vaslui.csv', 'dataset_Jud_Vrancea.csv']


# Inițializăm un DataFrame gol
df_total = pd.DataFrame()

# Parcurgem lista de fișiere și le adăugăm în DataFrame
for fisier in fisiere:
    df = pd.read_csv(fisier, low_memory=False)
    df_total = pd.concat([df_total, df])

# Eliminăm duplicatele
df_total = df_total.drop_duplicates()
print(df_total.duplicated().sum())

# Salvăm DataFrame-ul final într-un nou fișier CSV
df_total.to_csv('dataset_Romania.csv', index=False)
