import pandas as pd
from matplotlib.pyplot import show

def time_evolution(df: pd.DataFrame) -> None:
    """
    Crea un gráfico con las siguientes características:
    Eje x: Año
    Eje y: Tres series temporales con el número total de permit, hand_gun y long_gun registrado por cada uno de los años

    Parámetros:
        agg_df: Dataframe con campos year, permit, hand_gun y long_gun

    Returns:
        None
    """

    ax = df \
    .groupby('year')[['permit', 'handgun', 'longgun']] \
    .sum() \
    .rename(columns={'permit': 'permisos', 'handgun': 'pistolas (handguns)', 'longgun': 'rifles (long guns)'}) \
    .plot(
        kind='line',
        style='.-',
        figsize=(15, 5),
        title='Evolución del número de permisos y peticiones de pistolas y rifles en Estados Unidos',
        xlabel='Año',
        ylabel='Recuento total'
    );
    
    show()
    
    return None

def ej_4_2() -> str:
    """
    Muestra un comentario predeterminado en el que se analiza de manera sucinta el gráfico generado
    por time_evolution()
    """

    comment = """
    En el gráfico se aprecia una notable correlación entre las tres variables, lo que sugiere que la demanda de armas 
    es relativamente independiente del tipo de armas demandada. El crecimiento en la demanda de permisos de pistolas suele
    estar asociado también al crecimiento de la demanda de armas largas. Por otro lado, se observa también que la tendencia
    es ascendente, a pesar de la ocurrencia de ciertos picos. Parece que en Estados Unidos el interés por poseer un arma
    no solo se mantiene, sino que aumenta con el tiempo. La brusca bajada en el último año para el que hay registros se debe
    a que se trata de 2020, el año de la pandemia global que obligó al confinamiento. No obstante, dada la excepcionalidad 
    de esta situación y la tendencia observada en años anteriores, cabría esperar una nueva subida en los años siguientes 
    a 2020.
    """
    print(comment)

    return comment