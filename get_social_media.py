from keys import google_civic_api
import csv
import requests
import pprint
import time


# Open a database connection
new_rows_list = []
counter = 0

# Get the header row
with open('wellstone_alumni_candidate_2016.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		# Eliminate header row
		if row[1] == "First Name":
			header_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
			new_rows_list.append(header_row)
		else:
			print row[1], row[2]
			counter +=1




print str(counter)+ " alumni read"


outfile = open('candidate_soc_media_output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()