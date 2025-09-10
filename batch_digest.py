"""
This script was written to run once, as I have a backlog 
of daily CSVs from the last few months that I want to bunch into digests.

This will group them into digests
"""

import os
import csv
from datetime import date, timedelta
from pathlib import Path

working_date = date.today()
script_dir = Path(__file__).parent.absolute() 
project_root = script_dir.parent
input_dir = project_root / 'archives'
output_dir = project_root / 'digests'
logging_dir = project_root / 'logs'

all_files = os.listdir(str(input_dir))
all_files.sort(reverse=True)

'''Separate out files per week'''
batched_files = []
for i in range(1, len(all_files), 7):  
    # setting start to 1 to batch by Tuesdays to match my weekly cron job (today is Wednesday)
    # ignoring the most recent file is okay because it will get caught by the cron job
    group = all_files[i:i+7]
    batched_files.append(group)
    
for batch in batched_files:
    digest_dict = {}
    batch_name = batch[0]
    for file in batch:
        working_date = file.lstrip('BC-').rstrip('.csv')
        current_file = input_dir / file
        with open(current_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["last updated"] = working_date
                digest_dict[row['title']] = row
    target_out = output_dir / f'Digest-{batch_name.lstrip("BC-")}'
    with open(target_out, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title','link','last updated'])
        writer.writeheader()
        writer.writerows(digest_dict.values())

