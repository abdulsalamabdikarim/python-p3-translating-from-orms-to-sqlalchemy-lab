from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(Base, engine):
    if __name__ == '__main__':
        engine = create_engine('sqlite:///dogs.db')
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session(session)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    # dogs = session.query(Dog)
    # return dogs
    return session.query(Dog)
     

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed