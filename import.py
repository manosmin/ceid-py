import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

empdata1 = pd.read_csv('Graph1.csv', index_col=False, delimiter = ',')
empdata1.head()
empdata2 = pd.read_csv('Graph2.csv', index_col=False, delimiter = ',')
empdata2.head()
empdata3 = pd.read_csv('Graph3.csv', index_col=False, delimiter = ',')
empdata3.head()

try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root') # use your own credentials
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS Python2022CEIDCompilers")
        cursor.execute("CREATE DATABASE Python2022CEIDCompilers")
        print("Database is created")
        cursor.execute("use Python2022CEIDCompilers;")
        cursor.execute('DROP TABLE IF EXISTS graph1;')
        cursor.execute('DROP TABLE IF EXISTS graph2;')
        cursor.execute('DROP TABLE IF EXISTS graph3;')
        print('Creating table....')
        cursor.execute("CREATE TABLE graph1(date varchar(255),total_in_tons int(11))")
        cursor.execute("CREATE TABLE graph2(type varchar(255),total_in_tons int(11))")
        cursor.execute("CREATE TABLE graph3(month varchar(255),total_in_tons int(11))")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata1.iterrows():
            sql = "INSERT INTO graph1 VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
        for i,row in empdata2.iterrows():
            sql = "INSERT INTO graph2 VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
        for i,row in empdata3.iterrows():
            sql = "INSERT INTO graph3 VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
