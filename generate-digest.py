# step 1 - receive csv inputs (headline & link)
from datetime import date, timedelta  #identifying last week of files via REGEX
import csv #reading archives and creating digest files
import os #directory pathing and file admin
import shutil #for moving files

today = date.today()
date_scope = []
digest_dict = {}

for i in range(7):  #identify relevant dates for digest
    date_scope.append(str(today - timedelta(i))) #tuck date objects as string into list

# step 2 - write inputs to dictionary for dedup
for date in date_scope:
    with open("BC-"+date+".csv", "r", newline='') as file: #search file name as template using date
        reader = csv.DictReader(file)
        for row in reader:
            #digest_dict.update() #write contents of file to dictionary
            row["last update"] = date  # add/update the field inside the row
            digest_dict[row["title"]] = row  # store row keyed by title

filename = f"Digest-{today}.csv"
with open(filename, mode="w",  newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link", "last update"])
    writer.writeheader()
    writer.writerows(digest_dict.values())

print(digest_dict)
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


''' GIT Commit comment drafting
first half draft of the Digest creation script. 
Identifies the (BC-<date>.csv) archive files in scope, writes their contents to new dictionary
- WIP creates new CSV from new dictionary
- WIP moves scoped archive files into a new directory 
- SHOULD DO, run a temporary script on Pi to create an initial digest containing all previous articals
- WIP add cron job to run digest script weekly on Tuesdays at 0600
'''
