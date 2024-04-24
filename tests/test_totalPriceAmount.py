from utils.setup import setupTest

from tickets.getAllTickets import getAllTickets
from tickets.addTicketsToBasket import addTicketsToBasket
from tickets.calculateTotalPrice import calculateTotalPrice
from utils.elementSearcher import findElement

testConfig = {
    'serviceFee': 0.85,
    'minTicketChange': 0,
    'maxTicketChange': 7,
}

def test_run(isLocal):
    driver, config = setupTest(isLocal)
    # Arrange

    # Finds all tickets and fetches their increase and decrease buttons, name and price.
    # Check the get_all_tickets function to understand how find_element(s) functions work!!!
    tickets = getAllTickets(driver, serviceFee=testConfig['serviceFee'])

    # Calculates the expected total price based on the tickets and the min/max ticket change
    expectedTotalPrice = calculateTotalPrice(tickets, testConfig['minTicketChange'], testConfig['maxTicketChange'])

    # Act
    # Clicks the increase and decrease buttons for all tickets on their respective amounts specified above
    addTicketsToBasket(tickets)
    
    # Assert
    actualPrice = float(findElement('totalText', driver).text[2:].replace(',', '.'))
    assert expectedTotalPrice == actualPrice, f"Total price is not correct! Expected: {expectedTotalPrice}, got: {actualPrice}"