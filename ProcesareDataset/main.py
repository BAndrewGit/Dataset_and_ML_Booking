import pandas as pd

# Numele coloanelor pe care doriți să le păstrați
coloane_de_pastrat = [
    'name', 'address/full', 'address/postalCode', 'address/country', 'address/region', 'location/lat', 'location/lng',
    'checkIn', 'checkOut', 'breakfast',
    'price', 'currency', 'rating', 'reviews', 'rooms/0/available', 'stars',
    'type', 'rooms/0/persons', 'rooms/0/roomType'
]

df = pd.read_csv('dataset_Romania.csv', low_memory=False)

# Selectați doar coloanele pe care doriți să le păstrați
df_nou = df[coloane_de_pastrat].copy()


def replace_nan_with_zero(df_copy, columns):
    for column in columns:
        df_copy.loc[:, column] = df_copy[column].fillna(0)
    return df_copy


# Adăugați noile coloane
df_nou.loc[:, 'Nota Personal'] = df['categoryReviews/0/score']
df_nou.loc[:, 'Nota Facilităţi'] = df['categoryReviews/1/score']
df_nou.loc[:, 'Nota Curăţenie'] = df['categoryReviews/2/score']
df_nou.loc[:, 'Nota Confort'] = df['categoryReviews/3/score']
df_nou.loc[:, 'Nota Raport calitate/preţ'] = df['categoryReviews/4/score']
df_nou.loc[:, 'Nota Locaţie'] = df['categoryReviews/5/score']
df_nou.loc[:, 'Nota WiFi gratuit'] = df['categoryReviews/6/score']

columns_to_replace = ['Nota Personal', 'Nota Facilităţi', 'Nota Curăţenie', 'Nota Confort',
                      'Nota Raport calitate/preţ', 'Nota Locaţie', 'Nota WiFi gratuit']
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

# Adăugați fiecare facilitate ca o nouă coloană
for facil in facilitati:
    # Creați o nouă coloană pentru fiecare facilitate
    df_nou[facil] = 0
    # Parcurgeți toate coloanele care conțin numele facilităților
    for col in df.columns:
        if 'facilities' in col and 'name' in col:
            # Actualizați coloana facilitate dacă facilitatea există
            df_nou[facil] = df_nou[facil] | df[col].apply(lambda x: 1 if str(x).strip() == facil else 0)


# Eliminați spațiile de la început și de la sfârșitul denumirilor coloanelor
df_nou.columns = df_nou.columns.str.strip()

# Înlocuiți valorile NaN cu 0
df_nou = replace_nan_with_zero(df_nou, ['Nota Personal', 'Nota Facilităţi', 'Nota Curăţenie', 'Nota Confort',
                                        'Nota Raport calitate/preţ', 'Nota Locaţie', 'Nota WiFi gratuit'])

df_nou = df_nou[df_nou['price'] > 40]
df_nou = df_nou.drop_duplicates()
df['address/postalCode'] = pd.to_numeric(df['address/postalCode'], errors='coerce')

# Selectați rândurile în care 'address/country' nu este 'România' sau 'address/region' este null
index_names = df_nou[(df_nou['address/country'] != 'România') | (df_nou['address/region'].isnull())].index

# Eliminați aceste rânduri din DataFrame
df_nou.drop(index_names, inplace=True)

# Scrieți datele într-un fișier CSV nou
df_nou.to_csv('clean_dataset_Romania.csv', index=False)

# Scrieți datele într-un fișier Excel nou
df_nou.to_excel('clean_dataset_Romania.xlsx', index=False)
