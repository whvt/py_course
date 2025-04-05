import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_date(prompt):
    while True:
        try:
            user_input = input(prompt)
            date = datetime.strptime(user_input, "%Y-%m-%d")
            logging.info(f"Users input: {user_input}")
            return date
        except ValueError:
            logging.error("Invalid date format. Must use YYYY-ММ-DD.")
            print("Invalid date format. Must use YYYY-ММ-DD.")


date1 = get_date("Input 1st date (YYYY-ММ-DD): ")
date2 = get_date("Input second date (YYYY-ММ-DD): ")


difference = relativedelta(date2, date1)
days_difference = (date2 - date1).days


logging.info(f"Date diff: {date1.date()} and {date2.date()}: {abs(days_difference)} days.")


print(f"Date diff: {abs(days_difference)} days.")
