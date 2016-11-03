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


# Query all locations and exclude the header
locations = session.query(Location).all()[1:]


# For each location, send a request to the Google Civic Info API.

requests_sent = 0
race_names = []
candidate_names = []

# Check ballot info for each location in the database
for location in locations:
	# If the counter is divisible by 100, wait 100 seconds.
	if requests_sent > 0 and requests_sent % 100 == 0:
		time.sleep = 100
	url = "https://www.googleapis.com/civicinfo/v2/voterinfo?key="+google_civic_api+"&address="+location.address_string+"&electionId=2000"
	r = requests.get(url)
	results = r.json()
	requests_sent +=1
	try:
		for i in results["contests"]:
			if i["type"]=="General":
				if i["office"] not in race_names:
					r = Race(candidates = str(i["candidates"]), district_name = i["district"]["name"], district_scope = i["district"]["scope"], level = i["level"], office = i["office"])
					session.add(r)
					session.flush()
					race_id = r.id
					session.commit()
					race_names.append(i["office"])
					print race_id, i["office"]

				for j in i["candidates"]:
					if j["name"] not in candidate_names:
						try:
							name = j["name"]
						except:
							name = ""
						try:
							website = j["candidateUrl"]
						except:
							website = ""
						try:
							email = j["email"]
						except:
							email = ""
						try:
							phone = j["phone"]
						except:
							phone = ""
						try:
							party = j["party"]
						except:
							party = ""
						try:
							for k in j["channels"]:
								if k['type'] == 'Facebook':
									facebook = k['id']
								elif k['type'] == 'Twitter':
									twitter = k['id']
								elif k['type'] == 'GooglePlus':
									googleplus = k['id']
								elif k['type'] == 'YouTube':
									youtube = k['id']
								else:
									otherchannel = k['id']
						except:
							twitter = ""
							facebook = ""
							youtube = ""
							googleplus = ""
						c = Candidate(name = name, website = website, campaign_email = email, campaign_phone=phone, party=party, race_id = race_id, twitter = twitter, facebook=facebook, googleplus=googleplus, youtube=youtube)
						session.add(c)
						session.commit()
						candidate_names.append(j["name"])
						print c.id, c.name
	except:
		pprint.pprint(results)