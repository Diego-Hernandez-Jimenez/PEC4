import pandas as pd
import unittest
from contextlib import redirect_stdout # para evitar mostrar los prints al hacer los tests
from io import StringIO
from sys import path as syspath
from os import path as ospath

syspath.insert( 0, ospath.abspath( ospath.join(ospath.dirname(__file__), '..', 'src', 'pec4' )) )

from ej1 import read_csv, clean_csv, rename_col
from ej2 import breakdown_date, erase_month

class TestsEj2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cd = ospath.abspath(__file__)
        data = ospath.normpath(ospath.join(cd, '..',  '..','data', 'nics-firearm-background-checks.csv'))
        with redirect_stdout(StringIO()):
            cls.df = read_csv(data)
            cls.df = clean_csv(cls.df)
            cls.df = rename_col(cls.df)

    def test_ej_2_1(self):
        """
        Comprueba si el dataframe tiene month, year y tienen los tamaños adecuados
        """
        
        with redirect_stdout(StringIO()):
            df = breakdown_date(self.df)
        self.assertIn('month', df.columns)
        self.assertIn('year', df.columns)
        self.assertTrue(
            all([len(m) == 1 or len(m) == 2 for m in df['month'].unique()])
        )
        self.assertTrue(
            all([len(y) == 4 for y in df['year'].unique()])
        )

    def test_ej_2_2(self):
        """
        Comprueba que se ha borrado la columna month
        """
        
        with redirect_stdout(StringIO()):
            df = breakdown_date(self.df)
            df = erase_month(df)

        self.assertNotIn('month', df.columns)