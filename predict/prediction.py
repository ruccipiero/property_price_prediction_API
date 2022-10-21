import pandas as pd
import pickle


with open('model/house_model.pkl', 'rb') as house_pickle:
    house_model = pickle.load(house_pickle)
with open('model/apt_model.pkl', 'rb') as apt_pickle:
    apt_model = pickle.load(apt_pickle)

def predict(clean_entry):
    """that will take your preprocessed data as an input and return a price as output."""
    df=pd.DataFrame([clean_entry.values()], columns=clean_entry.keys())
    # House
    if df['property_type'][0] == 'HOUSE':
        feature_names = ['zip_code', 'rooms_number', 'area', 'equipped_kitchen', 'furnished',
        'open_fire', 'terrace', 'terrace_area', 'garden', 'garden_area',
        'land_area', 'facades_number', 'swimming_pool', 'building_state']
        X = df[feature_names]
        results = round(float(house_model.predict(X)))
        return results
    # Apartment
    if df['property_type'][0] == 'APARTMENT':
        feature_names = [ 'area','rooms_number',  'equipped_kitchen', 'furnished',
        'open_fire', 'terrace', 'terrace_area',  'garden', 'garden_area',
        'facades_number', 'swimming_pool', 'building_state'] 
        X = df[feature_names]
        results = round(float(apt_model.predict(X)))
        return results
    # Others
    if df['property_type'][0] == 'OTHERS':
        return 0


