import csv
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "list.csv")

class ToDoList():
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = []

    def add(self,task):
        with open(file_path , 'a' , newline="") as output:
            writer  = csv.writer(output)
            writer.writerow([task.name , task.description , task.priority])

    def delete(self,task):
        updated_list = []
        with open(file_path,'r') as input:
            reader = csv.reader(input)
            for row in reader:
                if task.name != row[0]:
                    updated_list.append(row)
        with open(file_path,'w',newline="") as output:
            writer = csv.writer(output)
            writer.writerows(updated_list)

    def show(self):
        with open(file_path,'r',newline='') as input:
            reader = csv.DictReader(input)
            high_priority = []
            medium_priority = []
            low_priority = []
            for row in reader:
                if row["priority"] == "high":
                    high_priority.append(row)
                elif row["priority"] == "medium":
                    medium_priority.append(row)
                elif row["priority"] == "low":
                    low_priority.append(row)
            print("**********High priority tasks**********")
            for row in high_priority:
                print(f"-{row["name"]} : {row["description"]}")
            print("**********Medium priority tasks**********")
            for row in medium_priority:
                print(f"-{row["name"]} : {row["description"]}")
            print("**********Low priority tasks**********")
            for row in low_priority:
                print(f"-{row["name"]} : {row["description"]}")
                
    def save(self):
        pass

class Task():
    def __init__(self,name,description,priority):
        self.name = name
        self.description = description
        self.priority = priority

def write_header():
    with open(file_path , 'w' , newline="") as output:
        writer  = csv.writer(output)
        writer.writerow(["name" , "description" , "priority"])


write_header()
task1  =Task("clean","i have to clean my room","high")
task2  =Task("Gym","go the gym","medium")
task3  =Task("cook","cook pizza","low")

list = ToDoList(file_path)

list.add(task1)
list.add(task2)
list.add(task3)

# list.delete(task2)

list.show()
print(file_path)