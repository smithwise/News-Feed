# step 1 - receive csv inputs (headline & link)
from datetime import date, timedelta  #identifying last week of files via REGEX
import csv #reading archives and creating digest files
import os #directory pathing and file admin
import shutil #for moving files

date_scope = []
digest_dict = {}

for i in range(7):  #identify relevant dates for digest
    date_scope.append(str(date.today() - timedelta(i))) #tuck date objects as string into list

# step 2 - write inputs to dictionary for dedup
for date in date_scope:
    with open("BC-"+date+".csv", "r", newline='') as file: #search file name as template using date
        reader = csv.DictReader(file)
        for row in reader:
            digest_dict.update(row) #write contents of file to dictionary

filename = f"Digest-{date.today()}.csv"
with open(filename, mode="r+",  newline='', encoding='utf-8'):
    writer = csv.DictWriter(file, fieldnames=["title", "link", "date"])
    content = file.read(filename)
    print(content)

''' Misc needs
# error logging
## (try...except) logic needed to log errors (if possible) for final script since this is running without oversight
## perhaps even including the error message in the digest email for the week that fails to run
'''

''' Cleanup routine needs:
# want to move the BC csvs into an archive folder titled "../Digest_Archive/<date>"
# 
'''

''' Email generation needs
'''
# step 3 - draft .msg with UL of hyperlinked headlines
# step 4 - smtp .msg to smithwise.secure@gmail.com

# step 5 - cleanup script, make it look all pythonic and stuff

