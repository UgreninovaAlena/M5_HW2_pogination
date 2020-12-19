import csv
import os
from pprint import pprint

from pathlib import Path

relative = Path('data.csv')
absolute = relative.absolute()  # absolute is a Path object

pathh=os.path.join(os.getcwd(), 'data-398-2020-12-08.csv')
print(pathh)
with open(pathh, newline='') as csvfile:
    CONTENT = csv.DictReader(csvfile)

pprint(CONTENT)

with open(pathh, newline='') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row['first_name'], row['last_name'])