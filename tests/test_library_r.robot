*** Settings ***
Library    ../library.py
Library    Collections
Library    BuiltIn

*** Variables ***
${BOOK_NAME}    The Hobbit
${AUTHOR}       J.R.R. Tolkien
${NUM_PAGES}    400
${ISBN}         1236754023
${READER_NAME}  Nick
*** Keywords ***
Create Book
    [Arguments]    ${book_name}    ${author}    ${num_pages}    ${isbn}
    ${book}=    Evaluate    library.Book("${book_name}", "${author}", ${num_pages}, "${isbn}")
    RETURN    ${book}
    
Create Reader
    [Arguments]    ${name}
    ${reader}=    Evaluate    library.Reader("${name}")
    RETURN    ${reader}
    
Reserve Book
    [Arguments]    ${reader}    ${book}
    ${reserved}=    Evaluate    reserve_book(${book}, ${reader})
    Log    Reserve result: ${reserved}

Cancel Reservation
    [Arguments]    ${reader}    ${book}
    ${canceled}=    Evaluate    cancel_reserve(${book}, ${reader})
    Log    Cancel reserve result: ${canceled}

Check Out Book
    [Arguments]    ${reader}    ${book}
    ${checked_out}=    Evaluate    get_book(${book}, ${reader})
    Log    Checkout result: ${checked_out}

Return Book
    [Arguments]    ${reader}    ${book}
    ${returned}=    Evaluate    return_book(${book}, ${reader})
    Log    Return result: ${returned}

*** Test Cases ***
Test Reserve Book
    ${book}=    Create Book    The Hobbit    J.R.R. Tolkien    400    1236754023
    ${reader}=    Create Reader    Nick
    Reserve Book    ${reader}    ${book}
    Should Not Be Empty    ${book.reserved_by}
    Should Be Equal    ${book.reserved_by.name}    Nick
Test Cancel Reservation
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    Reserve Book    ${reader}    ${book}
    Cancel Reservation    ${reader}    ${book}
    Should Be Empty    ${book.reserved_by}

Test Check Out Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    Reserve Book    ${reader}    ${book}
    Check Out Book    ${reader}    ${book}
    Should Not Be Empty    ${book.checked_out_by}
    Should Be Empty    ${book.reserved_by}

Test Return Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    Reserve Book    ${reader}    ${book}
    Check Out Book    ${reader}    ${book}
    Return Book    ${reader}    ${book}
    Should Be Empty    ${book.checked_out_by}
