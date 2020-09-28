import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="Hypyxel", 
    version="0.0.11",
    author="CraziiAce",
    author_email="teddyjraz@gmail.com",
    description="An easy-to-use python wrapper for the Hypixel API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CraziiAce/Hypyxel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
