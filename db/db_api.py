from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="Initial User")

session.add(user)
session.commit()
