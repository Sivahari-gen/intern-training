tasks = []   
def add_task(task):
    if task in tasks:
        raise ValueError("Task already exists")
    tasks.append(task)
    print("Task added")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("Task not found")
def show_tasks():
    for task in tasks:
        print(task)

# add_task("learn about git stash")
# add_task("learn about git flags")
# add_task("revise git")
# show_tasks()
# remove_task("complete git")
# remove_task("revise git")
# show_tasks()