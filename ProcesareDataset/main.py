import pandas as pd


coloane_de_pastrat = [
    'name', 'address/country', 'address/full', 'address/postalCode', 'address/region', 'location/lat', 'location/lng',
    'checkIn', 'checkOut',  'breakfast',
    'price', 'currency', 'rating', 'reviews', 'rooms/0/available', 'stars',
    'type', 'rooms/0/persons', 'rooms/0/roomType'
]


df = pd.read_csv('RAW_dataset_booking(Brasov).csv')


df_nou = df[coloane_de_pastrat].copy()


df_nou.loc[:, 'Nota Personal'] = df['categoryReviews/0/score']
df_nou.loc[:, 'Nota Facilităţi'] = df['categoryReviews/1/score']
df_nou.loc[:, 'Nota Curăţenie'] = df['categoryReviews/2/score']
df_nou.loc[:, 'Nota Confort'] = df['categoryReviews/3/score']
df_nou.loc[:, 'Nota Raport calitate/preţ'] = df['categoryReviews/4/score']
df_nou.loc[:, 'Nota Locaţie'] = df['categoryReviews/5/score']
df_nou.loc[:, 'Nota WiFi gratuit'] = df['categoryReviews/6/score']


facilitati = ['Bucătărie', 'Parcare', 'Internet', 'Baie', 'Media/Tehnologie', 'TV cu ecran plat', 'Hârtie igienică',
              'Exterior', 'Prosoape', 'Dormitor', 'fumatul interzis în toate spaţiile publice şi private',
              'Lenjerie de pat', 'Toaletă', 'Baie privată', 'Zonă de living', 'Uscător de păr', 'Mâncăruri și băuturi',
              'încălzire', 'Duş', 'Garderobă sau dulap', 'terasă', 'Cadă sau duş', 'Suport de haine',
              'Articole de toaletă gratuite', 'camere de familie', 'Frigider', 'Priză lângă pat', 'Masă',
              'Servicii de recepție', 'Aparat pentru prepararea de ceai/cafea', 'Zonă de luat masa',  'Exterior/Vedere',
              'Pardoseală de lemn sau parchet', 'Canale prin cablu', 'Factură disponibilă la cerere',
              'Ustensile de bucătărie']


for facil in facilitati:
    df_nou[facil] = 0
    for col in df.columns:
        if 'facilities' in col and 'name' in col:
            df_nou[facil] = df_nou[facil] | df[col].apply(lambda x: 1 if x == facil else 0)


df_nou.to_csv('clean_dataset.csv', index=False)


df_nou.to_excel('clean_dataset.xlsx', index=False)
