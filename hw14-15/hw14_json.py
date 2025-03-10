import json


with open("football_clubs.json", "r") as file:
    clubs = json.load(file)


max_wins_club = max(clubs, key=lambda club: club["total_wins"])


print(json.dumps(max_wins_club))
