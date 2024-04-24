from random import randint
from utils.setup import setupTest

from tickets.getAllTickets import getAllTickets
from tickets.addTicketsToBasket import addTicketsToBasket
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
    expectedTotalPrice = 0

    # Loop over all available tickets and calculate the expected total price
    for ticket in tickets:
        ticketIncreases = randint(testConfig['minTicketChange'], testConfig['maxTicketChange'])
        ticketDecreases = randint(testConfig['minTicketChange'], testConfig['maxTicketChange'])

        # Adds how many times the buttons should be clicked for further use
        ticket.update({
            'increase': ticketIncreases,
            'decrease': ticketDecreases,
        })
        
        expectedTotalPrice += ticket['price'] * max((ticketIncreases - ticketDecreases), 0)
    expectedTotalPrice = round(expectedTotalPrice, 2) # Round to 2 decimal places like the actual price

    # Act
    # Clicks the increase and decrease buttons for all tickets on their respective amounts specified above
    addTicketsToBasket(tickets)
    
    # Assert
    actualPrice = float(findElement('totalText', driver).text[2:].replace(',', '.'))
    assert expectedTotalPrice == actualPrice, f"Total price is not correct! Expected: {expectedTotalPrice}, got: {actualPrice}"