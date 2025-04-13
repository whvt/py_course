*** Settings ***
Library    ../hw13_bank.py
Library    Collections
Library    BuiltIn

*** Variables ***
${START_BALANCE}    1000
${YEARS}    1
${INTEREST_RATE}    0.10
${CONVERSION_RATES}    {"BYN": 1.0, "USD": 3.269, "EUR": 3.52}

*** Keywords ***
Initialize Currency Converter
    ${converter}=    Evaluate    CurrencyConverter(${CONVERSION_RATES})
    RETURN   ${converter}

Initialize Bank
    ${converter}=    Initialize Currency Converter
    ${bank}=    Evaluate    Bank(${converter})
    RETURN   ${bank}

Register Client
    [Arguments]    ${bank}    ${client_id}    ${name}    ${currency}    ${amount}
    ${none}=    Evaluate    ${bank}.register_client(${client_id}, ${name}, currency=${currency}, amount=${amount})
    Log    Client ${client_id} registered successfully.

Open Deposit Account
    [Arguments]    ${bank}    ${client_id}    ${start_balance}    ${years}
    ${none}=    Evaluate    ${bank}.open_deposit_account(${client_id}, ${start_balance}, ${years})
    Log    Deposit account opened for Client ${client_id}.

Calculate Compound Interest
    [Arguments]    ${bank}    ${client_id}
    ${interest}=    Evaluate    ${bank}.calc_interest_rate(${client_id})
    Log    Calculated compound interest: ${interest}
    RETURN   ${interest}

Close Deposit Account
    [Arguments]    ${bank}    ${client_id}
    ${final_amount}=    Evaluate    ${bank}.close_deposit(${client_id})
    Log    Deposit account closed for Client ${client_id}. Final Amount: ${final_amount}
    RETURN   ${final_amount}

Currency Conversion
    [Arguments]    ${bank}    ${client_id}    ${amount}    ${to_currency}
    ${converted}=    Evaluate    ${bank}.convert_client_currency(${client_id}, ${amount}, ${to_currency})
    Log    Converted ${amount} to ${to_currency}: ${converted}
    RETURN   ${converted}

*** Test Cases ***
Test Register Client and Open Deposit
    ${bank}=    Initialize Bank
    Register Client    ${bank}    0000001    Nick    USD    10
    Open Deposit Account    ${bank}    0000001    ${START_BALANCE}    ${YEARS}

Test Calculate Interest and Close Deposit
    ${bank}=    Initialize Bank
    Register Client    ${bank}    0000001    Nick    USD    10
    Open Deposit Account    ${bank}    0000001    ${START_BALANCE}    ${YEARS}
    ${interest}=    Calculate Compound Interest    ${bank}    0000001
    Should Be Equal As Numbers    ${interest}    1030.42
    ${final_amount}=    Close Deposit Account    ${bank}    0000001
    Should Be Equal As Numbers    ${final_amount}    1030.42

Test Currency Conversion
    ${bank}=    Initialize Bank
    Register Client    ${bank}    0000002    Vasya    USD    10
    ${converted}=    Currency Conversion    ${bank}    0000002    10    BYN
    Should Be Equal    ${converted}    [32.69, BYN]
