import requests
import json
def check_parameters():
    data = requests.get("https://87h9d4zmpd.execute-api.ap-south-1.amazonaws.com/MAIN/HR_API")
    parameters = data.json()
    return([parameters[0]['HR'],parameters[0]['SPO2'],parameters[0]['Temp']])