#################################
# Wellstone alumni races tracker
# v0.0 2016
#################################


# 1. Import API key and modules
from keys import google_civic_api, dbuser, dbpassword
import csv
import requests
import pprint
import sqlalchemy


# 2. Open a database connection
def connect(dbuser, dbpassword, db='alumni_races', host='localhost', port=5432):
	url = 'postgresql://{}:{}@{}:{}/{}'
	url = url.format(dbuser, dbpassword, host, port, db)

	con = sqlalchemy.create_engine(url, client_encoding='utf8')

	return con

con = connect(dbuser, dbpassword)

print con

# 3. Create location, alumnus, and matching_person tables


# 4. Add potential locations to database from csv


# 5. For each location, send a request to the Google Civic Info API.
#   a. For each candidate running in that location, check to see if
#   b. For each 