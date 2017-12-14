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
"""for item in items:
    print(item.name)"""

# working on the update command
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
"""for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.name)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
"""
urbanVeggieBurger = session.query(MenuItem).filter_by(id = 11).one()
#print(urbanVeggieBurger.name,urbanVeggieBurger.price)
urbanVeggieBurger.price = "$2.99"
session.add(urbanVeggieBurger)
session.commit()

