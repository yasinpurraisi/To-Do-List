import csv
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "list.csv")

class ToDoList():
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = []
        self.data.append(["name","description","priority"])

    def add(self,task):
        self.data.append([task.name , task.description , task.priority])

    def delete(self,task):
        for t in self.data:
            if t[0] == task.name:
                self.data.remove(t)

    def show(self):
        priority_order = {"high":3,"medium":2,"low":1}
        header , *tasks = self.data
        tasks.sort(key=lambda x : priority_order.get(x[2]),reverse=True)
        self.data = header + tasks
    def save(self):
        pass
        

class Task():
    def __init__(self,name,description,priority):
        self.name = name
        self.description = description
        self.priority = priority


task1  =Task("clean","i have to clean my room","high")
task2  =Task("Gym","go the gym","medium")
task3  =Task("cook","cook pizza","low")
task4  =Task("code","project","high")

list = ToDoList(file_path)

list.add(task1)
list.add(task2)
list.add(task3)
list.add(task4)
# list.delete(task2)

list.show()
print(list.data)