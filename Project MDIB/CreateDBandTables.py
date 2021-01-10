##Create DB File using SQLite3 (For Development)

# import sqlite3 as sql

# conn = sql.connect('unemploymentDatabase.db')

# conn.execute('CREATE TABLE JobsApplied (Site TEXT, Position TEXT, AppDate TEXT, Response TEXT, Interview TEXT)')

# conn.close()


##Create DB File using PostGreSQL (For production)

import os

import psycopg2 as pg

DATABASE_URL = os.environ['DATABASE_URL']

conn = pg.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

cur.execute('CREATE TABLE JobsApplied (Site TEXT, Position TEXT, AppDate TEXT, Response TEXT, Interview TEXT)')

cur.close()

conn.commit()