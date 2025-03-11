import requests
import json

url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

headers = {
    "x-rapidapi-key": "9fd6ca82d0msh169764e7d32a755p166de3jsn9492fcfd3dfb",
    "x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
}

# Replace with the actual geoId from Step 1
geoId = "EPSG:4207"  # Use the printed geoId for Lisbon

querystring = {
    "geoId": geoId,
    "latitude": "38.7223",
    "longitude": "-9.1393",
    "checkIn": "2025-04-01",
    "checkOut": "2025-04-05",
    "currencyCode": "CAD",
    "rating": "9",
    "priceMax": "1000"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()

    # Extract hotel names
    hotels = data.get("data", {}).get("hotels", [])
    hotel_names = [hotel.get("name", "Unknown Hotel") for hotel in hotels]

    # Save hotel names to a text file
    with open("hotel_names.txt", "w", encoding="utf-8") as file:
        for name in hotel_names:
            file.write(name + "\n")

    print("Hotel names saved to hotel_names.txt")
else:
    print(f"Error: {response.status_code}, {response.text}")
