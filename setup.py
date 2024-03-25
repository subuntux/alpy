from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='alpy',  # Der Name Ihres Pakets
    version='0.1.0',  # Die Versionsnummer Ihres Pakets
    author='Kevin Alexander Krefting',
    author_email='kakrefting@gmail.com',
    description='alpy is an modul for easyer python scripts',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yourusername/yourpackage',
    packages=find_packages(),  # Eine Liste der Pakete, die in diesem Modul enthalten sind
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)