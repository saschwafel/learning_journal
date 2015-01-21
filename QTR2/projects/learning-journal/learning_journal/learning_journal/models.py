import datetime
from cryptacular.bcrypt import BCRYPTPasswordManager as Manager
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    #name = Column(Text)
    name = Column(Unicode)
    value = Column(Integer)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(Unicode, unique=True, nullable=False)
    
    #created = Column(DateTime, default=datetime.datetime.now)
    created = Column(DateTime, default=datetime.datetime.now)

    edited = Column(DateTime, default=datetime.datetime.now)

    #Fix These


    @classmethod
    def all(cls, session=None):
	if session is None:
	    session = DBSession
#Mine

        #return session.query(cls).all().order_by(cls.created)

#Cris's
	return DBSession.query(cls).order_by(sa.desc(cls.created)).all()
    
    @classmethod
    def by_id(cls, id, session=None):
        """return a single entry identified by id
        If no entry exists with the provided id, return None
        """
        if session is None:
            session = DBSession
        return session.query(cls).get(id)


#    @classmethod
#    def by_id(cls, id, session=None):
#	if session is None:
#	    session = DBSession
#        return session.query(cls).get(id)

    # }

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)

    def verify_password(self, password):
        manager = Manager()
        return manager.check(self.password, password)
    
    @classmethod
    def by_name(cls, name):
        return DBSession.query(User).filter(cls.name == name).first()

Index('my_index', MyModel.name, unique=True, mysql_length=255)
