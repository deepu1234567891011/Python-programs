tasks = []
task_id_counter = 1  # to give unique IDs to tasks

def add_task(task):
    global task_id_counter
    tasks.append({"id": task_id_counter, "task": task, "status": "Pending"})
    print(f"✅ Task added (ID: {task_id_counter}): {task}")
    task_id_counter += 1

def view_tasks():
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\n📋 TO-DO LIST")
        print("-" * 40)
        print(f"{'ID':<5} {'Task':<20} {'Status':<10}")
        print("-" * 40)
        for t in tasks:
            print(f"{t['id']:<5} {t['task']:<20} {t['status']:<10}")
        print("-" * 40)

def mark_completed(task_id):
    for t in tasks:
        if t["id"] == task_id:
            if t["status"] == "Completed":
                print(f"⚠️ Task {task_id} is already completed.")
            else:
                t["status"] = "Completed"
                print(f"✅ Task {task_id} marked as completed!")
            return
    print("❌ Task ID not found.")

def delete_task(task_id):
    global tasks
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("❌ Task ID not found.")
    else:
        tasks = new_tasks
        print(f"🗑️ Task {task_id} deleted!")

# Main menu
while True:
    print("\n===== ADVANCED TO-DO LIST MENU =====")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        try:
            task_id = int(input("Enter Task ID to mark completed: "))
            mark_completed(task_id)
        except ValueError:
            print("⚠️ Please enter a valid number.")
    elif choice == "4":
        try:
            task_id = int(input("Enter Task ID to delete: "))
            delete_task(task_id)
        except ValueError:
            print("⚠️ Please enter a valid number.")
    elif choice == "5":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")