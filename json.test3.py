import json

# https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python
from pprint import pprint

with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    
pprint(type(fcc_data))
pprint(fcc_data)