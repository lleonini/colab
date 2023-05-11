from peewee import *

db = SqliteDatabase('database.db')

# ne pas changer cette classe
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()

class Document(BaseModel):
    name = CharField()
    url = CharField()
    year = IntegerField()

class UserDocument(BaseModel):
    # user.documents => UserDocument
    user = ForeignKeyField(User, backref='documents')
    # document.users => UserDocument
    document = ForeignKeyField(Document, backref='users')
    comment = TextField(null=True)
