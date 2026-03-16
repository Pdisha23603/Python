# todo_list = []

# while True:
#     print("    To Do List    ")
#     print("1. Add Task")
#     print("2. View Task")
#     print("3. Delete Task")
#     print("4. Exit")

# select = int(input("enter the task number: "))

# if select == "1":
#     task = inpurt("enter the task: ")
#     todo_list.append(task)
#     print("your task is added successfully!!")

to_do_lst = ["shopping","dusting","sleeping"]
task=input("Enter taks for weekend ")
print(f"{task in to_do_lst}")
print(f"{task not in to_do_lst}")