from model import *

db.connect()

# Create the database tables
db.create_tables([User, Document, UserDocument])

# Insérer des données
user1 = User.create(name='Alice')
user2 = User.create(name='Bob')
user3 = User.create(name='Charlie')

doc1 = Document.create(name='The Peewee ORM', year=2019, url='https://docs.peewee-orm.com/')
doc2 = Document.create(name='The Python Language Reference', year=2020, url='https://docs.python.org/3/reference/index.html')
doc3 = Document.create(name='The Flask Mega-Tutorial', year=2021, url='https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world')

UserDocument.create(user=user1, document=doc1, comment='Great documentation!')
UserDocument.create(user=user1, document=doc2, comment='A must-read for Python developers.')
UserDocument.create(user=user2, document=doc2, comment='Very comprehensive.')
UserDocument.create(user=user2, document=doc3, comment='Excellent tutorial.')
UserDocument.create(user=user3, document=doc1, comment='Saved my life!')
UserDocument.create(user=user3, document=doc3, comment='Highly recommended.')
