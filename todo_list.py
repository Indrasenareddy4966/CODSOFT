import os 

class Task: 
    def __init__(self, description): 
        self.description = description 
        self.completed = False 
        
class TodoApp: 
    def __init__(self): 
        self.tasks = []
        
    def add_task(self,description): 
        self.tasks.append(Task(description))
        
    def view_tasks(self): 
        for i , task in enumerate(self.tasks, 1): 
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.description} - {status}")
            
    def mark_task_as_completed(self, index): 
        if 1 <= index <= len(self.tasks): 
            self.tasks[index - 1].completed = True 
        else: 
            print("Invalid index.")
            
    def remove_task(self, index): 
        if 1 <= index <= len(self.tasks): 
            del self.tasks[index - 1]
        else: 
            print("Invalid index.")
            
    def save_tasks(self , filename):
        with open(filename,"w") as f: 
            for task in self.tasks: 
                f.write(f"{task.description},{task.completed}\n")
                
if __name__ == "__main__":
    todo_app = TodoApp()
    
    while True: 
        command = input("Enter a command (add,view,complete,remove,save,quit):")
        if command == "add":
            description = input("Enter task description:")
            todo_app.add_task(description)
        elif command == "view":
            todo_app.view_tasks()
        elif command == "complete": 
            index = int(input("Enter task index to mark as completed:"))
            todo_app.mark_task_as_completed(index)
        elif command == "remove": 
            index = int(input("Enter task index to remove:"))
            todo_app.remove_task(index)
        elif command == "save":
            filename = input("Enter filename to save tasks:")
            todo_app.save_tasks(filename)
        elif command == "quit": 
            break 
        else: 
            prinr("Invalid command.")
