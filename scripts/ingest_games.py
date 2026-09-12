import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("SNOWFLAKE_PASSWORD")

print(os.getenv("SNOWFLAKE_USER"))
print(os.getenv("SNOWFLAKE_ACCOUNT"))

response_col = requests.get("https://api-web.nhle.com/v1/club-schedule-season/COL/20252026")
print(response_col.status_code)

data_col = response_col.json()

games = []

for game in data_col["games"]:
    if game["gameType"] == 2:
        games.append(game)

print(len([game for game in games if game["gameType"] == 2]))

# print(games[0])

print(games[0]["id"])
print(games[0]["homeTeam"]["commonName"]["default"])
print(games[0]["homeTeam"]["abbrev"])
print(games[0]["homeTeam"]["score"])
print(games[0]["awayTeam"]["commonName"]["default"])
print(games[0]["awayTeam"]["abbrev"])
print(games[0]["awayTeam"]["score"])
print(games[0]["gameDate"])



raw_games = []

for game in games:
    raw_games.append({
        "game_id": game["id"],
        "home_team": game["homeTeam"]["commonName"]["default"],
        "home_team_abbrev": game["homeTeam"]["abbrev"],
        "home_team_score": game["homeTeam"]["score"],
        "away_team": game["awayTeam"]["commonName"]["default"],
        "away_team_abbrev": game["awayTeam"]["abbrev"],
        "away_team_score": game["awayTeam"]["score"],
        "game_date": game["gameDate"]
    })

raw_games_df = pd.DataFrame(raw_games)

print(raw_games_df.head())
print(raw_games_df.info())