import json
from pprint import pprint

with open('litecoin_pool.json') as json_file:  
    data = json.load(json_file)
    #print(data['pools'][0]['id'])
    #pprint(data)
    
    data['pools'][0]['id'] = "ltc2"
    

#write data to a new JSON file      
with open('litecoin_pool.json', 'w') as json_file:
    json.dump(data, json_file,indent=4)
