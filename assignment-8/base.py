

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:Rdr563455@localhost:1056/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()