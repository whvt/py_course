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

    def get_summary(self):
        return {
            "Start Balance": self.start_balance,
            "Current Balance": self.current_balance,
            "Years": self.years,
            "Interest Rate": self.interest_rate,
        }


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}"


class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name)
        else:
            print(f"Client {client_id} is already registered.")

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            if client_id not in self.deposits:
                self.deposits[client_id] = Deposit(start_balance, years)
                print(f"Deposit account opened for Client {client_id}.")
            else:
                print(f"Client {client_id} already has a deposit account.")
        else:
            print(f"Client {client_id} not found. Register the client first.")

    def calc_interest_rate(self, client_id):
        if client_id in self.deposits:
            return self.deposits[client_id].calculate_monthly_compound_interest()
        else:
            raise ValueError("No deposit account found.")

    def close_deposit(self, client_id):
        if client_id in self.deposits:
            final_amount = self.deposits[
                client_id
            ].calculate_monthly_compound_interest()
            del self.deposits[client_id]
            print(
                f"Deposit account for Client {client_id} closed. Final amount: {final_amount}"
            )
            return final_amount
        else:
            raise ValueError("No deposit account found.")

    def show_client_info(self, client_id):
        if client_id in self.clients:
            print(self.clients[client_id])
            if client_id in self.deposits:
                print(self.deposits[client_id].get_summary())
            else:
                print("No deposit account found.")
        else:
            print(f"Client {client_id} not found.")


bank = Bank()

bank.register_client(client_id="0000001", name="Nick")

bank.open_deposit_account("0000001", 1000, 1)


print("Final balance after interest:", bank.calc_interest_rate("0000001"))

bank.show_client_info("0000001")

bank.close_deposit("0000001")