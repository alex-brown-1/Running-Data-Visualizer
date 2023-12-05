import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

def parse_data(activities, token):
    activities = activities
    param1 = {
    'access_token': token
    }
    
    param2 = {
    'key': "7JHHE5QRZTVR2LGYAX9ANNDVH",
     'include': 'current'
    }
    laps= []
    for activity in activities:
        
        if activity["has_heartrate"]:
            id = activity["id"]
            activity_location = {"latlng": activity["start_latlng"]}
            new_laps = requests.get(f"https://www.strava.com/api/v3/activities/{id}/laps", params=param1).json()
            
            for lap in new_laps:
                lap.update(activity_location)

                time = lap['start_date_local'][:len(lap['start_date_local'])-1]
                lat = lap['latlng'][0]
                lng = lap['latlng'][1]
                
                weather = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lng}/{time}?key=7JHHE5QRZTVR2LGYAX9ANNDVH&include=current").json()
                
                temp = {"temp": weather["currentConditions"]["temp"]}
                dew = {"dew": weather["currentConditions"]["dew"]}
                lap.update(temp)
                lap.update(dew)
                
                laps.append(lap)

    df = pd.DataFrame(laps)
    return df
        