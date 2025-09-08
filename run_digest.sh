#!/bin/bash
source /mnt/newsdrive/newsfeed-project/venv/bin/activate
python /mnt/newsdrive/newsfeed-project/scripts/generate_digest.py >> /mnt/newsdrive/newsfeed-project/logs/digest.log 2>&1
