import carhire.data as data
from os import path

DB_DIRECTORY = path.dirname(__file__)
DB_NAME = path.join(DB_DIRECTORY, 'carhiredb.sql')
CAR_DATA_FILE = data.CAR_DATA_FILE
BIKE_DATA_FILE = data.BIKE_DATA_FILE
VAN_DATA_FILE = data.VAN_DATA_FILE
CARS_TABLE = 'cars'
BIKES_TABLE = 'bikes'
VANS_TABLE = 'vans'
