#################################
# Wellstone alumni races tracker guess flag script
# v0.0 2016
#################################


# 1. Import csv modules and states dictionary
import csv

states = {'Mississippi': 'MS', 'Northern Mariana Islands': 'MP', 'Oklahoma': 'OK', 'Wyoming': 'WY', 'Minnesota': 'MN', 'Alaska': 'AK', 'American Samoa': 'AS', 'Arkansas': 'AR', 'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 'Texas': 'TX', 'Tennessee': 'TN', 'Iowa': 'IA', 'Wisconsin': 'WI', 'Arizona': 'AZ', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'District of Columbia': 'DC', 'New Hampshire': 'NH', 'Idaho': 'ID', 'West Virginia': 'WV', 'South Carolina': 'SC', 'California': 'CA', 'Massachusetts': 'MA', 'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Florida': 'FL', 'Hawaii': 'HI', 'Kentucky': 'KY', 'Rhode Island': 'RI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 'Alabama': 'AL', 'Illinois': 'IL', 'Virgin Islands': 'VI', 'South Dakota': 'SD', 'Colorado': 'CO', 'New Jersey': 'NJ', 'National': 'NA', 'Washington': 'WA', 'North Carolina': 'NC', 'Maine': 'ME', 'New York': 'NY', 'Montana': 'MT', 'Nevada': 'NV', 'Delaware': 'DE', 'Guam': 'GU'}

new_rows_list = []
counter = 0
guesses = 0

with open('api_pvs_output_deduped.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		if "Alumnus" not in row[7]:
			state = row[7].split(",")[-1].strip()
			try: 
				state_string = states[state]
			except:
				state_string = ""
			print state_string, row[3]
			if state_string in row[3]:
				new_row = [row[0], "Y", row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
				guesses +=1
			else:
				new_row = [row[0], "", row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
			counter +=1
			print counter
		else:
			new_row = [row[0], "Alumnus state and candidate state match?", row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
		new_rows_list.append(new_row)


print "\n "+str(counter) + " lines read from csv file."
print str(guesses) + " good guesses"

outfile = open('api_pvs_output_deduped_and_flagged.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()