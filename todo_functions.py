def add_task(tasks, task=None):
    if task is None:
        task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task(tasks, task_num=None):
    if not tasks:
        print("\nNo tasks to delete.")
    else:
        if task_num is None:
            task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted from the list.")
        else:
            print("Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
