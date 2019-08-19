from Flask_App import db,app

class Table(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(50),unique=True,nullable=False)
    Phone=db.Column(db.Integer)
    Color=db.Column(db.String(20),unique=True,nullable=False)
    def __init__(self,Name,Phone,Color):
        self.Name=Name
        self.Color=Color
        self.Phone=Phone