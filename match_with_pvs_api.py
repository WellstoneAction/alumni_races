from keys import dbuser, dbpassword, pvs_api
import csv
import requests
import pprint
import time
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from configure_db import Base, Alumnus, Location, Matched_Race, Race, Candidate
from votesmart import votesmart

# Open a database connection
url = 'postgresql://'+dbuser+':'+dbpassword+'@localhost:5432/alumni_races'
engine = create_engine(url, client_encoding='utf8')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
new_rows_list = []
votesmart.apikey = pvs_api


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
		try:
			candidates = votesmart.candidates.getByLastname(a.last_name)
			for candidate in candidates:
				if candidate.firstName == a.first_name or candidate.preferredName == a.first_name:
					pprint.pprint(candidate.ballotName)
					name_and_district = candidate.electionOffice + candidate.electionStateId + " "+ candidate.electionDistrictName
					candidate_name = candidate.ballotName
					new_row = [a.constituent_id, "I am running for office", name_and_district, candidate_name, "", "", "", (candidate.electionDistrictName + ", " + candidate.electionStateId), a.first_name, a.last_name, a.email, ""]
					new_rows_list.append(new_row)
					counter +=1
		except:
			pass
print counter

outfile = open('api_pvs_output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()





