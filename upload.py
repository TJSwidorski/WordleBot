from database import *
import create
import sqlite3

CONN = sqlite3.connect('WordleDictionary.db')

WordleDatabase.create_dicts_table(CONN)
WordleDatabase.create_lists_table(CONN)

WordleDatabase.insert_list(CONN, 'Words List', create.word_dictionary)
