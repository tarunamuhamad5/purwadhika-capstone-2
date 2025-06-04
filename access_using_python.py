import mysql.connector
import pandas as pd

sql_enggine = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="abcde12345",
    database="employees",
)

cursor = sql_enggine.cursor()

query = "select * from employees where gender ='M'"

cursor.execute(query)

result = cursor.fetchall()

df = pd.DataFrame(result, columns=cursor.column_names)
print(df)

# yuhuuu~
# Tamabhan update dari cli
