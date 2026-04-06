import sys
from ent import Task
def inputProcessor(args):
 options = {
  "add": lambda: add(args[1:]),
  "update": lambda: update(args[1:]),
  "delete": lambda: delete(args[1:]),
  "list": lambda: list(args[1:]),
  "mark-in-progress": lambda: markIP(args[1:]),
  "mark-done": lambda: markD(args[1:])
 }
 handler = options.get(args[0], lambda: print('Балбес'))
 handler()

def add(name):
 res = Task(1,name)
 print(res.id,)
 print(res.escription)
 return res
 

def update(name):
 res = Task(1,name)
 print("Обновился")
 return res

def delete(name):
 res = Task(1,name)
 print("удалил")
 return res

def list(name):
 res = Task(1,name)
 print("Лист")
 return res

def markIP(name):
 res = Task(1,name)
 print("mark-in-progres")
 return res

def markD(name):
 res = Task(1,name)
 print("mark-done")
 return res


