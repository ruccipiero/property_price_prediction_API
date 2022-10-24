# Properties price prediction API

This API is designed to predict a price starting from a json file.

### Render link:
https://property-price-prediction-api.onrender.com

## Which methods are available?
The available methods are:
> GET /

returns "alive" if everything works
> GET /predict

returns a sting with the input template
>POST /predict 

takes the json file as an input and returns the prediction price with the following format:

``` {"prediction:": actual price as a int } ```

## What kind of input is expected?
Here is a template of the json file format that is expected as an input: 
```
  {'data':
    {area: int,
    property_type: str,
    rooms_number: int,
    zip_code: int ,
    land_area: int,
    garden: bool,
    garden_area: int,
    equipped_kitchen: bool,
    full_address: str | None,
    swimming_pool: bool,
    furnished: bool,
    open_fire: bool, 
    terrace: bool,
    terrace_area: int,
    facades_number: int,
    building_state: str,
    }
    }
```

## What is the output of each route in case of error?
It usually works but it may give a 404 error if the api is not working.

For the POST /predict method:

in case of client error as for example wrong input, an 400 error is provided with a good explanation of the problem, but only for the property type and building state. Because those features have a limited range of values.

You will recieve a 400 error also for missing or 0 value for "area", wich is an important feature.

More generic errors are provided for other input errors... In that case take into account that all the fields, except for full_address, are necessary for the proper operation of the method.

# The API was tested only on Python 3.10.4
You can find a requirements file for the required libraries.
