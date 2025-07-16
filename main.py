import csv
import os

base_dir = os.path.dirname(__file__)

class ToDoList():
    def __init__(self):
        self.data = []
        self.data.append(["name","description","priority"])

    def add(self,task):
        self.data.append([task.name , task.description , task.priority])

    def delete(self,name):
        is_task_removed = False
        for t in self.data:
            if t[0] == name:
                self.data.remove(t)
                print(f"\x1b[33mTask : {name} removed\033[0m")
                is_task_removed = True
                break
        if not is_task_removed:
            print(f"\033[31mTask with the name:\033[0m{name} \033[31mwasn't found!\033[0m")

    def show(self):
        priority_order = {"high":3,"medium":2,"low":1}
        header , *tasks = self.data
        tasks.sort(key=lambda x : priority_order.get(x[2]),reverse=True)
        self.data = [header] + tasks
        rows = self.data
        # max width for each column
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(len(header))]
        # Print header
        print(" | ".join(str(header[i]).center(col_widths[i]) for i in range(len(header))))
        print("-+-".join('-' * col_widths[i] for i in range(len(header))))
        # Print rows centered
        for row in tasks:
            print(" | ".join(str(row[i]).center(col_widths[i]) for i in range(len(row))))
    def save(self):
        csv_saves = [x for x in os.listdir(base_dir) if x.endswith(".csv")]
        print(f"available csv saves : {" ".join(csv_saves)}")
        print("\033[31mWARNING!\033[0m\nnew save with existing name will overwrite the old save with that name")
        save_name = input("enter a name for your save (example : name) : ")
        while True:
            if save_name.isalpha():
                file_path = os.path.join(base_dir,save_name+".csv")
                with open(file_path,'w',newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(self.data)
                print("\x1b[33mList saved.\033[0m")
                break
            else:
                save_name = input("\033[31mInvalid input!\033[0m\ntry agian (example : name) : ")

    def load(self):
        csv_saves = [x for x in os.listdir(base_dir) if x.endswith(".csv")]
        print(f"available csv saves : {" ".join(csv_saves)}") 
        save_name = input("chose one of these saves (example : name.csv) : ")
        while True:
            if save_name in csv_saves:
                file_path = os.path.join(base_dir,save_name)
                self.data = []
                with open(file_path,'r',newline="") as csvfile:
                    reader = csv.reader(csvfile)
                    self.data = list(reader)
                break
            else:
                save_name = input("\033[31msave file not found!\033[0m\ntry again (example : name.csv) : ")

class Task():
    def __init__(self,name,description,priority):
        self.name = name
        self.description = description
        self.priority = priority

def main():
    my_list = ToDoList()
    app_running = True
    while app_running:
        os.system('cls')
        ascii_art = r"""
    ░██████████  ░██████           ░███████     ░██████      ░██         ░██████  ░██████   ░██████████
        ░██     ░██   ░██          ░██   ░██   ░██   ░██     ░██           ░██   ░██   ░██      ░██    
        ░██    ░██     ░██         ░██    ░██ ░██     ░██    ░██           ░██  ░██             ░██    
        ░██    ░██     ░██ ░██████ ░██    ░██ ░██     ░██    ░██           ░██   ░████████      ░██    
        ░██    ░██     ░██         ░██    ░██ ░██     ░██    ░██           ░██          ░██     ░██    
        ░██     ░██   ░██          ░██   ░██   ░██   ░██     ░██           ░██   ░██   ░██      ░██    
        ░██      ░██████           ░███████     ░██████      ░██████████ ░██████  ░██████       ░██    
        """
        print(ascii_art)
        print("=" * 60)
        print("        Welcome to the To-Do List App".center(60))
        print("            Created by Yasin Purraisi".center(60))
        print("=" * 60)
        print("""
    1-Add a new task
    2-Delete a task
    3-Show all tasks
    4-Save list
    5-Load list
    \x1b[33m6-Quit\033[0m""")
        user_input = int(input("chose an option : "))
        if user_input == 1:
            os.system('cls')
            name1 = input("Name of task : ")
            description1 = input("Description : ")
            priority1 = input("Priority (high,medium,low) : ").lower()
            while priority1 not in ["high","medium","low"]:
                priority1 = input("Invalid input try again (high,medium,low) : ")
            added_task = Task(name1,description1,priority1)
            my_list.add(added_task)
            menu = input("\x1b[32mPress Enter to go back\033[0m\n")
        if user_input == 2:
            os.system('cls')
            name = input("Name of the task you want to delete : ")
            my_list.delete(name)
            menu = input("\x1b[32mPress Enter to go back\033[0m\n")
        if user_input ==3:
            os.system('cls')
            my_list.show()
            menu = input("\x1b[32mPress Enter to go back\033[0m\n")
        if user_input ==4:
            os.system('cls')
            my_list.save()
            menu = input("\x1b[32mPress Enter to go back\033[0m\n")
        if user_input == 5:
            os.system('cls')
            my_list.load()
            menu = input("\x1b[32mPress Enter to go back\033[0m\n")
        if user_input==6:
            app_running = False

if __name__ == "__main__":
    main()