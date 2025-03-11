import http.client
import json
#
# conn = http.client.HTTPSConnection("skyscanner89.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-key': "15f5bceb1dmsh1539b8effe70110p1196abjsn5ebd3230ae30",
#     'x-rapidapi-host': "skyscanner89.p.rapidapi.com"
# }
#
# conn.request("GET", "/flights/roundtrip/list?inDate=2025-04-01&outDate=2025-04-21&origin=YYZ&originId=95673353&destination=HNL&destinationId=95673827&cabinClass=economy&adults=1&children=0&infants=0&currency=CAD", headers=headers)
# res = conn.getresponse()
# data = res.read()
#
# # Decode the response data and load it as JSON
# decoded_data = data.decode("utf-8")
# json_data = json.loads(decoded_data)
#
# # Extract flight-specific data from the JSON response
# flights_data = []
#
# # Extract the flight itineraries (assuming flights are in the 'itineraries' field)
# if 'itineraries' in json_data:
#     for itinerary in json_data['itineraries']:
#         flights_data.append(itinerary)
#
# # Now, write the extracted flight data to a text file
# with open("flights_output.txt", "w") as file:
#     json.dump(flights_data, file, indent=2)
#
# print("Filtered flight data saved to flights_output.txt")
#
#
# import http.client
# import json
#
# conn = http.client.HTTPSConnection("skyscanner89.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-key': "15f5bceb1dmsh1539b8effe70110p1196abjsn5ebd3230ae30",
#     'x-rapidapi-host': "skyscanner89.p.rapidapi.com"
# }
#
# # Query for Toronto (YYZ) or change to another airport/city code
# conn.request("GET", "/flights/auto-complete?query=YYZ", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# # Parse and print the response in a readable format
# response_data = json.loads(data.decode("utf-8"))
# print(response_data)
# if 'inputSuggest' in response_data:
#     for suggestion in response_data['inputSuggest']:
#         # Extract the entityId and skyId (airport code) from the navigation section
#         entity_id = suggestion['navigation']['entityId']
#         entity_type = suggestion['navigation']['entityType']
#         name = suggestion['presentation']['title']
#         # Get the skyId (airport code) for AIRPORT type suggestions
#         sky_id = suggestion['navigation']['relevantFlightParams'].get('skyId', None)
#
#         # Print out the information
#         if sky_id:
#             print(f"{name} ({entity_type}) - Entity ID: {entity_id}, Airport Code: {sky_id}")
#         else:
#             print(f"{name} ({entity_type}) - Entity ID: {entity_id}")
# else:
#     print("No suggestions found.")


def flightReader():
    import json

    # Open the JSON file containing the data
    with open("output.txt", "r") as file:
        # Load the content of the file into a Python dictionary
        json_data = json.load(file)

    # Access the 'data' key in the loaded JSON data
    data = json_data.get('data', {})
    itineraries = data.get('itineraries', [])
    flightListFilterNum = 0
    while flightListFilterNum < 3:
        # Check if 'itineraries' exists inside 'data'
        i = 0
        if flightListFilterNum == 0:
            print("BEST:")

        elif flightListFilterNum ==1:
            print("\nCheapest:")

        else:
            print("\nFastest:")

        for x in itineraries["buckets"][flightListFilterNum]["items"]:

            print("\tOption " + str(i+1) + ":" + str(
                itineraries["buckets"][flightListFilterNum]["items"][i]["price"]["raw"]) + "$  with " + str(
                len(itineraries["buckets"][flightListFilterNum]["items"][i]["legs"])) +
                  " legs from ", end="")
            legCount = 0
            for y in int(itineraries["buckets"][flightListFilterNum]["items"][i]["legs"]["stopCount"]):
                if legCount == len(itineraries["buckets"][flightListFilterNum]["items"][i]["legs"]["stopCount"]) - 1:
                    print(legCount)

                    print("and " +
                          itineraries["buckets"][flightListFilterNum]["items"][i]["legs"][legCount]["segments"][legCount]["destination"][
                              "name"], end="")
                else:
                    print(legCount)

                    print(itineraries["buckets"][flightListFilterNum]["items"][i]["legs"][legCount]["segments"][legCount]["destination"][
                              "name"] + ",", end="")

                legCount += 1
            print("\n\t\tID:" + itineraries["buckets"][flightListFilterNum]["items"][i]["id"])
            i += 1
        flightListFilterNum += 1

flightReader()