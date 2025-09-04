from datetime import date, timedelta  #identifying last week of files via REGEX
import csv #reading archives and creating digest files
import os
from pathlib import Path

today = date.today()
date_scope = []
digest_dict = {}
log_content = ''

# path variables for I/O file management
cwd = Path.cwd()
home_dir = cwd.parent
input_dir = home_dir / 'archives'
output_dir = home_dir / 'digests'


# identify relevant dates for digest; MAY CHANGE THIS
#
# If changed, would target all files matching name template in source folder
# (this would be reliant on cleanup operations moving old files once processed)
for i in range(7):
    date_scope.append(str(today - timedelta(i)))

# testing for missing files, generates empty one and logs if so.
for date in date_scope:
    date_name = "BC-" + date + ".csv"
    try:
        for date in date_scope:  # could change to for file in source_dir:
            target_name = "BC-"+date+".csv"
            target_file = input_dir / target_name
            # search file name as template using date
            with open(target_file, "r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["last update"] = date
                    digest_dict[row["title"]] = row
    except:
        with open(target_file, "w", newline='',  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title','link'])
            writer.writerow([f'{date_name} no file found, generated empty file','n/a'])

# taking contents of source files and generating new CSV with the cumulation
filename = f"Digest-{today}.csv"
target_out = output_dir / filename
with open(target_out, mode="w",  newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link", "last update"])
    writer.writeheader()
    writer.writerows(digest_dict.values())

print(f"cwd={cwd} \n home={home_dir} \n input={input_dir} \n output={output_dir}")
''' Misc needs
#### need path awareness - source files, script, and output are all in separate locations

# error logging
## (try...except) logic needed to log errors (if possible) for final script since... 
   ## this is running without oversight
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
