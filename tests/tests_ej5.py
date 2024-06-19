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
from ej4 import time_evolution, ej_4_2
from ej5 import groupby_state, clean_states, merge_datasets, calculate_relative_values, ej_5_5

class TestsEj5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cd = ospath.abspath(__file__)
        us_pop = ospath.normpath(ospath.join(cd, '..',  '..','data', 'us-state-populations.csv'))
        data = ospath.normpath(ospath.join(cd, '..',  '..','data', 'nics-firearm-background-checks.csv'))
        with redirect_stdout(StringIO()):
            cls.df_pop = read_csv(us_pop)
            cls.df = read_csv(data)
            cls.df = clean_csv(cls.df)
            cls.df = rename_col(cls.df)
            cls.df = breakdown_date(cls.df)
            cls.df = erase_month(cls.df)
            cls.df = groupby_state_and_year(cls.df)

    def test_ej_5_1(self):
        """
        Comprueba que el dataframe se haya agrupado por state únicamente (no existe year)
        """
        
        with redirect_stdout(StringIO()):
            df = groupby_state(self.df)
        self.assertNotIn('year', df.columns)

    def test_ej_5_2(self):
        """
        Comprueba que se tiene el número correcto de estados
        """
        
        with redirect_stdout(StringIO()):
            df = groupby_state(self.df)
            df = clean_states(df)
        self.assertEqual(df['state'].nunique(), 50 + 1) # 50 estados federales más el distrito de Columbia

    def test_ej_5_3(self):
        """
        Comprueba que la fusión de dataframes es correcta
        """

        with redirect_stdout(StringIO()):
            df = groupby_state(self.df)
            df = clean_states(df)
            merged = merge_datasets(df, self.df_pop)
        self.assertIn('code', merged.columns)
        self.assertIn('pop_2014', merged.columns)
        self.assertEqual(merged.shape[0], df.shape[0]) # no hay pérdida de datos

    def test_ej_5_4(self):
        """
        Comprueba que el los valores relativos se hayan calculado correctamente
        """
        
        with redirect_stdout(StringIO()):
            df = groupby_state(self.df)
            df = clean_states(df)
            merged = merge_datasets(df, self.df_pop)
            merged = calculate_relative_values(merged)

        target = 'permit_perc' # para ser más exhaustivos, habría que hacer operaciones equivalentes para los otros targets
        self.assertIn(target, merged.columns)
        self.assertEqual(merged[target].min(), 0.0)
        self.assertAlmostEqual(merged[target].max(), 736.481220956724)

    def test_ej_5_5(self):
        """
        Comprueba que la modificación de permit_perc se ha producido correctamente
        """
        
        with redirect_stdout(StringIO()):
            df = groupby_state(self.df)
            df = clean_states(df)
            merged = merge_datasets(df, self.df_pop)
            merged = calculate_relative_values(merged)

        avg_permit_perc = merged['permit_perc'].mean().round(2)
        self.assertEqual(avg_permit_perc, 34.88)

        with redirect_stdout(StringIO()):
            merged = ej_5_5(merged)

        avg_permit_perc2 = merged['permit_perc'].mean().round(2)
        self.assertEqual(avg_permit_perc2, 21.12)