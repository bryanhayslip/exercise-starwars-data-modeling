import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship('Planet')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    residents_id = Column(Integer, ForeignKey('people.id'))
    residents = relationship(People)

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    planets_id = Column(Integer, ForeignKey('planet.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    user = relationship(User)
    planet = relationship(Planet)
    people = relationship(People)





# class Vehicle(Base):
#     __tablename__ = 'vehicle'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     model = Column(String(250))
#     length = Column(Integer)
#     crew = Column(Integer)
#     pilots_id = Column(Integer, ForeignKey('people.id'))
#     pilots = relationship(People)






    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')