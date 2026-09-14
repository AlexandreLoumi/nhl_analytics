import requests
import pandas as pd
import json


response_schedule = requests.get("https://api-web.nhle.com/v1/schedule/2025-10-07")

data_schedule = response_schedule.json()

current_date = data_schedule["regularSeasonStartDate"]
current_date = pd.to_datetime(current_date, format="%Y-%m-%d")
playoff_end = pd.to_datetime(data_schedule["playoffEndDate"])


games = []

while current_date <= playoff_end:
    response_schedule = requests.get(f"https://api-web.nhle.com/v1/schedule/{current_date.strftime('%Y-%m-%d')}")
    data_schedule = response_schedule.json()

    
    for day in data_schedule["gameWeek"]:
        for game in day["games"]:
            if game["gameType"] in (2, 3):
                games.append(game)

    current_date = pd.to_datetime(data_schedule["nextStartDate"], format="%Y-%m-%d")


with open("data/raw/games.json", "w", encoding="utf-8") as f:
    json.dump(games, f, ensure_ascii=False, indent=2)