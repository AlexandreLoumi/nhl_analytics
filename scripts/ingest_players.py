import pandas as pd
import requests
from collections import Counter

team_abbrevs = [
    "ANA", "BOS", "BUF", "CAR", "CBJ", "CGY", "CHI", "COL",
"DAL", "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NJD",
"NSH", "NYI", "NYR", "OTT", "PHI", "PIT", "SEA", "SJS",
"STL", "TBL", "TOR", "UTA", "VAN", "VGK", "WPG", "WSH"
]




players = []

for team in team_abbrevs:
    response = requests.get(f"https://api-web.nhle.com/v1/roster/{team}/20252026")
    data = response.json()

    for key in data.keys():
        for player in data[key]:
            player_data = {}

            player_data["id"] = player["id"]
            player_data["first_name"] = player["firstName"]["default"]
            player_data["last_name"] = player["lastName"]["default"]
            player_data["number"] = player.get("sweaterNumber")
            player_data["position"] = player["positionCode"]
            player_data["shoots_catches"] = player.get("shootsCatches")
            player_data["height"] = player["heightInCentimeters"]
            player_data["weight"] = player["weightInKilograms"]
            player_data["birth_date"] = player["birthDate"]
            player_data["birth_city"] = player["birthCity"]["default"]
            player_data["birth_country"] = player["birthCountry"]
            player_data["team"] = team

            players.append(player_data)


player_ids = [player["id"] for player in players]
print(len(player_ids))
print(len(set(player_ids)))

duplicates = [player_id for player_id, count in Counter(player_ids).items() if count > 1]

print(duplicates)

for player in players:
    if player["id"] == 8482713:
        print(player)

players = list({player["id"]: player for player in reversed(players)}.values())

print(len(set(player_ids)))