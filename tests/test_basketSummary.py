import time
from utils.setup import setupTest

from tickets.getAllTickets import getAllTickets
from tickets.addTicketsToBasket import addTicketsToBasket
from tickets.calculateTotalPrice import calculateTotalPrice
from utils.elementSearcher import findElement, findElements
import logging

testConfig = {
    'serviceFee': 0.85,
    'minTicketChange': 0,
    'maxTicketChange': 7,
}

logger = logging.getLogger(__name__)

# Checks if the summary is correct
def test_run(isLocal):
    driver, config = setupTest(isLocal)

    tickets = getAllTickets(driver, serviceFee=testConfig['serviceFee'])
    calculateTotalPrice(tickets, testConfig['minTicketChange'], testConfig['maxTicketChange'])

    addTicketsToBasket(tickets)

    # Get summary parent
    basketSummary = findElement('summaryItems', driver)
    summaryItems = findElements('summaryItem', basketSummary)

    ticketsSorted = [x for x in tickets if x['increase'] - x['decrease'] > 0] # Only get tickets that are supposed to be in the summary

    # Loop over all tickets and check if summary is correct
    for i in range(len(ticketsSorted)):
        # Get the summary item
        summaryItem = summaryItems[i]
        # Get the name and price from the summary item
        summaryName = findElement('summaryName', summaryItem).text
        summaryPrice = float(findElement('summaryPrice', summaryItem).text[2:].replace(',', '.'))

        # Check if the summary item is correct
        assert summaryName == ticketsSorted[i]['name']
        assert summaryPrice == ticketsSorted[i]['totalPrice']