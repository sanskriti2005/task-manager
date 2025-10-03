from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# The DB url
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/taskmanager"

# the engine ("connection factory?")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# sessionlocal : a factory to create a DB session (a session = one unit of work (an interaction? a post, a put, a delete or a get???))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Base: the collctory/ registery for all ORM models
Base = declarative_base()