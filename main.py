from database import *
import create
import sqlite3

CONN = sqlite3.connect('WordleDictionary.db')

words_list = WordleDatabase.retrieve_list(CONN, 'Words List')

print(len(words_list))