from keys import google_civic_api, dbuser, dbpassword
import csv
import requests
import pprint
import time
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from configure_db import Base, Alumnus, Location, Matched_Race, Race, Candidate


# Open a database connection
from sqlalchemy.orm import sessionmaker
url = 'postgresql://'+dbuser+':'+dbpassword+'@localhost:5432/alumni_races'
engine = create_engine(url, client_encoding='utf8')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
new_rows_list = []

# Get the header row
with open('survey.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Eliminate header row
		if row[7] == "First name":
			header_row = ["Constituent_ID", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
			new_rows_list.append(header_row)


# alumni = session.query(Alumnus).all()
alumni = session.query(Alumnus).all()

counter = 0
for a in alumni:
	a_name = a.first_name + " "+ a.last_name
	if len(a_name) > 4:
		s = session.query(Candidate).filter(Candidate.name.contains(a_name)).first()
		if s is not None:
			race = session.query(Race).get(s.race_id)
			name_and_district = race.office + " " + race.district_scope + " " + race.district_name
			print name_and_district
			new_row = [a.constituent_id, "I am running for office", name_and_district, "", "", "", "", (a.city +", " + a.state), a.first_name, a.last_name, a.email, ""]
			new_rows_list.append(new_row)
			counter +=1

print counter


outfile = open('api_output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()