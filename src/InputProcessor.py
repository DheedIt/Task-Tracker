import sys
from ent import Task
def inputProcessor(args):
 options = {
  "add": lambda: add(args[1:]),
  "update": lambda: update(args[1:])
  # "delete"
  # "list"
  # "mark-in-progress"
  # "mark-done"
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
 return Task(1,name)

def list(name):
 return Task(1,name)

def markIP(name):
 return Task(1,name)

def markD(name):
 return Task(1,name)


