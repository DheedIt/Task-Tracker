from typing import  List
from src.entity.task import Task
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def inputProcessor(args:List[str]):
 options = {
  "add": lambda: add(args[1:]),
  "update": lambda: update(args[1:]),
  "delete": lambda: delete(args[1:]),
  "list": lambda: list(),
  "markIP": lambda: markIP(args[1:]),
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

def update(argAll: List[str]):
 idToUpdate = int(argAll[0])
 statusUpdateVal = " ".join(argAll[1:])
 print(idToUpdate)
 print(statusUpdateVal)
 Task.updateToId(idToUpdate, statusUpdateVal)

def delete(id: List[str]):
 if(id.__len__() < 1):
  print("id balbec")
  return
 idTDelete = id[0]
 Task.deleteToId(idTDelete)
 print("Зашли в делейт")

def list():
 Task.listAllTasks()
 print("Лист")

def markIP(argAll: List[str]):
 idChangeStat = int(argAll[0])
 ChangeStat = argAll[1]
 Task.ChangeStat( idChangeStat, ChangeStat)
 print("mark-in-progres")

def markD():
 Task.listCompletingTask()
 print("mark-done")



