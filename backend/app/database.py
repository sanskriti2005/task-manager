from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# The DB url
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/taskmanager"

# Let's break down this url, this url is formed from the variables you made in yout docker-compose file
# postgresql:// this tells us that we are connected to postgres
# postgres:postgres this is the username and password you made in your docker-compose file
# @db: this is the hostname of the database container, this is the name of the
# this db will probably be localhost if you are not using docker
# :5432 this is the port that the database is running on, this is the port
# /taskmanager this is the name of the database we are connecting to, I used the name of the project to keep it simple

# the engine ("connection factory?")
#  All I can say is that it connects us to the db
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# sessionlocal : a factory to create a DB session (a session = one unit of work (an interaction= a post, a put, a delete and a get))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Base: the collctory/ registery for all ORM models
Base = declarative_base()