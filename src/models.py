import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)

    def to_dict(self):
        return {}
    
class planet(Base):
    __tablename__="planet"

    id = Column (Integer, primary_key=True)
    name=Column(String(200))
    population=Column(Integer)
    weather=Column(String(50))

class character(Base):
    __tablename__="character"

    id = Column (Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)
    zodiac = Column(String(100))

class favorite(Base):
    __tablename__="favorite"

    id = Column(Integer, primary_key=True)
    
    user_id=Column(Integer, ForeignKey('user.id'))
    user=relationship(user)

    character_id=Column(Integer, ForeignKey('user.id'))
    character=relationship(character)

    planet_id=Column(Integer, ForeignKey('user.id'))
    planet=relationship(planet)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
