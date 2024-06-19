import pandas as pd

def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Divide la información que hay en la columna month creando dos nuevas columnas en el dataframe.
    Una de ellas llamada year y que contendrá el número del año y
    la otra columna llamada month y que será el número del mes. Ej: 2020-02 -> year = 2020,  month = 2.
    También se muestran las cinco primeras filas del dataframe resultante.

    Parámetros:
        df: Datafame que, en principio, tiene la columna month, aunque no necesariamente.
        El formato esperado del campo es una cadena con la estructura: 'yyyy-mm'

    Returns:
        pd.DataFrame: El dataframe editado.
    """

    df['year'] = df['month'].str.extract('(\d+)-0?\d')
    df['month'] = df['month'].str.extract('\d+-0?(\d)')
    print(df.head())

    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna month. También se muestran las cinco primeras filas
    del dataframe resultante.

    Parámetros:
        df: Datafame que, en principio, tiene la columna month, aunque no necesariamente.

    Returns:
        pd.DataFrame: El dataframe editado.
    """

    df = df.drop(columns='month')
    print('Columnas incluidas en el dataframe después de eliminar "month":')
    print(df.columns, '\n')
    print("Primeros 5 registros:")
    print(df.head())

    return df