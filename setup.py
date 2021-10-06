'''
Created on 12 juin 2020

@author: tleduc

https://packaging.python.org/tutorials/packaging-projects/
'''
from setuptools import setup, find_packages

from t4gpd.Version import Version


with open('README.md') as readme_file:
    README = readme_file.read()

# with open('HISTORY.md') as history_file:
#     HISTORY = history_file.read()

setup_args = dict(
    name='t4gpd',
    # version='0.0.1',
    version=Version.number(),
    description='Set of tools based on Python, GeoPandas and Shapely to achieve urban geoprocessing',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    # long_description=README + '\n\n' + HISTORY,
    license='GPLv3+',
    # license='MIT',
    packages=find_packages(exclude=["tests", "future"]),
    author='Thomas Leduc',
    author_email='thomas.leduc@crenau.archi.fr',
    keywords=['Geospatial analysis', 'Urban form', 'Urban morphology', 'Isovist'],
    url='https://sourcesup.renater.fr/projects/t4gs',
    download_url='https://sourcesup.renater.fr/frs/?group_id=463',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

install_requires = [
    # 'matplotlib>=2.0.1',
    # 'numpy',
    # 'geopandas',
    # 'shapely'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
