#################################
# Wellstone alumni races tracker
# v0.0 2016
#################################


# 1. Import API key and modules
from keys import google_civic_api, dbuser, dbpassword
import csv
import requests
import pprint
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


# 2. Open a database connection
def connect(dbuser, dbpassword, db='alumni_races', host='localhost', port=5432):
	url = 'postgresql://{}:{}@{}:{}/{}'
	url = url.format(dbuser, dbpassword, host, port, db)

	engine = create_engine(url, client_encoding='utf8')

	return engine

engine = connect(dbuser, dbpassword)

print engine

# 3. Create location, alumnus, and matching_person tables
Base = declarative_base()


#Define new tables
class Location(Base):
	__tablename__ = 'location'
	id = Column(Integer, primary_key = True)
	city = Column(String(250))
	state = Column(String(45))
	address_string = Column(String(500), nullable=False)



class Alumnus(Base):
	__tablename__ = 'alumnus'
	id = Column(Integer, primary_key = True)
	constituent_id = Column(String(45))
	first_name = Column(String(45), nullable=True)
	last_name = Column(String(45), nullable=True)
	city = Column(String(250))
	state = Column(String(45))
	email = Column(String(250))
	training = Column(String(1000))
	twitter = Column(String(250))
	facebook = Column(String(250))
	website = Column(String(250))
	candidate = Column(Integer, default = 0)
	campaign_worker = Column(Integer, default = 0)


class Matched_Race(Base):
	__tablename__ = 'matched_race'
	id = Column(Integer, primary_key = True)
	office = Column(String(250))
	level = Column(String(45))
	alumnus_id = Column(Integer, ForeignKey('alumnus.id'))




# Drop all existing tables
Base.metadata.bind = engine
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)