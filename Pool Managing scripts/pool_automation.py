import os
import shutil
import json
from pprint import pprint
from os import path

src = path.realpath("litecoin_pool.json")
filename, ext = os.path.splitext(src)

##### Auto file name gen ######

def checkfile(path):
     path = os.path.expanduser(path)

     if not os.path.exists(path):
        return path

     root, ext = os.path.splitext(os.path.expanduser(path))
     dir = os.path.dirname(root)
     fname = os.path.basename(root)
     candidate = fname + ext
     index = 0
     ls = set(os.listdir(dir))
     while candidate in ls:
             candidate = "{}_{}{}".format(fname,index,ext)
             index += 1
     return os.path.join(dir,candidate)
	 
src = path.realpath("litecoin_pool.json")
dst = checkfile(src) 

#######################

#dst = filename + "0" + ext 

shutil.copy(src, dst)

####### change pool id #########

with open(dst) as json_file:  
    data = json.load(json_file)
    #print(data['pools'][0]['id'])
    #pprint(data)
    
    data['pools'][0]['id'] = "ltc2"
    

#write data to a new JSON file      
with open(dst, 'w') as json_file:
    json.dump(data, json_file,indent=4)
