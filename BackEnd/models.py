from BackEnd import db

class EmployeeModel(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.Integer())

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"<Employee {self.name}>"