# !/usr/bin/ python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import path
import pandas as pd

def main():
    """
    Esta función permite controlar qué ejercicios se muestran y qué datos se utilizan
    """

    parser = ArgumentParser(description='Ejecuta los ejercicios de la PEC 4')
    parser.add_argument(
        '--data',
        type=str,
        default='nics-firearm-background-checks.csv',
        help='Nombre fichero csv que contiene los datos de E.E.U.U.'
    )
    parser.add_argument(
        '--ej',
        type=int,
        default=6,
        choices=range(1, 7),
        help='Ejecuta secuencialmente los n primeros ejercicios, siendo n el valor proporcionado en --ej'
    )

    args = parser.parse_args()
    data = args.data
    
    # para asegurar que siempre se utiliza la ruta adecuada, sin importar
    # desde dónde se ejecute main.py 
    # ref: https://stackoverflow.com/questions/14424514/getting-correct-path-of-a-folder-in-python
    mainpy_dir = path.abspath(__file__)
    data = path.normpath(path.join(mainpy_dir, '..',  '..', '..', 'data', args.data))
    ej = args.ej

    # ejercicio 1
    print(
    """
    ###################
    Ejercicio 1
    ###################
    """
    )
    
    from ej1 import read_csv, clean_csv, rename_col
    
    df = read_csv(data)
    df = clean_csv(df)
    df = rename_col(df)
    if ej == 1:
        return None

    # ejercicio 2
    print(
    """

    ###################
    Ejercicio 2
    ###################
    """
    )
    
    from ej2 import breakdown_date, erase_month
    
    df = breakdown_date(df)
    df = erase_month(df)
    if ej == 2:
        return None

    # ejercicio 3
    print(
    """

    ###################
    Ejercicio 3
    ###################
    """
    )
    
    from ej3 import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
    
    df = groupby_state_and_year(df)
    print_biggest_handguns(df)
    print_biggest_longguns(df)
    if ej == 3:
        return None

    # ejercicio 4
    print(
    """

    ###################
    Ejercicio 4
    ###################
    """
    )
    
    from ej4 import time_evolution, ej_4_2
    
    time_evolution(df)
    ej_4_2()
    if ej == 4:
        return None

    # ejercicio 5
    print(
    """

    ###################
    Ejercicio 5
    ###################
    """
    )
    
    from ej5 import groupby_state, clean_states, merge_datasets, calculate_relative_values, ej_5_5
    
    csv_population = input(
        """
        Introduzca el nombre del fichero csv con los datos de población de E.E.U.U.
        (Pulse Enter si va a utilizar los datos por defecto)
        """
    )
    
    if not csv_population:
        csv_population = 'us-state-populations.csv'
    
    us_pop_path = path.normpath(path.join(mainpy_dir, '..',  '..', '..', 'data', csv_population))
    df_population = pd.read_csv(us_pop_path)

    df = groupby_state(df)
    print('\n')
    df = clean_states(df)
    print('\n')
    df = merge_datasets(df, df_population)
    print('\n')
    df = calculate_relative_values(df)
    df = ej_5_5(df)
    if ej == 5:
        return None

    # ejercicio 6
    print(
    """
    ###################
    Ejercicio 6
    ###################
    """
    )
    
    from ej6 import plot_choropleth

    save_path = input(
    """
    Introduzca la ruta y el nombre del fichero que se va a guardar
    (Pulse Enter si no desea guardar el mapa generado)
    """
    )
    plot_choropleth(df, save_path)


if __name__ == "__main__":
    main()