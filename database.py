from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///user_db.db', echo=False)
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
