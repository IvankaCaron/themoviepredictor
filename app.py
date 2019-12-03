#!/usr/bin/python
import mysql.connector as mariadb
import csv



mariadb_connection = mariadb.connect(user='root', password='root', database='themoviepredictor')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM movies")


with open('tmp.csv', 'w', newline='') as csvfile:
    tmp = csv.writer(csvfile)

    tmp.writerows(cursor)

#Test
 

    