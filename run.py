from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
#creating a DBSession
DBSession = sessionmaker(bind = engine )

session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

session.query(Restaurant).all()

cheesePizza = MenuItem(name= "Cheese Pizza",description = "Made with cheese",course = "Entree",price = "8.99$",restaurant = myFirstRestaurant)
session.add(cheesePizza)
session.commit()
session.query(MenuItem).all()

#querying the db
firstResult = session.query(Restaurant).first()

items = session.query(MenuItem).all()
for item in items:
    print(item.name)