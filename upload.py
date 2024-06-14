from database import *
import create
import sqlite3

CONN = sqlite3.connect('WordleWords.db')

WordleDatabase.create_dicts_table(CONN)
WordleDatabase.create_lists_table(CONN)

WordleDatabase.insert_list(CONN, 'Words', create.words)
WordleDatabase.insert_dict(CONN, 'Letter Percentages', create.lDict)
