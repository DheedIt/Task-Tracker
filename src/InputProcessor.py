from typing import  List
from src.entity.task import Task
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def inputProcessor(args:List[str]) -> None:
 options = {
  "add": lambda: add(args[1:]),
  "update": lambda: update(args[1:]),
  "delete": lambda: delete(args[1:]),
  "list": lambda: list(),
  "markIP": lambda: markIP(),
  "markDone": lambda: markD()
 }
 if(len(args) == 0):
  print('Нет аргументов!')
  return

 handler = options.get(args[0], lambda: print('Балбес'))
 handler()

def add(name: List[str]):
 fullName:str = " ".join(name)
 res = Task(Task.getLastId()+1,fullName)
 res.save()
 return res
 

def update(argAll: List[str]):
 idToUpdate = int(argAll[0])
 statusUpdateVal = " ".join(argAll[1:])
 print(idToUpdate)
 print(statusUpdateVal)
 Task.updateToId(idToUpdate, statusUpdateVal)
 res2 = Task(0,"")
 return res2

def delete(id: List[str]):
 idTDelete = id[0]
 Task.deleteToId(idTDelete) 
 print("Зашли в делейт")
 res2 = Task(0,"")
 return res2

def list():
 Task.listAllTasks()
 res = Task(1, " ")
 print("Лист")
 return res

def markIP():
 Task.listInProgres()
 res = Task(1,"")
 print("mark-in-progres")
 return res

def markD():
 Task.listCompletingTask()
 res = Task(1, "")
 print("mark-done")
 return res


