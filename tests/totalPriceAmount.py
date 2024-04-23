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
    tickets = get_all_tickets(serviceFee=config['serviceFee'])
    supposedTotalPrice = 0

    for ticket in tickets:
        ticketIncreases = randint(config['minTicketChange'], config['maxTicketChange'])
        ticketDecreases = randint(config['minTicketChange'], config['maxTicketChange'])
        ticket.update({
            'increase': ticketIncreases,
            'decrease': ticketDecreases,
        })
        
        supposedTotalPrice += ticket['price'] * max((ticketIncreases - ticketDecreases), 0)
    supposedTotalPrice = round(supposedTotalPrice, 2)

    # Act
    add_tickets_to_basket(tickets)
    
    # Assert
    actualPrice = float(find_element('totalText').text[2:].replace(',', '.'))
    assert_equal(supposedTotalPrice, actualPrice,
                    f"Total price is not correct! Expected: {supposedTotalPrice}, got: {actualPrice}")