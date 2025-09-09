from datetime import date, timedelta
import csv
import os
from pathlib import Path

today = date.today()
date_scope = []
digest_dict = {}
log_content = ''

# path variables for I/O file management
script_dir = Path(__file__).parent.absolute()  # parent here indicates the file's parent (directory)
project_root = script_dir.parent  # parent folder of the scripts directory
input_dir = project_root / 'archives'
output_dir = project_root / 'digests'


# identify relevant dates for digest
for i in range(7):
    date_scope.append(str(today - timedelta(i)))

# testing for missing files, generates empty one and logs if so.
for date in date_scope:
    date_name = "BC-" + date + ".csv"
    try:
        for date in date_scope:  
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
