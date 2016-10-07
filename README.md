# alumni_races

This collection of Python scripts finds out if the alumni in a csv are currently running for office or working on a candidate race.

Files
=====
(1) Alumni lists should not be committed to this repository, but should be .csvs files formatted with columns:
- Constituent ID
- First name
- Last name
- Email number
- Preferred City
- Preferred State
- Event Name


(2) A keys file holds API credentials

(3) run.py is the main file to execute - ultimately it outputs a separate CSV formatted as detailed in "Outputs" below



Data sources
============

run.py draws on the Google Search API, the Google Civic Information API, and matches to CSVs exported from Raiser's Edge


Output
=======

run.py outputs a csv that contains:
- Constituent IDs and all other original information for alumni. The constituent ID allows easy matching back into RE.
- A field indicating "Yes" is the alumnus is running for office in 2016
- A field indicating "Yes" if the alumnus is working on a candidate race in 2016
- The race on which the alumnus is running/working
