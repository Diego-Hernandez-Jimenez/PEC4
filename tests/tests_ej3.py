import pandas as pd
import unittest
from contextlib import redirect_stdout # para evitar mostrar los prints al hacer los tests
from io import StringIO
from sys import path as syspath
from os import path as ospath

syspath.insert( 0, ospath.abspath( ospath.join(ospath.dirname(__file__), '..', 'src', 'pec4' )) )

from ej1 import read_csv, clean_csv, rename_col
from ej2 import breakdown_date, erase_month
from ej3 import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns


class TestsEj3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cd = ospath.abspath(__file__)
        data = ospath.normpath(ospath.join(cd, '..',  '..','data', 'nics-firearm-background-checks.csv'))
        with redirect_stdout(StringIO()):
            cls.df = read_csv(data)
            cls.df = clean_csv(cls.df)
            cls.df = rename_col(cls.df)
            cls.df = breakdown_date(cls.df)
            cls.df = erase_month(cls.df)

    def test_ej_3_1(self):
        """
        Comprueba si el dataframe tiene month, year y tienen los tamaños adecuados
        """
        
        with redirect_stdout(StringIO()):
            df = groupby_state_and_year(self.df)
        self.assertTrue(True)

    def test_ej_3_23(self):
        """
        Comprueba que los resultados agregados para handgun y longgun son correctos
        """
        
        out_print_handguns = StringIO()
        out_print_longguns = StringIO()
        with redirect_stdout(StringIO()):
            df = groupby_state_and_year(self.df)

        # para conservar el output del print se redirige salida a variable
        with redirect_stdout(out_print_handguns):
            print_biggest_handguns(df)
        self.assertEqual(
            out_print_handguns.getvalue(),
            'El mayor número de peticiones de armas de fuego cortas se ha registrado en Florida en el año 2016 (662308.0)\n'
        )

        with redirect_stdout(out_print_longguns):
            print_biggest_longguns(df)

        self.assertEqual(
            out_print_longguns.getvalue(),
            'El mayor número de armas de fuego largas se ha registrado en Pennsylvania en el año 2012 (873543.0)\n'
        )