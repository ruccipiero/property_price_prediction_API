import numpy as np
import json
from fastapi import HTTPException


def preprocess(item):
    data = item.dict()
    clean_entry = data['data']
    if clean_entry['area'] == np.nan or clean_entry['area'] == 0 :
        raise HTTPException(status_code=400, detail="missing value for 'area'")
    if clean_entry['property_type'] not in ["APARTMENT" , "HOUSE" , "OTHERS"]:
    	raise HTTPException(status_code=400, detail="unknown property type, make sure that you've used one of the following:APARTMENT, HOUSE or OTHERS")
    # Categorial data
    if clean_entry["building_state"] not in ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]:
        raise HTTPException(status_code=400, detail="Error, unknown building state, make sure that you've used one of the following:NEW, GOOD, TO RENOVATE, JUST RENOVATED or TO REBUILD")
    #numerical values
    for key, value in clean_entry.items():
        if key == 'building_state':
            if clean_entry[key] == 'NEW':
                clean_entry[key] = 1
            else:
                clean_entry[key] = 0 
        if key in ['garden', 'equipped_kitchen', 'swimming_pool', 'furnished', 'open_fire', 'terrace']:
            if value ==True:
                clean_entry[key] = 1
            else:
                clean_entry[key] = 0
    return clean_entry
