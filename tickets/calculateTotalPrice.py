from random import randint

def calculateTotalPrice(tickets, minTicketChange: int, maxTicketChange: int):
    expectedTotalPrice = 0
    # Loop over all available tickets and calculate the expected total price
    for ticket in tickets:
        ticketIncreases = randint(minTicketChange, maxTicketChange)
        ticketDecreases = randint(minTicketChange, maxTicketChange - 1)
        ticketTotalPrice = round(ticket['price'] * max((ticketIncreases - ticketDecreases), 0), 2) # Round to 2 decimal places like the actual price

        # Adds how many times the buttons should be clicked for further use
        ticket.update({
            'increase': ticketIncreases,
            'decrease': ticketDecreases,
            'totalPrice': ticketTotalPrice,
        })
        
        expectedTotalPrice += ticketTotalPrice
    return round(expectedTotalPrice, 2)