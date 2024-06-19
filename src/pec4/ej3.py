import pandas as pd

def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores acumulados totales agrupando los datos por año (year) y por estado (state)

    Parámetros:
        df: Datafame que, en principio, tiene las columnas year, state
        y al menos otra de tipo numérico.

    Returns:
        pd.DataFrame: El dataframe editado.
    """

    agg_df = df.groupby(['year', 'state'], as_index=False).sum()

    return agg_df


def print_biggest_handguns(agg_df: pd.DataFrame) -> None:
    """
    Imprime por pantalla un mensaje informativo indicando el nombre del estado
    y el año en donde se ha registrado un mayor numero de hand_guns.

    Parámetros:
        agg_df: Dataframe resultado de haber aplicado previamente groupby_state_and_year()

    Returns:
        None
    """
    top_handguns = agg_df \
    .sort_values('handgun', ascending=False) \
    .iloc[0]
    print(
        f'El mayor número de peticiones de armas de fuego cortas se ha registrado en {top_handguns.state} en el año {top_handguns.year} ({top_handguns.handgun})'
    )

    return None


def print_biggest_longguns(agg_df: pd.DataFrame) -> None:
    """
    Imprime por pantalla un mensaje informativo indicando el nombre del estado
    y el año en donde se ha registrado un mayor numero de long_gun.

    Parámetros:
        agg_df: Dataframe resultado de haber aplicado previamente groupby_state_and_year()

    Returns:
        None
    """
    top_longguns = agg_df \
    .sort_values('longgun', ascending=False) \
    .iloc[0]
    print(
        f'El mayor número de armas de fuego largas se ha registrado en {top_longguns.state} en el año {top_longguns.year} ({top_longguns.longgun})'
    )

    return None