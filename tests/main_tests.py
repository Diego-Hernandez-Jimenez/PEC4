# !/usr/bin/ python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import unittest

def main():
    """
    Esta función permite controlar que test o tests se van a ejecutar
    """
    
    parser = ArgumentParser(description='Ejecuta los tests unitarios de la PEC 4')
    parser.add_argument(
        '--ej',
        type=int,
        default=0,
        choices=range(0, 7),
        help='Ejecuta el conjunto de test del ejercicio seleccionado o ejecuta todos los tests (0)'
    )
    
    ej = parser.parse_args().ej
    
    from tests_ej1 import TestsEj1
    from tests_ej2 import TestsEj2
    from tests_ej3 import TestsEj3
    from tests_ej5 import TestsEj5
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestsEj1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestsEj2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestsEj3)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(TestsEj5)
    suite_all = unittest.TestSuite([suite1, suite2, suite3, suite5])
    
    tests_dic = {'1': suite1, '2': suite2, '3': suite3, '5': suite5, '0': suite_all}
    if ej in [4, 6]:
        print('No se han creado tests para los ejercicios 4 y 6')
    else:
        unittest.TextTestRunner(verbosity=2).run(tests_dic[str(ej)])
    
if __name__ == "__main__":
    main()