import csv
import sqlite3

import carhire.database as db_consts


def drop_table(table_name):
    print('Dropping %s table' % table_name)
    try:
        cursor.execute('''
            DROP TABLE %s
        ''' % table_name)
    except sqlite3.OperationalError:
        print('%s table does not exist yet' % table_name)


db = sqlite3.connect(db_consts.DB_NAME)
cursor = db.cursor()

'''
Create cars table
'''
drop_table("cars")
cursor.execute('''
    CREATE TABLE cars(vehicle_id INTEGER, make TEXT,
                       model TEXT, wheels INTEGER, colour TEXT,
                       doors INTEGER, passengers INTEGER, bags INTEGER, type TEXT, user_id TEXT)
''')
with open(db_consts.CAR_DATA_FILE) as car_data_file:
    reader = csv.DictReader(car_data_file)
    csv_data = [(i['car_id'], i['make'], i['model'], i['wheels'], i['colour'], i['doors'], i['passengers'], i['bags'], i['type'], i['user_id']) for i in reader]

cursor.executemany("INSERT INTO cars (vehicle_id, make, model, wheels, colour, doors, passengers, bags, type, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", csv_data)

'''
Create bikes table
'''
# TODO

'''
Create vans table
'''
# TODO

db.commit()
db.close()
