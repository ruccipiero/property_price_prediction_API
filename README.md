# Properties price prediction API

This API is designed to predict a price starting from a json file.

To have it working you will have to download the full folder 
here is an exemple of the input: 
```
  {'data':
    {area: int
    property_type: str
    rooms_number: int
    zip_code: int 
    land_area: int
    garden: bool
    garden_area: int
    equipped_kitchen: bool
    full_address: str | None
    swimming_pool: bool
    furnished: bool
    open_fire: bool 
    terrace: bool
    terrace_area: int
    facades_number: int
    building_state: str
    }
    }
```

## The program was tested only on Python 3.10.4
I've made a requirements file for the requirements
