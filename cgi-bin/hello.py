#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect("sammy","postgres","","localhost")
cursor = conn.cursor()
cursor.execute("select * from lol")
records =  cursor.fetchall()
cursor.close()
conn.close()


print("Content-type: application/json")
print()
print("re:Hello world!" + str(records))
