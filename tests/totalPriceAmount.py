from selenium.webdriver.remote.webdriver import WebDriver

from tickets.getAllTickets import get_all_tickets
from tickets.addTicketsToBasket import add_tickets_to_basket
from utils import find_element, check_assertion
from random import randint

def run(driver: WebDriver):
    # Arrange
    tickets = get_all_tickets()
    supposedTotalPrice = 0

    for ticket in tickets:
        ticketIncreases = randint(0, 7)
        ticketDecreases = randint(0, 7)
        ticket.update({
            'increase': ticketIncreases,
            'decrease': ticketDecreases,
        })
        
        supposedTotalPrice += ticket['price'] * max((ticketIncreases - ticketDecreases), 0)
    supposedTotalPrice = round(supposedTotalPrice, 2)

    # Act
    add_tickets_to_basket(tickets)
    
    # Assert
    totalPrice = float(find_element('totalText').text[2:].replace(',', '.'))
    check_assertion(totalPrice == supposedTotalPrice,
                    f"Total price is not correct! Expected: {supposedTotalPrice}, got: {totalPrice}")