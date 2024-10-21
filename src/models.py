import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

{
    "id":"",
    "name":"",
    "post":[
        {
            "user"
            "media": [{
                "imagenes"
            }]

        }
    ]
}

class User(Base):
    __tablename__ = "user"

    id= Column(Integer, primary_key=True)
    username = Column(String(50), unique= True, nullable=False)
    firstname =Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    pass

    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='author')

class Post (Base):
    __tablename__ = "post"
    id = Column (Integer, primary_key=True)
    user_id =Column(Integer)

user = relationship('User', back_populates='posts')
media = relationship('Media', back_populates='post')
comments = relationship('Comment' back_populates='post')

class Comment (Base):
    __tablename__ = "comment"

    id = Column (Integer, primary_key=True)
    content = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id')) # clave foreana falta
    post_id = Column(Integer, ForeignKey('user.id'))   # clave foreana falta

author = relationship('user', back_populates='comments')
post = relationship('Post', back_populates='comments')

class Media(Base):
    __tablename__ ="media"

    id=Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column (Integer, ForeignKey('post.id'))
    type = Column (Enum('video', 'imagen',) nullable= False)

post = relationship('Post', back_populate='media')

class Follower(Base):
    __tablename__="media"
    user_from_id = Column(Integer, ForeignKey('user.id') primary_key = True)
    user_to_id = Column(Integer, ForeignKey ('user.id')primary_key=True)

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

    def to_dict(self):
        return {}
    
query(User)
{
    "id":1,
    "name": "",
    "person": ""
}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
