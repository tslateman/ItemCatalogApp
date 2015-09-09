from sqlalchemy import create_engine	
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, User, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

items = session.query(Item)
for item in items:
	session.delete(item)
	session.commit()

categories = session.query(Catalog)
for category in categories:
	session.delete(category)
	session.commit()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

Category1 = Catalog(category="Basic", user=User1)
session.add(Category1)
session.commit()

Item1 = Item(name="FirstItem", description="Hello! This is the first item",
			price="$9.99", catalog=Category1, user=User1)
session.add(Item1)
session.commit()

Item2 = Item(name="SecondItem", description="Hello! This is item number two",
			price="$12.99", catalog=Category1, user=User1)
session.add(Item2)
session.commit()

Category2 = Catalog(category="Furniture", user=User1)
session.add(Category2)
session.commit()

Item3 = Item(name="Chair", description="The long lost comfortable chair",
			price="$19.99", catalog=Category2, user=User1)
session.add(Item3)
session.commit()

Item4 = Item(name="Table", description="Something to eat off of",
			price="$12.99", catalog=Category2, user=User1)
session.add(Item4)
session.commit()

print "Added Items!"