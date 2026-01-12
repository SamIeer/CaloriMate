from pydantic import BaseModel

class ModelInput(BaseModel):
    id : int
    Sex : str
    Age : int
    Height : float
    Weight : float
    Duration : float
    Heart_Rate : float
    Body_Temp : float

'''
This insures clean input, validate data - no missing or invalid field when API get hitt
'''
#Building a schema read more write more