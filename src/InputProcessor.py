from typing import List
from src.entity.task import Task
def inputProcessor(args:List[str]) -> None:
 options = {
  "add": lambda: add(args[1:]),
  "update": lambda: update(args[2]),
  "delete": lambda: delete(args[2]),
  "list": lambda: list(),
  "mark-in-progress": lambda: markIP(args[2]),
  "mark-done": lambda: markD(args[2])
 }
 handler = options.get(args[0], lambda: print('Балбес'))
 handler()

def add(name: List[str]):
 fullName:str = " ".join(name)
 res = Task(Task.getLastId()+1,fullName)
 print(res.id,)
 print(res.description)
 return res
 

def update(id: str):
 res = Task(1,name)
 print("Обновился")
 return res

def delete(id: str):
 res = Task()
 print("удалил")
 return res

def list():
 res = Task(1,name)
 print("Лист")
 return res

def markIP(id: str):
 res = Task(1,name)
 print("mark-in-progres")
 return res

def markD(name: str):
 res = Task(1,name)
 print("mark-done")
 return res


