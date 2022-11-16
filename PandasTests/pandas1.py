"""
1) Calcular el promedio de altura y peso de todos los Pokemons en donde su categoría sea Flame, Worm y Turtle para luego imprimirlo por pantalla.
2) Calcular el IMC de cada pokemon y agregarlo como una columna al data frame cargado desde el archivo csv.
3) Cree una matriz usando numpy en donde se calcule el daño que realizará cada Pokémon al resto de los otros Pokemons.
4) Agregue una columna al data frame con el máximo daño que puede recibir cada Pokemon.
"""

import pandas as pd
df = pd.read_csv('pokemons.csv')


# filtro1 = df[(df['Category'] == 'Flame') | (df['Category'] == 'Worm') | (df['Category'] == 'Turtle')]
# altura = filtro1['Height'].mean()
# peso = filtro1['Weight'].mean()
# print(f'Altura promedio (Flame, Worm, Turtle): {altura}')
# print(f'Peso promedio (Flame, Worm, Turtle): {peso}')

imc = []
for i in range(df.shape[0]):
    a = df['Weight'][i]/df['Height'][i]**2
    a = a.round(1)
    imc.append(a)
df['IMC'] = imc
# print(df)

lista = []
for i in range(df.shape[0]):
    a = (df['Weight'][i]-df['Weight'].min())*0.7/(df['Weight'].max()-df['Weight'].min())
    lista.append(a)

for i in range(df.shape[0]):
    b = (df['IMC'][i]-df['IMC'].min())*0.3/(df['IMC'].max-df['IMC'].min())
    lista[i] += b
print(lista)