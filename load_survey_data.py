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

address_strings = []

counter = 0
matches = 0
new_rows_list = []

with open('survey.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Eliminate header row
		if row[7] != "First name":
			csv_first_name = row[7].strip().capitalize()
			csv_last_name = row[8].strip().capitalize()
			counter +=1
			a = session.query(Alumnus).filter(Alumnus.last_name.ilike(csv_last_name)).filter(Alumnus.email.like(csv_first_name)).first()
			a = session.query(Alumnus).filter(Alumnus.last_name.ilike(csv_last_name)).filter(Alumnus.first_name.ilike(csv_first_name)).first()
			if a:
				constituent_id = a.constituent_id
				matches +=1

			else:
				constituent_id = ""
			new_row = [constituent_id, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
			new_rows_list.append(new_row)
		else:
			header_row = ["Constituent_ID", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
			new_rows_list.append(header_row)			


      
# Do the writing
outfile = open('survey_output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()

print "\n "+str(counter) +" alumni read from csv file."
print "\n "+str(matches) +" matched the database."
