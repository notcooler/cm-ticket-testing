from selenium.webdriver.remote.webdriver import WebDriver
from random import randint

from tickets.getAllTickets import get_all_tickets
from tickets.addTicketsToBasket import add_tickets_to_basket
from utils.elementSearcher import find_element
from utils.assertion import assert_equal

config = {
    'serviceFee': 0.85,
    'minTicketChange': 0,
    'maxTicketChange': 7,
}

def run(driver: WebDriver):
    # Arrange

    # Finds all tickets and fetches their increase and decrease buttons, name and price.
    # Check the get_all_tickets function to understand how find_element(s) functions work!!!
    tickets = get_all_tickets(serviceFee=config['serviceFee'])
    expectedTotalPrice = 0

    # Loop over all available tickets and calculate the expected total price
    for ticket in tickets:
        ticketIncreases = randint(config['minTicketChange'], config['maxTicketChange'])
        ticketDecreases = randint(config['minTicketChange'], config['maxTicketChange'])

        # Adds how many times the buttons should be clicked for further use
        ticket.update({
            'increase': ticketIncreases,
            'decrease': ticketDecreases,
        })
        
        expectedTotalPrice += ticket['price'] * max((ticketIncreases - ticketDecreases), 0)
    expectedTotalPrice = round(expectedTotalPrice, 2)

    # Act
    # Clicks the increase and decrease buttons for all tickets on their respective amounts specified above
    add_tickets_to_basket(tickets)
    
    # Assert
    actualPrice = float(find_element('totalText').text[2:].replace(',', '.'))
    assert_equal(expectedTotalPrice, actualPrice,
                    f"Total price is not correct! Expected: {expectedTotalPrice}, got: {actualPrice}")