from keys import google_civic_api
import csv
import requests
import pprint

counter = 0
addresses = []
names = []
with open('alumni.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Eliminate header row
		if row.index !=0:
			name = row[1]+" "+row[2] 
			if name not in names:
				names.append(name)
			address = (row[4].strip() + " " +row[5].strip()).strip()
			training = row[6]
			if len(address) > 0:
				if address not in addresses:
					addresses.append(address)
				counter +=1

print "\n "+str(counter) +" unique alumni read from csv file."
print " Alumni reported "+ str(len(addresses)) + " unique addresses.\n"


candidates = []
matched_candidates = []
# Check ballot info for the town where this person lives
for address in addresses:
	url = "https://www.googleapis.com/civicinfo/v2/voterinfo?key="+google_civic_api+"&address="+address+"&electionId=2000"
	r = requests.get(url)
	results = r.json()

	try:
		for i in results["contests"]:
			if i["type"]=="General":
				for j in i["candidates"]:
					candidate_name = j["name"]
					candidates.append(candidate_name)
					if candidate_name in names:
						if candidate_name not in matched_candidates:
							pprint.pprint(j["name"])
							matched_candidates.append(candidate_name)
	except:
		print address
		pprint.pprint(results)

print len(candidates)
print matched_candidates


# 3. Add alumni to database from csv


# 4. Add potential locations to database from csv


# 5. For each location, send a request to the Google Civic Info API.
#   a. For each candidate running in that location, check to see if
#   b. For each 