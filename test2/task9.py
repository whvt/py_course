import logging
import random

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


class Hero:
    def __init__(self, team, hero_id):
        self.team = team
        self.hero_id = hero_id
        self.level = 1  # Ensure this attribute is initialized

    def level_up(self):
        self.level += 1


class Soldier:
    def __init__(self, team, soldier_id):
        self.team = team
        self.soldier_id = soldier_id

    def move_to_hero(self, hero):
        if hero.team == self.team:
            logger.info(
                f"Soldier {self.soldier_id} is now"
                f" following Hero {hero.hero_id}."
            )
        else:
            logger.info(
                f"Soldier {self.soldier_id} cannot follow"
                f" Hero {hero.hero_id} from a different team."
            )


hero_team1 = Hero("Red", 1)
hero_team2 = Hero("Blue", 2)

soldiers_team1 = []
soldiers_team2 = []

for i in range(1, 21):
    team = random.choice(["Red", "Blue"])
    soldier = Soldier(team, i)
    if team == "Red":
        soldiers_team1.append(soldier)
    else:
        soldiers_team2.append(soldier)

logger.info(f"Number of soldiers in Team1: {len(soldiers_team1)}")
logger.info(f"Number of soldiers in Team2: {len(soldiers_team2)}")

if len(soldiers_team1) > len(soldiers_team2):
    hero_team1.level_up()
    logger.info(
        f"Hero {hero_team1.hero_id} from Team1 leveled up to level {hero_team1.level}."
    )
elif len(soldiers_team2) > len(soldiers_team1):
    hero_team2.level_up()
    logger.info(
        f"Hero {hero_team2.hero_id} from Team2 leveled up to level {hero_team2.level}."
    )
else:
    logger.info("Both teams have the same number of soldiers. No hero levels up.")

if soldiers_team1:
    soldier_to_move = soldiers_team1[0]
    soldier_to_move.move_to_hero(hero_team1)

logger.info(f"Hero ID: {hero_team1.hero_id}, Soldier ID: {soldier_to_move.soldier_id}")
