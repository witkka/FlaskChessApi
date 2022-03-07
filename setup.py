from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    description='Chess api returning valid chess moves',
    author='Katarzyna Witkowska',
    author_email='k.witkowska008@gmail.com',
    url='https://github.com/witkka/FlaskChessApi',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    setup_requires=['pytest-runner', 'black', 'flake8'],
    tests_require=['pytest'],
)
