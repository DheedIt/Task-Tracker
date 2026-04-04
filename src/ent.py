from sqlite3 import Date


class Task:  
    def __init__(self,id,escription,status,createdAt,updateAt):
        self.id = id
        self.escription = escription
        self.status = status
        self.createdAt = createdAt
        self.updateAt = updateAt
        
    def __init__(self,id,description):
        self.id = id
        self.escription = description
        self.status = ""
        self.createdAt = Date.today()
        self.updateAt = Date.today()