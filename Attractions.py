
def getAttractions(region, interests):
    import requests
    import json
    from collections import Counter

    url = "https://travel-guide-api-city-guide-top-places.p.rapidapi.com/check"

    querystring = {"noqueue":"1"}

    payload = {
        "region": region,  # reigon is the city name
        "language": "en",
        "interests": interests # interests is a list of strings see the example usage at the end of the file
    }
    headers = {
        "x-rapidapi-key": "8eab76cf9emsha8e7bf7d9471c29p168e19jsn8288762193bf",
        "x-rapidapi-host": "travel-guide-api-city-guide-top-places.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    file_path = response.json()

    # initial output is a json file, so we need to read the file
    # and extract the data and convert it to a list of tuples
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    result = data.get('result', [])
    
    # Extract relevant values and create a list of tuples
    extracted_data = [(item['name'], item['description'], item['type']) for item in result]
    
    # Sort the list of tuples by the 'type' field
    sorted_data = sorted(extracted_data, key=lambda x: x[2])
    
    # Count the number of similar 'type' values
    type_counter = Counter(item[2] for item in sorted_data)
    
    # the output is a list of sorted attractions by type and a counter of the types of attractions
    return sorted_data, type_counter


getAttractions("Paris", ["museum", "park", "restaurant"])