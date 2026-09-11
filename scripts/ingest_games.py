import requests

response_col = requests.get("https://api-web.nhle.com/v1/club-schedule-season/COL/20252026")
print(response_col.status_code)

data_col = response_col.json()

games = []

for game in data_col["games"]:
    if game["gameType"] in [2, 3]:
        games.append(game)

print(len([game for game in games if game["gameType"] == 3]))

print(len(games))

response_bracket = requests.get("https://api-web.nhle.com/v1/playoff-bracket/2026")

data_bracket = response_bracket.json()

print(response_bracket.status_code)

print(data_bracket["series"][0])

bracket_col = []

for series in data_bracket["series"]:
    if series["topSeedTeam"]["abbrev"] == "COL" or series["bottomSeedTeam"]["abbrev"] == "COL":
        bracket_col.append(series)

print(bracket_col)