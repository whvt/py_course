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
    def __init__(self, client_id, name, currency="BYN", amount=0):
        self.client_id = client_id
        self.name = name
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return (f"Client ID: {self.client_id},"
                f" Name: {self.name}, "
                f"Currency: {self.currency}, "
                f"Amount: {self.amount}")


class CurrencyConverter:
    def __init__(self, rates):
        # rates: Dictionary with currency conversion rates relative to BYN
        self.rates = rates

    def exchange_currency(self, from_currency, amount, to_currency="BYN"):
        if from_currency not in self.rates:
            raise ValueError(f"Unknown currency: {from_currency}")
        if to_currency not in self.rates:
            raise ValueError(f"Unknown target currency: {to_currency}")

        # Convert from 'from_currency' to 'BYN'
        amount_in_byn = amount * self.rates[from_currency]

        # Convert from 'BYN' to 'to_currency' if required
        if to_currency == "BYN":
            return round(amount_in_byn, 2), "BYN"
        else:
            converted_amount = amount_in_byn / self.rates[to_currency]
            return round(converted_amount, 2), to_currency


class Bank:
    def __init__(self, converter):
        self.clients = {}
        self.deposits = {}
        self.converter = converter

    def convert_client_currency(self, client_id, amount, to_currency="BYN"):
        if client_id in self.clients:
            client = self.clients[client_id]
            return self.converter.exchange_currency(
                client.currency, amount, to_currency
            )
        else:
            raise ValueError(f"Client {client_id} not found.")

    def register_client(self, client_id, name, currency="BYN", amount=0):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name, currency, amount)
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


# Example usage

defined_rates = {"BYN": 1.0, "USD": 3.269, "EUR": 3.52}
converted = CurrencyConverter(defined_rates)

bank = Bank(converted)

# Register a client
bank.register_client(client_id="0000001", name="Nick", currency="USD", amount=10)

# Open a deposit account
bank.open_deposit_account("0000001", 1000, 1)

# Final balance after interest
print("Final balance after interest:", bank.calc_interest_rate("0000001"))

# Show client information
bank.show_client_info("0000001")

# Close deposit
bank.close_deposit("0000001")

# Test cases with currency conversion
vasya = Client(client_id="0000002", name="Vasya", currency="USD", amount=10)
petya = Client(client_id="0000003", name="Petya", currency="EUR", amount=5)

# Conversion to BYN
assert converted.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN"), (
    "Conversion to BYN failed"
)
assert converted.exchange_currency(petya.currency, petya.amount) == (17.6, "BYN"), (
    "Conversion to BYN failed"
)
