import pandas as pd
import unittest
from contextlib import redirect_stdout # para evitar mostrar los prints al hacer los tests
from io import StringIO # necesario para la redirección de los outputs
from sys import path as syspath
from os import path as ospath

# esta operación permite hacer el import de los módulos, aún cuando estén en otro directorio distinto a pwd
syspath.insert( 0, ospath.abspath( ospath.join(ospath.dirname(__file__), '..', 'src', 'pec4' )) )

from ej1 import read_csv, clean_csv, rename_col

class TestsEj1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # para asegurar que siempre se utiliza la ruta adecuada, sin importar
        # desde dónde se ejecute el test 
        cd = ospath.abspath(__file__)
        data = ospath.normpath(ospath.join(cd, '..',  '..','data', 'nics-firearm-background-checks.csv'))
        with redirect_stdout(StringIO()):
            cls.df = read_csv(data)

    def test_ej_1_1(self):
        """
        Comprueba si objeto creado es un DataFrame
        """
        
        self.assertIsInstance(self.df, pd.DataFrame)

    def test_ej_1_2(self):
        """
        Comprueba que el número de columnas sea el adecuado
        """
        
        with redirect_stdout(StringIO()):
            df = clean_csv(self.df)
        self.assertEqual(df.shape[1], 5)

    def test_ej_1_3(self):
        """
        Comprueba que longgun es un campo
        """
        
        with redirect_stdout(StringIO()):
            df = clean_csv(self.df)
            df = rename_col(df)
        self.assertIn('longgun', df.columns)
