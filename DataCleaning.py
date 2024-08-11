#Importazioni Librerie
import pandas as pd
import numpy as np

#Importazione Dataset
file_path = r"Comune-di-Milano.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')

#Prime righe del dataset
print(df.head())

#Informazioni generali
print(df.info())

#Statistiche descrittive
print(df.describe())

#Totale della popolazione per ciascuna ipotesi
df['Tot Ipotesi alta'] = df.groupby(['Anno', 'Quartiere',])['Ipotesi alta'].transform('sum')
df['Tot Ipotesi media'] = df.groupby(['Anno', 'Quartiere'])['Ipotesi media'].transform('sum')
df['Tot Ipotesi bassa'] = df.groupby(['Anno', 'Quartiere'])['Ipotesi bassa'].transform('sum')

print(df)