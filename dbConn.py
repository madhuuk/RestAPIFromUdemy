import sqlite3


def dbConn():
    conn = sqlite3.connect('../data.db')
    cur = conn.cursor()

    return cur, conn


def closedb(conn):
    conn.commit()

    conn.close()
