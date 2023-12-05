from flask import request
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

def get_data(code):
    token = get_token(code)
    param = {
    'access_token': token
    }
    activities = requests.get(activities_url, params=param).json()
    return activities


def get_token(code):
    payload = {
    'client_id': "111442",
    'client_secret': "e91b8e82aea1b1d21a93c8888a0c0061e139ddca",
    'code': code,
    'grant_type': "authorization_code"
    }
    res = requests.post(auth_url, data=payload).json()
    return res["access_token"]

print(get_data("51501691aba01044df719ebb0de722cd2f38918c"))