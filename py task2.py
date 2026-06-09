tasks = []

while True:
    print("TO-DO LIST MENU")
    print("1. add task")
    print("2. view task")
    print("3. mark task as comppleted")
    print("4. delete task")
    print("5. Exit")

    choice = input("enter your choice(1-5)=")
    if choice == "1":
        task = input("enter new task:")
        tasks.append({"task": task,"completed":False})
        print("task added successfully")

    elif choice == "2":
        if not tasks:
            print("no tasks available")
        else:
            print("your tasks:")
            for i, t in enumerate(tasks,start=1):
                status = "completed" if t["completed"] else "pending"
                print(f"{i}. {t['task']}-{status}")

    elif choice == "3":
     if not tasks:
        print("no tasks available")
     else:
      for i, t in enumerate(tasks,start=1):
        print(f"{i}. {t['task']}")

        num = int(input("enter task number to mark as completed="))
        if 1<=num <=len(tasks):
            tasks[num-1]["completed"] =True
            print("task marked as complterd")
        else:
            print("invalid task number")

    elif choice == "4":
     if not tasks:
      print("no tasks available")
     else:
      for i,t in enumerate(tasks, start=1):
        print(f"{i}. {t['task']}")

        num = int(input("enter task number to delete="))
        if 1 <=num <=len(tasks):
            deleted = tasks.pop(num-1)
            print(f"task '{deleted['task']}' deleted")
        else:
            print("invalid task number")
    elif  choice == "5":
     print("thankyou for using TO-DO LIST")
     break
else:
    print("invalid choice try again")