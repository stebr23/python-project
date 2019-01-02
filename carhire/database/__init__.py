from os import path

DB_DIRECTORY = path.dirname(__file__)
DB_NAME = path.join(DB_DIRECTORY, 'carhiredb.sql')
CAR_DATA_FILE = path.join(DB_DIRECTORY, 'car.csv')
CARS_TABLE = 'cars'
BIKES_TABLE = 'bikes'
VANS_TABLE = 'vans'
