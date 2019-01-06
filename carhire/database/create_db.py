"""
Running this file creates the database as well as the Cars table
utilising the car.csv file in the current directory

TODO:
  - Add Bike and Van tables
  - Refactor table creation functionality
  - Migrate to a permanent db solution in the future
"""
import csv
import sqlite3

import carhire.database as db_consts


def drop_table(table_name):
    """
    Drops the provided table from the current database

    :param table_name: String of the name of the table to be dropped
    """
    print('Dropping %s table' % table_name)
    try:
        cursor.execute('''
            DROP TABLE %s
        ''' % table_name)
    except sqlite3.OperationalError:
        print('%s table does not exist yet' % table_name)


def create_car_table():
    """
    Create the car table on the database from the car.csv data file
    located in the current directory.
    """
    drop_table("cars")

    cursor.execute('''
    CREATE TABLE cars(vehicle_id TEXT, make TEXT, model TEXT, wheels INTEGER, colour TEXT,
                       doors INTEGER, passengers INTEGER, user_id TEXT, bags INTEGER, car_type TEXT)
''')
    with open(db_consts.CAR_DATA_FILE) as car_data_file:
        print("CREATE_DB Opened csv")
        reader = csv.DictReader(car_data_file)
        csv_data = [(i['vehicle_id'], i['make'], i['model'], i['wheels'], i['colour'], i['doors'], i['passengers'],
                     i['user_id'], i['bags'], i['car_type']) for i in reader]

    cursor.executemany(
        "INSERT INTO cars (vehicle_id, make, model, wheels, colour, doors, passengers, user_id, bags, car_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
        csv_data)


def create_bike_table():
    """
    Create the bike table on the database from the bike.csv data file
    located in the current directory.
    """
    drop_table("bikes")

    cursor.execute('''
    CREATE TABLE bikes(vehicle_id TEXT, make TEXT, model TEXT, wheels INTEGER, colour TEXT,
                       doors INTEGER, passengers INTEGER, user_id TEXT, storage TEXT)
''')
    with open(db_consts.BIKE_DATA_FILE) as bike_data_file:
        print("CREATE_DB Opened csv")
        reader = csv.DictReader(car_data_file)
        csv_data = [(i['vehicle_id'], i['make'], i['model'], i['wheels'], i['colour'], i['doors'], i['passengers'],
                     i['user_id'], i['storage']) for i in reader]

    cursor.executemany(
        "INSERT INTO bikes (vehicle_id, make, model, wheels, colour, doors, passengers, user_id, storage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
        csv_data)

def create_van_table():
    """
    Unimplemented
    TODO:
      - Create van.csv file
      - Implement
    """
    pass


def create_tables():
    """
    Create the three tables for cars, bikes and vans
    """
    create_car_table()
    create_bike_table()
    create_van_table()


def create_db_connection():
    """
    Create connection to db
    """
    global db, cursor
    db = sqlite3.connect(db_consts.DB_NAME)
    cursor = db.cursor()


def update_null_values():
    """
    Update 'Null' user_id values in the csv file to NULL so they work
    correctly when queried in the code
    """
    cursor.execute("UPDATE CARS SET user_id=NULL where user_id='NULL'")


def commit_and_close_db_connection():
    """
    Commit the changes to the db tables and close the db connection
    """
    db.commit()
    db.close()


create_db_connection()
create_tables()
update_null_values()
commit_and_close_db_connection()
