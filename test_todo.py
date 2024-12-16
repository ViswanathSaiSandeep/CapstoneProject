import pytest
from io import StringIO
from contextlib import redirect_stdout
from todo_functions import add_task, delete_task, view_tasks

def test_add_task():
    tasks = []
    add_task(tasks, task="Buy milk")
    assert tasks == ["Buy milk"], "Task should be added to the list"

def test_delete_task():
    tasks = ["Buy milk", "Walk the dog"]
    delete_task(tasks, task_num=1)
    assert tasks == ["Walk the dog"], "Task should be deleted from the list"

def test_view_tasks_empty():
    tasks = []
    f = StringIO()
    with redirect_stdout(f):
        view_tasks(tasks)
    out = f.getvalue().strip()
    assert out == "No tasks in the list.", "Should indicate no tasks available"

def test_view_tasks_with_tasks():
    tasks = ["Buy milk", "Walk the dog"]
    f = StringIO()
    with redirect_stdout(f):
        view_tasks(tasks)
    out = f.getvalue().strip()
    assert "1. Buy milk" in out and "2. Walk the dog" in out, "Should list all tasks"
