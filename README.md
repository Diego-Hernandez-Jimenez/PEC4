# PEC4

Este paquete contiene una serie de módulos que permiten realizar un preprocesamiento de datos básico y análisis exploratorio del conjunto de datos nics-firearm-background-checks.csv, aunque mcuhas de las funciones incluidas pueden utilizarse aisladamente con otros conjuntos de datos, siempre que se mantenga el mismo esquema.


## Instalación

### Sin utilizar setup.py

Una vez descomprimido el archivo .zip que contiene el proyecto, será necesario revisar los requerimientos en `requirements.txt`. En caso de duda, para garantizar que se cumplen todos los requisitos, se recomienda emplear la instrucción:

```
$ python3 -m pip install -r requirements.txt
```

### Con setup.py

Dado que se ha creado un fichero `setup.py`, es posible instalar el paquete como si fuera un paquete de python normal. Después de descomprimir el archivo y de situarse en el directorio PEC4/, habría que ejecutar:

```bash
$ python3 setup.py install
```
o, si se requieren permisos de administrador:

```bash
$ sudo python3 setup.py install
```

Este método difiere del anterior en que no es necesario revisar manualmente los requisitos, se instalan automáticamente.


## Cómo usar el paquete


### main.py

La función principal que realiza todos los ejercicios de la PEC se encuentra en PEC4/src/pec4/main.py. Para ejecutarla se utiliza la instrucción (se asume que el usuario está en el directorio raíz del proyecto, es decir, /pec4):

```
$ python3 src/modules/main.py
```
De esta manera se ejecutan todos los ejercicios de manera secuencial y utilizando los conjuntos de datos predeterminados. Sin embargo, esta función admite la posibilidad de seleccionar hasta qué ejercicio realizar el análisis y que dataset utilizar. La instrucción anterior equivale a la siguiente (más explícita):


```bash
$ python3 src/pec4/main.py --data nics-firearm-background-checks.csv --ej 6
```

Si se hace, por ejemplo:

```bash
$ python3 src/pec4/main.py --data firearms_duplicate.csv --ej 3
```

Se obtienen las salidas de los 3 primeros ejercicios, habiendo utilizado el conjunto de datos firearms_duplicate.csv, que debe encontrarse en el mismo directorio que nics-firearm-background-checks.csv, es decir, en pec4/data. De no ser así, la ejecución dará error. Igualmente, hay que tener en cuenta que los scripts de los ejercicios asumen que el conjunto de datos tiene la misma estructura que nics-firearm-background-checks.csv. Si el dataset elegido no presenta los mismos campos y tipos, el programa resultará en error.

Para consultar los detalles sobre los argumentos:

```bash
$ python3 src/pec4/main.py --help
```

Durante la ejecución de `main.py`, otras decisiones se solicitarán al usuario. En el ejercicio 5, el siguiente mensaje se muestra en pantalla:

```bash
Introduzca el nombre del fichero csv con los datos de población de E.E.U.U.
(Pulse Enter si va a utilizar los datos por defecto)
```

Por defecto, el fichero utilizado es data/us-state-populations.csv, pero puede indicarse otro, siempre que mantenga la misma estructura y campos. Por ejemplo, podría introducirse "uspop_duplicate.csv" (sin las comillas). En el ejercicio 6 se presentan la siguiente situación:

```bash
Introduzca la ruta y el nombre del fichero que se va a guardar
(Pulse Enter si no desea guardar el mapa generado)
```

que resulta autoexplicativa.


### Módulos aislados

Si se ha instalado el paquete en el sistema, se podrá acceder a él y a sus módulos de la misma forma que se hace con otros paquetes de python. A continuación se muestran algunos ejemplos:

```python
from pec4 import ej1

df = ej1.read_csv(...)
```

```python
from pec4.ej4 import time_evolution

time_evolution(df)
```


### Tests unitarios

Para obtener los resultados de los tests unitarios se utiliza la instrucción (se asume que el usuario está en el directorio raíz del proyecto, es decir, /PEC4):

```bash
$ python3 tests/main_tests.py
```

Si se desean obtener solamente los tests asociados a un ejercicio, se puede utilizar el argumento --ej:

```bash
$ python3 tests/main_tests.py --ej 5
```

Cuando el valor del argumento es 0 se ejecutan todos los tests, equivale al primer comando mostrado.

### Informe de cobertura

Para obtener un informe de cobertura hay que situarse en el directorio raíz del proyecto (/pec4) y ejecutar la siguiente instrucción en consola:

```bash
$ coverage run --source=tests --omit=tests/main_tests.py -m unittest && coverage report

```

Nótese que para que la instrucción se ejecute con éxito será necesario haber instalado previamente `coverage` (por ejemplo, a través del fichero `requirements.txt`)
