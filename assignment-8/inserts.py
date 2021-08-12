from datetime import date

from actor import Actor
from base import Session, engine, Base
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman

template_folder='methods'
# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create movies
maharshi = Movie("Maharshi", date(2019, 10, 11))
vakeelsab = Movie("Vakeelsab", date(2021, 4, 2))
krack = Movie("Krack", date(2021, 8, 23))

# 5 - creates actors
mahesh_babu = Actor("Mahesh Babu", date(1970, 10, 8))
Pawan_kalyan = Actor("Pawan Kalyan", date(1972, 5, 2))
ravi_teja = Actor("Ravi Teja", date(1971, 6, 5))

# 6 - add actors to movies
maharshi.actors = [mahesh_babu]
vakeelsab.actors = [Pawan_kalyan]
krack.actors = [ravi_teja, mahesh_babu]

# 7 - add contact details to actors
mahesh_contact = ContactDetails("415 555 2671", "Hyderabad,Hitech_city", mahesh_babu)
pawan_contact = ContactDetails("423 555 5623", "Warangal, CA", Pawan_kalyan)
pawan_contact_2 = ContactDetails("421 444 2323", "Krishna, CA", Pawan_kalyan)
ravi_contact = ContactDetails("421 333 9428", "Vishakaptnam, vizag", ravi_teja)

# 8 - create stuntmen
mahesh_stuntman = Stuntman("Harsha", True, mahesh_babu)
pawan_stuntman = Stuntman("satya", True, Pawan_kalyan)
ravi_stuntman = Stuntman("Raj", True, ravi_teja)

# 9 - persists data
session.add(maharshi)
session.add(vakeelsab)
session.add(krack)

session.add(mahesh_contact)
session.add(pawan_contact)
session.add(pawan_contact_2)
session.add(ravi_contact)

session.add(mahesh_stuntman)
session.add(pawan_stuntman)
session.add(ravi_stuntman)

# 10 - commit and close session
session.commit()
session.close()