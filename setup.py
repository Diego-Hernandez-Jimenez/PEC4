from setuptools import setup, find_packages

setup(
    name='pec4',
    version='0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'coverage==7.5.3',
        'folium==0.17.0',
        'matplotlib==3.7.1',
        'pandas==1.5.3',
    ],
    url='https://github.com/Diego-Hernandez-Jimenez/pec4',
    license='MIT',
    author='Diego Hernández Jiménez',
    author_email='dhernande685@uoc.edu',
    description='Paquete con las respuestas a la PEC 4'
)