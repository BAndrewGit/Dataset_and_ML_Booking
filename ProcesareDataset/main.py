import pandas as pd

# Numele coloanelor pe care doriți să le păstrați
coloane_de_pastrat = [
    'name', 'address/full', 'address/postalCode', 'address/country', 'address/region', 'location/lat', 'location/lng',
    'checkIn', 'checkOut', 'breakfast', 'price', 'currency', 'rating', 'reviews', 'rooms/0/available', 'stars',
    'type', 'rooms/0/persons', 'rooms/0/roomType'
]

df = pd.read_csv('dataset_Romania.csv', low_memory=False)

# Selectați doar coloanele pe care doriți să le păstrați
df_nou = df[coloane_de_pastrat].copy()

# Înlocuiți valorile din coloana 'breakfast' cu 1 dacă micul dejun este inclus și 0 în caz contrar
df_nou['breakfast'] = df_nou['breakfast'].notna().astype(int)


# Definirea funcției pentru înlocuirea valorilor NaN cu 0
def replace_nan_with_zero(df_copy, columns):
    for column in columns:
        df_copy[column] = df_copy[column].fillna(0)
    return df_copy


# Adăugați noile coloane pentru notele de recenzie
df_nou['nota_personal'] = df['categoryReviews/0/score']
df_nou['nota_facilităţi'] = df['categoryReviews/1/score']
df_nou['nota_curăţenie'] = df['categoryReviews/2/score']
df_nou['nota_confort'] = df['categoryReviews/3/score']
df_nou['nota_raport_calitate/preţ'] = df['categoryReviews/4/score']
df_nou['nota_locaţie'] = df['categoryReviews/5/score']
df_nou['nota_wifi_gratuit'] = df['categoryReviews/6/score']

# Înlocuire NaN cu 0 pentru notele de recenzie
columns_to_replace = ['nota_personal', 'nota_facilităţi', 'nota_curăţenie', 'nota_confort',
                      'nota_raport_calitate/preţ', 'nota_locaţie', 'nota_wifi_gratuit']
df_nou = replace_nan_with_zero(df_nou, columns_to_replace)

# Facilitățile pe care doriți să le adăugați
facilitati = ['Vedere la oraș', 'Menaj zilnic', 'Canale prin satelit', 'Zonă de luat masa în aer liber', 'Cadă',
              'Facilităţi de călcat', 'Izolare fonică', 'terasă la soare', 'Pardoseală de gresie/marmură',
              'Papuci de casă', 'uscător de rufe', 'Animale de companie', 'Încălzire', 'Birou', 'mobilier exterior',
              'Alarmă de fum', 'Vedere la grădină', 'Cuptor', 'Cuptor cu microunde', 'Zonă de relaxare', 'Canapea',
              'Intrare privată', 'Fier de călcat', 'Mașină de cafea', 'Plită de gătit', 'Extinctoare', 'Cană fierbător',
              'grădină', 'Ustensile de bucătărie', 'Maşină de spălat', 'Balcon', 'Pardoseală de lemn sau parchet',
              'Aparat pentru prepararea de ceai/cafea', 'Zonă de luat masa', 'Canale prin cablu', 'aer condiţionat',
              'Masă', 'Suport de haine', 'Cadă sau duş', 'Frigider']

# Normalizare facilități (denumiri mici)
facilitati_normalizate = {facil: facil.lower().replace(' ', '_') for facil in facilitati}

# Adăugați fiecare facilitate ca o nouă coloană
for facil in facilitati_normalizate.values():
    df_nou[facil] = 0

# Actualizați coloanele de facilități
for col in df.columns:
    if 'facilities' in col and 'name' in col:
        for facil, facil_normalizat in facilitati_normalizate.items():
            df_nou[facil_normalizat] = df_nou[facil_normalizat] | df[col].apply(lambda x: True if str(x).strip() == facil else False)

# Eliminați spațiile de la început și de la sfârșitul denumirilor coloanelor
df_nou.columns = df_nou.columns.str.strip()

# Înlocuiți valorile NaN cu 0
df_nou = replace_nan_with_zero(df_nou, ['nota_personal', 'nota_facilităţi', 'nota_curăţenie', 'nota_confort',
                                        'nota_raport_calitate/preţ', 'nota_locaţie', 'nota_wifi_gratuit'])

# Înlocuirea valorilor lipsă cu mediana
df_nou['rooms/0/persons'] = df_nou['rooms/0/persons'].fillna(df_nou['rooms/0/persons'].median())
df_nou['stars'] = df_nou['stars'].fillna(df_nou['stars'].median())

# Mutați coloana 'breakfast' la sfârșitul DataFrame-ului
breakfast = df_nou.pop('breakfast')
df_nou['mic_dejun'] = breakfast

# Filtrați datele
df_nou = df_nou[df_nou['price'] > 40]
df_nou = df_nou.drop_duplicates()
df_nou['address/postalCode'] = pd.to_numeric(df_nou['address/postalCode'], errors='coerce')

# Selectați rândurile în care 'address/country' nu este 'România' sau 'address/region' este null
index_names = df_nou[(df_nou['address/country'] != 'România') | (df_nou['address/region'].isnull())].index

# Eliminați aceste rânduri din DataFrame
df_nou.drop(index_names, inplace=True)

# Renumirea coloanelor pentru a corespunde cu baza de date
df_nou.rename(columns={
    'name': 'name',
    'address/full': 'address',
    'address/postalCode': 'postal_code',
    'address/country': 'country',
    'address/region': 'region',
    'location/lat': 'latitude',
    'location/lng': 'longitude',
    'checkIn': 'check_in',
    'checkOut': 'check_out',
    'price': 'price',
    'currency': 'currency',
    'rating': 'rating',
    'reviews': 'num_reviews',
    'rooms/0/available': 'availability',
    'rooms/0/persons': 'persons',
    'rooms/0/roomType': 'room_type'
}, inplace=True)

# Scrieți datele într-un fișier CSV nou
df_nou.to_csv('clean_dataset_Romania.csv', index=False)

# Scrieți datele într-un fișier Excel nou
df_nou.to_excel('clean_dataset_Romania.xlsx', index=False)
