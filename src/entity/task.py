from datetime import date
import json
from typing import List


class Task:  
    def __init__(self,id:int, description:str, status:str = ""):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = date.today()
        self.updateAt = date.today()
        
    def save(self, task: Task):
     with open('jsonVault/tasks.json', 'w', encoding='utf-8') as file:
           json.dump(task, file, indent=4, ensure_ascii=False)
        
    def load(self,id:int) -> Task:
        with open('jsonVault/tasks.json', 'r', encoding='utf-8') as file:
            data: Task = json.load(file)
            print(f'{data}')
        return self
    @staticmethod
    def getLastId() -> int:
        with open('jsonVault/tasks.json', 'r', encoding='utf-8') as file:
            data: List[Task] = json.load(file)
        return data[-1].id