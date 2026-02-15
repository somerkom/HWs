tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT
)
"""

read_tasks = """
SELECT id, name, date FROM tasks
"""

update_tasks = """
UPDATE tasks SET name = ? WHERE id = ?
"""

delete_tasks = """
DELETE FROM tasks WHERE id = ?
"""

insert_tasks = "INSERT INTO tasks (name, date) VALUES (?, ?)"
