from keys import google_civic_api
import csv
import requests
import pprint
import time


# Open a database connection
new_rows_list = []
counter = 0
requests_sent = 0

# Get the header row
with open('wellstone_alumni_candidate_2016.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		counter +=1
		print counter
		# Eliminate header row
		if row[1] == "First Name":
			header_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
			new_rows_list.append(header_row)
		else:
			first_name = row[1]
			last_name = row[2]
			location = row[3]
			print first_name + " " + last_name + " : " + location
			if requests_sent > 0 and requests_sent % 100 == 0:
				time.sleep = 100
			url = "https://www.googleapis.com/civicinfo/v2/voterinfo?key="+google_civic_api+"&address="+location+"&electionId=2000"
			r = requests.get(url)
			results = r.json()
			try:
				for i in results["contests"]:
					if i["type"]=="General":
						try:
							for j in i["candidates"]:
								twitter = ""
								facebook = ""
								youtube = ""
								googleplus = ""
								otherchannel = ""
								if last_name in j["name"]:
									try:
										website = j["candidateUrl"]
									except:
										website = ""
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
										pass
									new_row = [row[0], row[1], row[2], row[3], row[4], row[5], facebook, twitter, website, googleplus, youtube, otherchannel]
									new_rows_list.append(new_row)
							requests_sent +=1

						except:
							pass
			except:
				pass

print str(counter)+ " alumni read"


outfile = open('candidate_soc_media_output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()