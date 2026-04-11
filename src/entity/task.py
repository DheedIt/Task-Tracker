from datetime import date
import json
from typing import Any, List
from pathlib import Path

from src.entity.customException import TaskNotFoundError
BASE_DIR = Path(__file__).parent.parent / "jsonVault" / "tasks.json"
path:str = BASE_DIR.as_posix()
class Task:  
    def __init__(self,id:int, description:str, status:str = ""):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = date.today()
        self.updateAt = date.today()
        
    def save(self):
        tasks:List[dict[str,Any]] = []
        if(BASE_DIR.exists()):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения!")
                    return
            tasks.append(self.to_dict())
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=4, ensure_ascii=False)
    @staticmethod
    def listAllTasks():
        tasks:List[dict[str,Any]] = []
        if(BASE_DIR.exists()):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения!")
                    return
            allTasks = [item.get("description") for item in tasks if "description" in item]
            print(allTasks)

    @staticmethod
    def listCompletingTask():
        tasks:List[dict[str,Any]] = []
        if(BASE_DIR.exists()):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения!")
                    return
            print(tasks)
            allTasks = [item['description'] for item in tasks if item['status'] == "Аlready"]
            print(allTasks)

    @staticmethod
    def updateToId(id:int,status:str):
        tasks:List[dict[str,Any]] = []
        if(BASE_DIR.exists()):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения!")
                    return

        for item in tasks:
            if item.get("id") == id:
                print(tasks)
                print(f"Обновили объект под номером{id}")
                item['status'] = status
                item['updateAt'] = date.today
                print(f"Обновили на {status}")
                print(tasks)
                with open(path, 'w', encoding='utf-8') as file:
                    json.dump(tasks, file, indent=4, ensure_ascii=False)
                break
            


    @staticmethod
    def deleteToId(id:str):
        tasks:List[dict[str,Any]] = []
        if(BASE_DIR.exists()):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения!")
                    return
            tasks = [item for item in tasks if item['id'] != int(f"{id}")]
            print(f"Taska{tasks} ")
            print(f"Удалили под номером{id} ")
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=4, ensure_ascii=False)
                
                return tasks

    @staticmethod
    def getLastId() -> int:
        id:int = -1
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data: List[dict[str,Any]] = json.load(file)
                if not data:
                    return 1
            
                item:str = data[-1].get('id', "-1")
                id: int = int(item)
                if(id == -1):
                    raise TaskNotFoundError(Exception)
                return id
        except:
            print('Ошибка преобразования id из str в int')
        return id #Тут ошибка что отсутствует id. Найди способ вытащить его
    
    def to_dict(self) -> dict[str,Any]:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": str(self.createdAt),
            "updateAt": str(self.updateAt)
        }
    
  