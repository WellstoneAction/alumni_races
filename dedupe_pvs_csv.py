#################################
# Wellstone alumni races tracker deduplication script
# v0.0 2016
#################################


# 1. Import csv modules
import csv

new_rows_list = []
counter = 0

with open('api_pvs_output.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
		if new_row not in new_rows_list:
			new_rows_list.append(new_row)
		else:
			print "Duplicate removed!"
		counter +=1
		print counter

print "\n "+str(counter) + " lines read from csv file."
print str(len(new_rows_list)) + " total lines after de-duping"

outfile = open('api_pvs_output_deduped.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(new_rows_list)
outfile.close()