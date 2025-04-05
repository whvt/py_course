import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Order:
    statuses = ["PENDING", "IN_PROGRESS", "READY", "COMPLETED", "CANCELLED"]

    def __init__(self, order_id, status="PENDING"):
        if status not in self.statuses:
            raise ValueError(
                f"Status {status} is invalid. Valid statuses: {', '.join(self.statuses)}"
            )
        self.order_id = order_id
        self.status = status
        logging.info(f"Order {self.order_id} is placed with status {self.status}")

    def update_status(self, new_st):
        if new_st not in self.statuses:
            raise ValueError(
                f"Status {new_st} is invalid. Valid statuses: {', '.join(self.statuses)}"
            )
        logging.info(f"Updating {self.order_id} order: {self.status} -> {new_st}")
        self.status = new_st

    def display_status(self):
        logging.info(f"Getting order's {self.order_id} status:")
        return f"->Order {self.order_id}: {self.status}"


order1 = Order(11111, "PENDING")
order2 = Order(11112, "IN_PROGRESS")
order3 = Order(11113, "READY")
order4 = Order(11114, "PENDING")

orders = [order4, order2, order3, order1]


order1.update_status("IN_PROGRESS")
order2.update_status("READY")


for order in orders:
    logging.info(order.display_status())
