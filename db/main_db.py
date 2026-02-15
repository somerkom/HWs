import config 
import sqlite3
from db import queries
from datetime import datetime

def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.tasks_table)

    conn.commit()
    conn.close()

def add_new_task(name):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    current_date = datetime.now().strftime("%d.%m.%Y %H:%M")

    cursor.execute(queries.insert_tasks, (name, current_date))

    conn.commit()
    id = cursor.lastrowid
    conn.close()

    return id

def edit_task(id, new_value):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.update_tasks, (new_value, id))

    conn.commit()
    conn.close()


def delete_task(id):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_tasks, (id,))
    conn.commit()
    conn.close()
