import requests
import pandas as pd
import numpy as np
import datetime

# Setting this option will print all columns of a dataframe
pd.set_option('display.max_columns', None)
# Setting this option will print all of the data in a feature
pd.set_option('display.max_colwidth', None)

# Helper functions to get data from SpaceX API
def getBoosterVersion(data):
    BoosterVersion = []
    for x in data['rocket']:
        if x:
            response = requests.get(f"https://api.spacexdata.com/v4/rockets/{x}").json()
            BoosterVersion.append(response['name'])
    return BoosterVersion

def getLaunchSite(data):
    LaunchSite, Longitude, Latitude = [], [], []
    for x in data['launchpad']:
        if x:
            response = requests.get(f"https://api.spacexdata.com/v4/launchpads/{x}").json()
            LaunchSite.append(response['name'])
            Longitude.append(response['longitude'])
            Latitude.append(response['latitude'])
    return LaunchSite, Longitude, Latitude

def getPayloadData(data):
    PayloadMass, Orbit = [], []
    for load in data['payloads']:
        if load:
            response = requests.get(f"https://api.spacexdata.com/v4/payloads/{load}").json()
            PayloadMass.append(response['mass_kg'])
            Orbit.append(response['orbit'])
    return PayloadMass, Orbit

def getCoreData(data):
    Block, ReusedCount, Serial, Outcome, Flights, GridFins, Reused, Legs, LandingPad = [], [], [], [], [], [], [], [], []
    for core in data['cores']:
        if core['core'] is not None:
            response = requests.get(f"https://api.spacexdata.com/v4/cores/{core['core']}").json()
            Block.append(response.get('block'))
            ReusedCount.append(response.get('reuse_count'))
            Serial.append(response.get('serial'))
        else:
            Block.append(None)
            ReusedCount.append(None)
            Serial.append(None)
        Outcome.append(str(core['landing_success']) + ' ' + str(core['landing_type']))
        Flights.append(core['flight'])
        GridFins.append(core['gridfins'])
        Reused.append(core['reused'])
        Legs.append(core['legs'])
        LandingPad.append(core['landpad'])
    return Block, ReusedCount, Serial, Outcome, Flights, GridFins, Reused, Legs, LandingPad

def main():
    # Fetch SpaceX data
    spacex_url = "https://api.spacexdata.com/v4/launches/past"
    response = requests.get(spacex_url)

    # Check the status code of the response
    print(f"API Response Status Code: {response.status_code}")

    # Check if the response was successful
    if response.status_code == 200:
        # Convert the JSON response to a DataFrame
        data = pd.json_normalize(response.json())
        
        # Get the head of the DataFrame
        print(data.head(5))
    else:
        print("Failed to fetch data from SpaceX API")

    # Check the structure of the data
    print(data.columns)

    # If data is empty or structure is different, use static JSON for testing
    if data.empty:
        static_json_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
        response = requests.get(static_json_url)
        if response.status_code == 200:
            data = pd.json_normalize(response.json())
            print(data.head(5))
        else:
            print("Failed to fetch static JSON data")

    # Lets take a subset of our dataframe keeping only the features we want and the flight number, and date_utc.
    data = data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]

    # We will remove rows with multiple cores because those are falcon rockets with 2 extra rocket boosters and rows that have multiple payloads in a single rocket.
    data = data[data['cores'].map(len)==1]
    data = data[data['payloads'].map(len)==1]

    # Since payloads and cores are lists of size 1 we will also extract the single value in the list and replace the feature.
    data['cores'] = data['cores'].map(lambda x : x[0])
    data['payloads'] = data['payloads'].map(lambda x : x[0])

    # We also want to convert the date_utc to a datetime datatype and then extracting the date leaving the time
    data['date'] = pd.to_datetime(data['date_utc']).dt.date

    # Using the date we will restrict the dates of the launches
    data = data[data['date'] <= datetime.date(2020, 11, 13)]

    # Call helper functions
    BoosterVersion = getBoosterVersion(data)
    LaunchSite, Longitude, Latitude = getLaunchSite(data)
    PayloadMass, Orbit = getPayloadData(data)
    Block, ReusedCount, Serial, Outcome, Flights, GridFins, Reused, Legs, LandingPad = getCoreData(data)

    # Create launch_dict
    launch_dict = {
        'FlightNumber': list(data['flight_number']),
        'Date': list(data['date']),
        'BoosterVersion': BoosterVersion,
        'PayloadMass': PayloadMass,
        'Orbit': Orbit,
        'LaunchSite': LaunchSite,
        'Outcome': Outcome,
        'Flights': Flights,
        'GridFins': GridFins,
        'Reused': Reused,
        'Legs': Legs,
        'LandingPad': LandingPad,
        'Block': Block,
        'ReusedCount': ReusedCount,
        'Serial': Serial,
        'Longitude': Longitude,
        'Latitude': Latitude
    }

    # Create a data from launch_dict
    data2 = pd.DataFrame(launch_dict)

    # Show the head of the dataframe
    print(data2.head(5))

    # Filter for Falcon 9 data
    data_falcon9 = data2[data2['BoosterVersion']=='Falcon 9']
    print(data_falcon9)

    data_falcon9.loc[:,'FlightNumber'] = list(range(1, data_falcon9.shape[0]+1))
    print(data_falcon9)

    print(data_falcon9.isnull().sum())

    # Calculate the mean value of PayloadMass column
    pm_mean = data_falcon9['PayloadMass'].mean()

    # Replace the np.nan values with its mean value
    data_falcon9['PayloadMass'] = data_falcon9['PayloadMass'].replace(np.nan, pm_mean)
    print(data_falcon9)

if __name__ == "__main__":
    main()