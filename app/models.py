from flask_appbuilder import Model
from sqlalchemy import Column, Integer

class Data(Model):
    id = Column(Integer, primary_key=True)
    cislo = Column(Integer(), nullable=False)

    def __repr__(self):
        return self.cislo