#!/usr/bin/env python3

import psycopg2
import os

conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
cursor = conn.cursor()
cursor.execute("select * from lol")
records =  cursor.fetchall()
cursor.close()
conn.close()


print("Content-type: application/json")
print()
print("re:Hello world!" + str(records))
