contacts ={}
def add_contact(name, phone):
    contacts[name] = phone
    print("contact added")
def find_contact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("not found")
def list_contacts():
    print("\nContacts:")
    for name in contacts:
        print(name,":",contacts[name])

add_contact("siva", "1234567890")
add_contact("hari", "0987654321")
find_contact("siva")
find_contact("sivahari")
list_contacts()

tasks = []   
def add_task(task):
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

add_task("learn about git stash")
add_task("learn about git flags")
add_task("revise git")
show_tasks()
remove_task("complete git")
remove_task("revise git")
show_tasks()