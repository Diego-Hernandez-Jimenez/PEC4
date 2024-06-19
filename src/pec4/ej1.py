import pandas as pd

def read_csv(path_to_file: str) -> pd.DataFrame:
    """
    Lee un fichero csv como un dataframe y muestra por pantalla
    las cinco primeras filas de la base de datos así como su estructura.

    Parámetros:
        path_to_file: Ruta del fichero csv.

    Returns:
        pd.DataFrame: dataframe leído.
    """

    df = pd.read_csv(path_to_file)
    print('Estructura del conjunto de datos:')
    print(df.info(), '\n')
    print('Primeros 5 registros:')
    print(df.head())

    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset inicial, eliminando todas sus columnas excepto month, state, permit, handgun, long_gun.
    Además, muestra por pantalla el nombre de todas las columnas del dataframe.

    Parámetros:
        df: Datafame. Se asume que, como mínimo, contiene los campos month, state, permit, handgun, long_gun.

    Returns:
        pd.DataFrame: El dataframe editado.
    """

    clean_df = df[['month', 'state', 'permit', 'handgun', 'long_gun']]
    print('Columnas retenidas en el dataframe:')
    print(clean_df.columns)

    return clean_df


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cambia el nombre de la columna long_gun por longgun si existe en el dataframe.
    También se muestra por pantalla el nombre de todas las columnas del dataframe
    antes y después de ser editado.

    Parámetros:
        df: Datafame que, en principio, tiene la columna long_gun, aunque no necesariamente

    Returns:
        pd.DataFrame: El dataframe editado.
    """

    print('Columnas incluidas en el dataframe:')
    print(df.columns)
    if df.columns.isin(['long_gun']).any():
        renamed_df = df.rename(columns={'long_gun': 'longgun'})
        print('Columnas incluidas en el dataframe tras la edición:')
        print(renamed_df.columns)
        return renamed_df
    else:
        print('El dataframe no contiene la columna "long_gun", se devuelve sin modificaciones')
        return df