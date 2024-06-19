import pandas as pd

def groupby_state(agg_df: pd.DataFrame) -> pd.DataFrame:
    """
    Muestra los valores totales de permit, hand_gun y long_gun
    agrupando los valores unicamente por estado y no por año.

    Parámetros:
        agg_df: Dataframe con, al menos, los campos state, permit, handgun y longgun resultado de
        aplicar groupby_state_and_year()

    Returns:
        pd.DataFrame: Dataframe con los valores agregados
    """
    agg_df_bystate = agg_df.groupby('state', as_index=False)[['permit', 'handgun', 'longgun']].sum()
    print('Primeros 5 registros de los datos agregados por estado:')
    print(agg_df_bystate.head())
    return agg_df_bystate


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Comprueba si existen los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands y,
    en el caso de que existan los elimina. También se muestra por pantalla el número de estados
    diferentes tras la alteración del dataframe

    Parámetros:
        agg_df: Dataframe con, al menos, el campo state.

    Returns:
        pd.DataFrame: Dataframe sin los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands
    """

    states_to_remove = df['state'].isin(['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands'])
    if states_to_remove.sum() >= 1:
        df = df[~states_to_remove]

    print(f"Nº de estados incluidos: {df['state'].nunique()}")
    
    return df


def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame='us-state-populations.csv') -> pd.DataFrame:
    """
    Fusiona los datos de los dos datasets recibidos como parámetros de entrada,
    incluyendo por cada estado toda la información procedente de las dos fuentes de datos.
    También se imprimen por pantalla las cinco primeras filas del dataset resultante.

    Parámetros:
        df1: Dataframe con, al menos, el campo state.
        df2: Dataframe con, al menos, el campo state.

    Returns:
        pd.DataFrame: Dataframe fusionado con todos los campos de df1 y df2
    """

    merged_df = df1.merge(df2, how='inner')
    print('Primeros 5 registros:')
    print(merged_df.head())

    return merged_df


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea 3 nuevas columnas llamadas permit_perc, longgun_perc y handgun_perc.
    Los valores relativos se calculann con la fórmula: 100 * target_col / pop_2014

    Parámetros:
        df: Dataframe con los campos permit, longgun, handgun y pop_2014

    Returns:
        pd.DataFrame: Dataframe editado
    """

    df['permit_perc'] =  100 * df['permit'] / df['pop_2014']
    df['longgun_perc'] = 100 * df['longgun'] / df['pop_2014']
    df['handgun_perc'] = 100 * df['handgun'] / df['pop_2014']

    return df


def ej_5_5(df: pd.DataFrame) -> pd.DataFrame:
    """
    1. Calcula la media de permisos permit_perc con dos decimales y muestra el resultado en pantalla.
    2. Después se muestra por pantalla toda la información relativa al estado de Kentucky.
    3. A continuación reemplaza el valor permit_perc de Kentucky con el valor de la media de esta columna.
    4. Se vuelve a calcular la media con dos decimales y ha mostrarse el resultado en pantalla. 
    5. Muestra unas conclusiones sobre el proceso realizado

    Parámetros:
        df: Dataframe con los campos permit_perc y state. La columna state debe
        contener datos de Kentucky.

    Returns:
        pd.DataFrame: dataframe editado
    """

    # 1.
    avg_permit_perc = df['permit_perc'].mean().round(2)
    print(f'Media de permisos: {avg_permit_perc}\n')

    # 2.
    ky_data = df.query("state == 'Kentucky'")
    print('Información relativa al estado de Kentucky:')
    print(ky_data,'\n')

    # 3.
    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = avg_permit_perc

    # 4.
    avg_permit_perc2 = df['permit_perc'].mean().round(2)
    print(f'Media de permisos (post-tratamiento Kentucky): {avg_permit_perc2}\n')
    
    comment = """
    Como se puede observar, el tratamiento del valor atípico altera enormemente la media de proporción de permisos,
    lo que puede llevar a conclusiones y decisiones muy diferentes. Cuando se calculan estadísticos de tendencia central,
    siempre es buena práctica acompañarlos de medidas de dispersión u algún otro análisis sobre la distribución de la
    variable en cuestión. Si se decide hacer un tratamiento de ellos, como sucede aquí, hay que tener cierto cuidado.
    La eliminación o sustitución de los valores atípicos encontrados puede ser razonable si los outliers representan una
    pequeña de la muestra y/o se deben a errores. Sin embargo, cuando los casos atípicos abundan y/o son casos con valores
    legítimos (aunque sean extremos), eliminarlos o reemplazarlos puede ser distorsionador.
    """
    print(comment)

    return df