from datetime import date


class Task:  
    def __init__(self,id,description, status = ""):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = date.today()
        self.updateAt = date.today()