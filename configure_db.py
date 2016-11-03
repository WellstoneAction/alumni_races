#################################
# Wellstone alumni races tracker
# v0.0 2016
#################################


# 1. Import API key and modules
from keys import google_civic_api, dbuser, dbpassword
import csv
import requests
import pprint
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


# 2. Open a database connection
url = 'postgresql://'+dbuser+':'+dbpassword+'@localhost:5432/alumni_races'
engine = create_engine(url, client_encoding='utf8')
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



class Race(Base):
	__tablename__ = 'race'
	id = Column(Integer, primary_key = True)
	candidates = Column(Text)
	district_name = Column(String(250))
	district_scope = Column(String(45))
	level = Column(String(45))
	office = Column(String(250))


class Candidate(Base):
	__tablename__ = 'candidate'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable=True)
	website = Column(String(250), nullable=True)
	campaign_email = Column(String(45))
	campaign_phone = Column(String(25))
	party = Column(String(45))
	twitter = Column(String(250))
	facebook = Column(String(250))
	googleplus = Column(String(250))
	youtube = Column(String(250))
	otherchannel = Column(String(250))
	race_id = Column(Integer, ForeignKey('race.id'))



# Drop all existing tables
Base.metadata.bind = engine
Base.metadata.create_all(engine)