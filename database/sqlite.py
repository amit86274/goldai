import sqlite3
def connect(path="gold_ai.db"):
    return sqlite3.connect(path)
