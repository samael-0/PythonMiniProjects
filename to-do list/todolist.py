todos = []


def add_task():
    task = input("Enter your task/todo: \n")
    todos.append({"Description": task, "Completed": False})
    print("Task added succesfully")


def remove():
    if not todos:
        print("There's ntg to remove")
    else:

        display_menu()
        index = int(input("Enter the index of task you want to remove"))
        if 0 <= index <= len(todos):
            removed_task = todos.pop(index - 1)
            print(f" Task - {removed_task['Description']} removed successfully")


def display_menu():
    print("Your Tasks!:- ")
    for index, items in enumerate(todos):
        print(
            f" Index:- {index+1} || Task:- {items['Description']} || Completed Status:- {items['Completed'] }"
        )


def main():
    while True:
        add_remove = input(
            "Hey! You want to add(A) remove(R) or view(V) the task and (Q) to quit?: "
        ).lower()
        if add_remove == "a":
            add_task()
        elif add_remove == "v":
            display_menu()
        elif add_remove == "r":
            remove()
        else:
            quit()


main()
