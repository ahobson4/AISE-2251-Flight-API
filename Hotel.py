import requests

userAnswer = input("What city do you want to go to: ")

# Step 1: Find the geoId for a location
location_url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation"
location_query = {"query": userAnswer}

APIKey = "9fd6ca82d0msh169764e7d32a755p166de3jsn9492fcfd3dfb"
Host = "tripadvisor16.p.rapidapi.com"

headers = {
    "x-rapidapi-key": APIKey,
    "x-rapidapi-host": Host
}

# Get the geoId for the location
location_response = requests.get(location_url, headers=headers, params=location_query)
location_data = location_response.json()

if location_data.get("status") and location_data.get("data"):
    geoId = location_data["data"][0]["geoId"]  # Use the first result's geoId
    print(f"Found geoId for {userAnswer}: {geoId}")
else:
    print("Failed to find geoId for the location.")
    exit()


# Get the hotel data for the location
APIKey = "9fd6ca82d0msh169764e7d32a755p166de3jsn9492fcfd3dfb"
Host = "tripadvisor16.p.rapidapi.com"
hotel_url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

headers = {
    "x-rapidapi-key": APIKey,
    "x-rapidapi-host": Host
}

# Hardcoded for now change later to input requests from the user
querystring = {
    "geoId": geoId,
    "checkIn": "2025-05-05",
    "checkOut": "2025-05-10",
    "currencyCode": "CAD",
    "priceMax": "500",
    "sort": "REVIEW",
}

response = requests.get(hotel_url, headers=headers, params=querystring)


# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Check if the 'data' key contains hotel information
    if data.get("data", {}).get("data"):
        # Open a file to write the output
        with open("hotels_output.txt", "w") as file:
            # Write each hotel's details to the file
            for hotel in data["data"]["data"]:
                file.write(f"Hotel Name: {hotel.get('title', 'N/A')}\n")
                file.write(f"Price: {hotel.get('priceForDisplay', 'N/A')}\n")
                file.write(f"Rating: {hotel.get('bubbleRating', {}).get('rating', 'N/A')}\n")
                file.write(f"Book through: {hotel.get('provider', 'N/A')}\n")
                file.write("-" * 40 + "\n")
        print("Hotel data written to hotels_output.txt")
    else:
        print("No hotel data found in the API response.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    
