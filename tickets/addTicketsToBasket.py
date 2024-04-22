
def add_tickets_to_basket(tickets):
    for ticket in tickets:
        for i in range(ticket['increase']): # Click the increase ticket button
            ticket['increaseButton'].click()
        
        for i in range(ticket['decrease']): # Click the decrease ticket button
            ticket['decreaseButton'].click()