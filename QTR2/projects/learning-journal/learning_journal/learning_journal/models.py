import datetime
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

    #Fix These

    #edited = Column(DateTime, default=datetime.datetime.now)

    @classmethod
    def by_id(self, id):
        return session.query(Entry).order_by(Entry.created)

    # }
Index('my_index', MyModel.name, unique=True, mysql_length=255)
