import csv
from requests import get
# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

POSTCODE_URL = 'https://courttribunalfinder.service.gov.uk/search/results.json?postcode='

def data_from_closest_valid_court(court_data: list, court_type: str) -> dict:
    """Gets the court data for the closest court of the correct type, returning
    the relevant information in a dictionary"""
    for court in court_data:
        if court_type in court['types']:
            return {'court_name': court['name'], 'dx_number': court['dx_number'], 'distance': court['distance']}


def get_court_data(person_data: dict) -> dict:
    """Gathering all of the relevcant court and person data, putting in into a dict"""
    response = get(f"{POSTCODE_URL}{person_data['home_postcode']}")
    court_data = response.json()
    closest_court = data_from_closest_valid_court(court_data, person['looking_for_court_type'])
    return {'name': person['person_name'],
            'desired_court_type': person['looking_for_court_type'],
            'home_postcode': person['home_postcode'],
            'court_name': closest_court['court_name'],
            'dx_number': closest_court['dx_number'],
            'distance': closest_court['distance']}


def display_court_data(data: dict):
    """Displays the data in a human readable fashion"""
    print("------------")
    print(f"Name: {data['name']}")
    print(f"Type of court desired: {data['desired_court_type']}")
    print(f"Home postcode: {data['home_postcode']}")
    print(f"Court Name: {data['court_name']}")
    print(f"dx_number: {data['dx_number']}")
    print(f"Distance from home: {data['distance']}")
    print("------------\n")


if __name__ == "__main__":
    with open(f"people.csv", mode='r', encoding="utf-8") as data:
        csv_reader = csv.DictReader(data)
        for person in csv_reader:
            data = get_court_data(person)
            display_court_data(data)
