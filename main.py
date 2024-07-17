#!/usr/bin/env python3.9
import os
import sys
import shutil
import datetime

# Define import and export directories via environment variables (required by pennsieve as of 041924)
src  = os.environ['INPUT_DIR']+'/BIDS/'
dest = os.environ['OUTPUT_DIR']+'/'

# Get a date time for the report
current_time = datetime.datetime.now()
outfile      = f"bidsreport_{current_time.month:02d}{current_time.day:02d}{current_time.year:04d}_{current_time.hour:02d}{current_time.minute:02d}.report"

# Run the command
os.system(f"bids-validator {src} > {dest}{outfile}")