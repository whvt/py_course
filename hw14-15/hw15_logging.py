import logging
from logging.handlers import TimedRotatingFileHandler

log_format = "%(asctime)s - %(levelname)s - %(message)s"

logger = logging.getLogger("UserActionsLogger")
logger.setLevel(logging.INFO)

file_handler = TimedRotatingFileHandler(
    "user_actions.log", when="midnight", interval=1, backupCount=7, encoding="utf-8"
)
file_handler.setFormatter(logging.Formatter(log_format))

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def simulate_user_actions():
    try:
        logger.info("User started working with the program.")

        logger.info("User performed a successful action.")

        raise ValueError("Error: Invalid data was entered.")
    except ValueError as e:
        logger.error(e)
    finally:
        logger.info("User finished working with the program.")


if __name__ == "__main__":
    simulate_user_actions()
