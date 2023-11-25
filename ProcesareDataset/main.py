import pandas as pd

# Numele coloanelor pe care doriți să le păstrați
coloane_de_pastrat = [
    'name', 'address/country', 'address/full', 'address/postalCode', 'address/region', 'location/lat', 'location/lng',
    'checkIn', 'checkOut',  'breakfast',
    'price', 'currency', 'rating', 'reviews', 'rooms/0/available', 'stars',
    'type', 'rooms/0/persons', 'rooms/0/roomType'
]

# Încărcați datele din fișierul CSV original
df = pd.read_csv('dataset_booking(Brasov).csv')

# Selectați doar coloanele pe care doriți să le păstrați
df_nou = df[coloane_de_pastrat].copy()

# Adăugați noile coloane
df_nou.loc[:, 'Nota Personal'] = df['categoryReviews/0/score']
df_nou.loc[:, 'Nota Facilităţi'] = df['categoryReviews/1/score']
df_nou.loc[:, 'Nota Curăţenie'] = df['categoryReviews/2/score']
df_nou.loc[:, 'Nota Confort'] = df['categoryReviews/3/score']
df_nou.loc[:, 'Nota Raport calitate/preţ'] = df['categoryReviews/4/score']
df_nou.loc[:, 'Nota Locaţie'] = df['categoryReviews/5/score']
df_nou.loc[:, 'Nota WiFi gratuit'] = df['categoryReviews/6/score']

# Facilitățile pe care doriți să le adăugați
facilitati = ['Bucătărie', 'Parcare', 'Internet', 'Baie', 'Media/Tehnologie', 'TV cu ecran plat', 'Hârtie igienică',
              'Exterior', 'Prosoape', 'Dormitor', 'fumatul interzis în toate spaţiile publice şi private',
              'Lenjerie de pat', 'Toaletă', 'Baie privată', 'Zonă de living', 'Uscător de păr', 'Mâncăruri și băuturi',
              'încălzire', 'Duş', 'Garderobă sau dulap', 'terasă', 'Cadă sau duş', 'Suport de haine',
              'Articole de toaletă gratuite', 'camere de familie', 'Frigider', 'Priză lângă pat', 'Masă',
              'Servicii de recepție', 'Aparat pentru prepararea de ceai/cafea', 'Zonă de luat masa',  'Exterior/Vedere',
              'Pardoseală de lemn sau parchet', 'Canale prin cablu', 'Factură disponibilă la cerere',
              'Ustensile de bucătărie']

# Adăugați fiecare facilitate ca o nouă coloană
for facil in facilitati:
    # Creați o nouă coloană pentru fiecare facilitate
    df_nou[facil] = 0
    # Parcurgeți toate coloanele care conțin numele facilităților
    for col in df.columns:
        if 'facilities' in col and 'name' in col:
            # Actualizați coloana facilitate dacă facilitatea există
            df_nou[facil] = df_nou[facil] | df[col].apply(lambda x: 1 if x == facil else 0)

# Scrieți datele într-un fișier CSV nou
df_nou.to_csv('clean_dataset.csv', index=False)

# Scrieți datele într-un fișier Excel nou
df_nou.to_excel('clean_dataset.xlsx', index=False)
