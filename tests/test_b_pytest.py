import pytest
import logging
from hw13_bank import Deposit, Client, CurrencyConverter, Bank

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@pytest.fixture
def currency_converter():
    return CurrencyConverter(rates={"USD": 2.5, "EUR": 2.8, "BYN": 1})


@pytest.fixture
def bank(currency_converter):
    bank_instance = Bank(currency_converter)
    bank_instance.register_client(1, "Ivan", currency="USD", amount=1000)
    return bank_instance


def test_calculate_monthly_compound_interest():
    deposit = Deposit(start_balance=1000, years=2, interest_rate=0.1)
    result = deposit.calculate_monthly_compound_interest()
    logger.info(f"Calculated compound interest: {result}")
    assert pytest.approx(result, rel=1e-2) == 1220.39


def test_get_summary():
    deposit = Deposit(start_balance=500, years=1, interest_rate=0.1)
    deposit.calculate_monthly_compound_interest()
    summary = deposit.get_summary()
    logger.info(f"Deposit summary: {summary}")
    assert summary["Start Balance"] == 500
    assert summary["Years"] == 1
    assert pytest.approx(summary["Current Balance"], rel=1e-2) == 552.356
    assert summary["Interest Rate"] == 0.1


def test_client_initialization():
    client = Client(client_id=1, name="Ivan", currency="USD", amount=1000)
    logger.info(f"Initialized client: {client}")
    assert client.client_id == 1
    assert client.name == "Ivan"
    assert client.currency == "USD"
    assert client.amount == 1000
    assert str(client) == "Client ID: 1, Name: Ivan, Currency: USD, Amount: 1000"


def test_exchange_to_byn(currency_converter):
    amount, currency = currency_converter.exchange_currency("USD", 100)
    logger.info(f"Exchanged currency to BYN: {amount} {currency}")
    assert amount == 250.0
    assert currency == "BYN"


def test_exchange_from_byn_to_eur(currency_converter):
    amount, currency = currency_converter.exchange_currency("BYN",
                                                            280, "EUR")
    logger.info(f"Exchanged currency from BYN to EUR: {amount} {currency}")
    assert amount == 100.0
    assert currency == "EUR"


def test_unknown_currency(currency_converter):
    with pytest.raises(ValueError):
        logger.info("Testing exchange with unknown currency: GBP")
        currency_converter.exchange_currency("GBP", 100)
    with pytest.raises(ValueError):
        logger.info("Testing exchange with unknown currency: JPY")
        currency_converter.exchange_currency("USD", 100, "JPY")


def test_register_client(bank):
    logger.info(f"Registering client: {bank.clients[1]}")
    assert 1 in bank.clients
    assert bank.clients[1].name == "Ivan"
    assert bank.clients[1].currency == "USD"
    assert bank.clients[1].amount == 1000


def test_open_deposit_account(bank):
    bank.open_deposit_account(1, 1000, 2)
    logger.info(f"Opened deposit account for client 1: {bank.deposits[1]}")
    assert 1 in bank.deposits
    assert bank.deposits[1].start_balance == 1000
    assert bank.deposits[1].years == 2


def test_calc_interest_rate(bank):
    bank.open_deposit_account(1, 1000, 2)
    final_balance = bank.calc_interest_rate(1)
    logger.info(f"Calculated interest rate for client 1: {final_balance}")
    assert pytest.approx(final_balance, rel=1e-2) == 1220.391


def test_close_deposit(bank):
    bank.open_deposit_account(1, 1000, 2)
    final_amount = bank.close_deposit(1)
    logger.info(f"Closed deposit account for client 1. Final amount: {final_amount}")
    assert pytest.approx(final_amount, rel=1e-2) == 1220.391
    assert 1 not in bank.deposits


def test_convert_client_currency(bank):
    amount, currency = bank.convert_client_currency(1, 1000, "EUR")
    logger.info(f"Converted client currency to EUR: {amount} {currency}")
    assert pytest.approx(amount, rel=1e-2) == 892.86
    assert currency == "EUR"
