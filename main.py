from db import main_db
import flet as ft
from datetime import datetime


def main(page: ft.Page):
    tasks_collumn = ft.Column()

    def add_new_task(e):
        def edit_db(id, new_value):
            main_db.edit_task(id, new_value)
            print("Задача успешно обновлена")

        def edit(e):
            task_text.read_only = True
            edit_db(task_id, task_text.value)

        def delete(e):
            tasks_collumn.controls.remove(task_row)
            main_db.delete_task(task_id)
            page.update()

        def add_to_db(name):
            id = main_db.add_new_task(name)
            print(f"Добавлена новая задача: {name} ID: {id}")
            return id

        def to_edit(e):
            task_text.read_only = not task_text.read_only
            page.update()

        if user_input.value:
            task_text = ft.TextField(value=user_input.value, expand=True, read_only=True, on_submit=edit)
            edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
            submit_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=edit)
            delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete)
            task_id = add_to_db(user_input.value)
            user_input.value = ""
            current_date = datetime.now().strftime("%d.%m.%Y %H:%M")
            date_text = ft.Text(current_date, size=12, color="grey")
            task_row = ft.Row([
                task_text,
                date_text,
                edit_button,
                submit_button,
                delete_button
            ])
            tasks_collumn.controls.append(task_row)
            page.update()

    user_input = ft.TextField(
        label="Новая задача", expand=True, on_submit=add_new_task)

    enter_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)
    main_row = ft.Row([user_input, enter_button])
    page.add(main_row, tasks_collumn)


if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main)