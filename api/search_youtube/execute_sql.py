import os

import psycopg2 as pg
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")


def connect(connection_string: str = CONNECTION_STRING):
    return pg.connect(connection_string)


def execute(query, data: tuple):
    conn = connect()
    cur = conn.cursor()
    sql = query.get_sql()

    cur.execute(sql, data)

    conn.commit()


def execute_and_fetch_all(query, data: tuple):
    conn = connect()
    cur = conn.cursor()
    sql = query.get_sql()

    cur.execute(sql, data)

    result = cur.fetchall()

    conn.commit()

    return result
