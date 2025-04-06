import unittest
from hw13_bank import Deposit, Client, CurrencyConverter, Bank


class TestDeposit(unittest.TestCase):
    def test_calculate_monthly_compound_interest(self):
        deposit = Deposit(start_balance=1000, years=2, interest_rate=0.1)
        result = deposit.calculate_monthly_compound_interest()
        self.assertAlmostEqual(result, 1220.39, places=2)

    def test_get_summary(self):
        deposit = Deposit(start_balance=500, years=1, interest_rate=0.1)
        deposit.calculate_monthly_compound_interest()
        summary = deposit.get_summary()
        self.assertEqual(summary["Start Balance"], 500)
        self.assertEqual(summary["Years"], 1)
        self.assertAlmostEqual(summary["Current Balance"], 552.356, places=2)
        self.assertEqual(summary["Interest Rate"], 0.1)


class TestClient(unittest.TestCase):
    def test_client_initialization(self):
        client = Client(client_id=1, name="Ivan", currency="USD", amount=1000)
        self.assertEqual(client.client_id, 1)
        self.assertEqual(client.name, "Ivan")
        self.assertEqual(client.currency, "USD")
        self.assertEqual(client.amount, 1000)
        self.assertEqual(str(client), "Client ID: 1, Name: Ivan, Currency: USD, Amount: 1000")


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter(rates={"USD": 2.5, "EUR": 2.8, "BYN": 1})

    def test_exchange_to_byn(self):
        amount, currency = self.converter.exchange_currency("USD", 100)
        self.assertEqual(amount, 250.0)
        self.assertEqual(currency, "BYN")

    def test_exchange_from_byn_to_eur(self):
        amount, currency = self.converter.exchange_currency("BYN", 280, "EUR")
        self.assertEqual(amount, 100.0)
        self.assertEqual(currency, "EUR")

    def test_unknown_currency(self):
        with self.assertRaises(ValueError):
            self.converter.exchange_currency("GBP", 100)

        with self.assertRaises(ValueError):
            self.converter.exchange_currency("USD", 100, "JPY")


class TestBank(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter(rates={"USD": 2.5, "EUR": 2.8, "BYN": 1})
        self.bank = Bank(self.converter)
        self.bank.register_client(1, "Ivan", currency="USD", amount=1000)

    def test_register_client(self):
        self.assertIn(1, self.bank.clients)
        self.assertEqual(self.bank.clients[1].name, "Ivan")
        self.assertEqual(self.bank.clients[1].currency, "USD")
        self.assertEqual(self.bank.clients[1].amount, 1000)

    def test_open_deposit_account(self):
        self.bank.open_deposit_account(1, 1000, 2)
        self.assertIn(1, self.bank.deposits)
        self.assertEqual(self.bank.deposits[1].start_balance, 1000)
        self.assertEqual(self.bank.deposits[1].years, 2)

    def test_calc_interest_rate(self):
        self.bank.open_deposit_account(1, 1000, 2)
        final_balance = self.bank.calc_interest_rate(1)
        self.assertAlmostEqual(final_balance, 1220.391, places=2)

    def test_close_deposit(self):
        self.bank.open_deposit_account(1, 1000, 2)
        final_amount = self.bank.close_deposit(1)
        self.assertAlmostEqual(final_amount, 1220.391, places=2)
        self.assertNotIn(1, self.bank.deposits)

    def test_convert_client_currency(self):
        amount, currency = self.bank.convert_client_currency(1, 1000, "EUR")
        self.assertEqual(amount, 892.86)
        self.assertEqual(currency, "EUR")


if __name__ == "__main__":
    unittest.main()
