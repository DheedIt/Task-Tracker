import sys
from ent import Task
def inputProcessor(args):
 options = {
  "add": lambda: add(args[1])
  # "update"
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
 return Task(1,name)

def delete(name):
 return Task(1,name)

def list(name):
 return Task(1,name)

def markIP(name):
 return Task(1,name)

def markD(name):
 return Task(1,name)


