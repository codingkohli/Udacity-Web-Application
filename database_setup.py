#importing the libraries
import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


#creating a base class
Base = declarative_base()


#declaring the class Restaurant
class Restaurant(Base):
    __tablename__ = 'restaurant'
    #defining the contents of the table restaurant
    name = Column(String(80),nullable=False)
    id = Column(Integer,primary_key=True)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    #defining the contents of the table menu_item
    name = Column(String(80),nullable=False)
    id = Column(Integer,primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restraunt_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



#creating an engine of sqlite
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
