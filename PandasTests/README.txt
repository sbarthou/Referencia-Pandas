dataframe (df) : Tabla de datos.
series : Lista estilo numpy array.
df = pd.read_csv("file.csv") : Carga y lee el archivo .csv en la variable df.
df = pd.read_excel("file.xlsx") : Carga y lee el archivo .xlsx en la variable df.
df.head(n) : Retorna los n primeros datos del dataframe.
df.tail(n) : Retorna los n ultimos datos del dataframe.
df.index : Retorna el indice de los datos del dataframe. (el número de fila)
df.columns : Retorna las columnas del dataframe.
df.shape : Retorna el número de filas(i) y el número de columnas(j) de forma (i,j). (igual que la función shape de numpy)
df.iloc[i] : Retorna los datos de la fila i.
df.iloc[i,j] : Retorna el dato en la posición j de la fila i.
df["columna"] : Retorna los datos de la columna llamada columna.
df["columna"][i] : Retorna el dato en la posición i (fila n°i) de la columna llamada columna.
data = df[["columnaA", "columnaB"]] : Crea una variable llamada data que contiene solo los datos de las columnas columnaA y columnaB.
df["columna"].unique() : Retorna los datos de la columna llamada columna pero sin repetirlos.
len(df["columna"].unique()) : Retorna la cantidad de datos de la columna llamada columna pero sin repetir ninguno.
df[df["columna"] == "valor"] : Retorna un dataframe "filtrado" con los datos que en la columna llamada columna tengan valor valor.
df[(df["columnaA"] == "valorA") | (df["columnaB"] == "valorB")] : Se pueden ocupar multiples condiciones poniendoles () y separandolas con | (or) o & (and).
df[df["columna"].fillna("None")] : La función .fillna permite asignar un valor (None) en una columna (columna) que no tenga un dato alguna fila.
df[df["columna"].fillna("None") != "None"] : Retorna un dataframe sin aquellas filas que no tengan un valor en la columna llamada columna.
df.to_numpy() : Convierte un dataframe a un array de numpy.
df.values : Convierte un dataframe a un array de numpy.
df.size : Retorna el número de elementos.
df.add() : Add DataFrames.
df.sub() : Subtract DataFrames.
df.mul() : Multiply DataFrames.
df.div() : Divide DataFrames (float division).
df.floordiv() : Divide DataFrames (integer division).
df.mod() : Calculate modulo (remainder after division). (resto de la division)
df.pow() : Calculate exponential power.
df.sum() : Return the sum over the requested axis.
df.min() : Return the minimum over the requested axis.
df.max() : Return the maximum over the requested axis.
df.idxmin() : Return the index of the minimum over the requested axis.
df.idxmax() : Return the index of the maximum over the requested axis.
df.mean() : Return the mean of the values over the requested axis.
df.std() : Return the standard deviation over requested axis.