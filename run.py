from keys import google_civic_api
import csv
#Python uses 'packages' to hold a set of tools you don't use all the
#time. But you can import them when you need them. CSV is a package of tools for
#working on CSVs.



counter = 0
with open('alumni.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		# Check folks who were in a candidate track in 2015 or 2016
		if "candidate" in row[6].lower() and ("2015" in row[6].lower() or "2016" in row[6].lower()):
			print row[1]+" "+row[2]+": "+ row[4] + ", " +row[5]+" - "+row[6]+"\n"
			counter +=1
print counter
# Working with a csv file always has these parts:
#---------------------------------------------------
# A line (like line 7) to open the file that tells the computer which file 
# you want to open and some options to help it understand how that file is laid out.

# A line (like line 8) that tells Python how to save the info from the csv in its own
# language.

# A line (like line 9) that starts the for loop that will cycle through all the rows

# Then, the print line prints out the value from the first and second columns for each row