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
from configure_db import Base, Alumnus, Location, Matched_Race


# 2. Open a database connection
url = 'postgresql://'+dbuser+':'+dbpassword+'@localhost:5432/alumni_races'
engine = create_engine(url, client_encoding='utf8')
print engine


# 3. Add alumni and locations to database from csv
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

###############
# sqlalchamy commands
###############

with open('survey.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Eliminate header row
		if row[7] == "First name":
						header_row = ["Constituent_ID", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
						print header_row