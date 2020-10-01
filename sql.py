
import mysql.connector as mysql

import pandas as pd
from pandas import DataFrame
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

db = mysql.connect(
    host = "localhost",
    user = "root",
    database="mysql"    #chose your database
    
    
)

cursor = db.cursor()

query = input("input SQL Query : ")


cursor.execute(query)

 
#fetching all records from the 'cursor' object
records = cursor.fetchall()
df=DataFrame(records)
print(df)

## Showing the data
'''for record in records:
    print(record)'''

    