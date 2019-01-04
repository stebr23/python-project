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
    CREATE TABLE cars(vehicle_id TEXT, make TEXT, model TEXT, wheels INTEGER, colour TEXT,
                       doors INTEGER, passengers INTEGER, user_id TEXT, bags INTEGER, car_type TEXT)
''')
with open(db_consts.CAR_DATA_FILE) as car_data_file:
    print("CREATE_DB Opened csv")
    reader = csv.DictReader(car_data_file)
    csv_data = [(i['vehicle_id'], i['make'], i['model'], i['wheels'], i['colour'], i['doors'], i['passengers'], i['user_id'], i['bags'], i['car_type']) for i in reader]

cursor.executemany("INSERT INTO cars (vehicle_id, make, model, wheels, colour, doors, passengers, user_id, bags, car_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", csv_data)

'''
Create bikes table
'''
# TODO

'''
Create vans table
'''
# TODO

db.commit()

print("SELECT")
for row in cursor.execute("SELECT * FROM CARS"):
    print(row)

print("UPDATE")
cursor.execute("UPDATE CARS SET user_id=NULL where user_id='NULL'")

print("SELECT")
for row in cursor.execute("SELECT * FROM CARS"):
    print(row)

db.commit()
db.close()
