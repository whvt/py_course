class Deposit:
    def __init__(self, start_balance, years, interest_rate=0.10):
        self.start_balance = start_balance
        self.years = years
        self.interest_rate = interest_rate
        self.current_balance = start_balance

    def calculate_monthly_compound_interest(self):
        months = self.years * 12
        monthly_rate = self.interest_rate / 12
        for _ in range(months):
            self.current_balance += self.current_balance * monthly_rate
        return round(self.current_balance, 2)


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.deposit_account = None

    def open_deposit_account(self, start_balance, years):
        self.deposit_account = Deposit(start_balance, years)

    def calc_interest_rate(self):
        if self.deposit_account:
            return self.deposit_account.calculate_monthly_compound_interest()
        else:
            raise ValueError("No deposit account found.")

    def close_deposit(self):
        if self.deposit_account:
            final_amount = self.calc_interest_rate()
            self.deposit_account = None
            return final_amount
        else:
            raise ValueError("No deposit account found.")


class Bank:
    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name)

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            self.clients[client_id].open_deposit_account(start_balance, years)

    def calc_interest_rate(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id].calc_interest_rate()
        else:
            raise ValueError("Client not found.")

    def close_deposit(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id].close_deposit()
        else:
            raise ValueError("Client not found.")


# client_id = "0000001"

bank = Bank()
bank.register_client(client_id="0000001", name="Nick")
bank.open_deposit_account(client_id="0000001", start_balance=1000, years=1)

assert bank.calc_interest_rate(client_id="0000001") == 1104.71, "<Error message>"

final_balance = bank.close_deposit(client_id="0000001")
print(f"Final balance after closing the deposit: {final_balance}")
