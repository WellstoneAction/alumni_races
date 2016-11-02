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
from configure_alumni_races_db import Base, Alumnus, Location, Matched_Race

# 2. Open a database connection
def connect(dbuser, dbpassword, db='alumni_races', host='localhost', port=5432):
	url = 'postgresql://{}:{}@{}:{}/{}'
	url = url.format(dbuser, dbpassword, host, port, db)

	engine = create_engine(url, client_encoding='utf8')

	return engine

engine = connect(dbuser, dbpassword)

print engine

# 3. Add alumni and locations to database from csv
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


counter = 0
with open('alumni.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Eliminate header row
		if row.index !=0:
			constituent_id = row[0]
			first_name = row[1]
			last_name = row[2]
			email = row[3]
			city = row[4].strip()
			state = row[5].strip()
			address_string = (city + " " + state).strip()
			training = row[6]
			counter +=1
			session.add(Alumnus(constituent_id = constituent_id, first_name=first_name, last_name = last_name, email = email, city = city, state = state, training = training))
			session.add(Location(address_string = address_string))
			session.commit()
			print first_name, last_name

print "\n "+str(counter) +" alumni read from csv file."