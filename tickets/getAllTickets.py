from utils.elementSearcher import find_element, find_elements

# This function is used to get all avaiable tickets from the page and fetch their data
def get_all_tickets(serviceFee: float = None):
    parentElement = find_element('ticketsRow') # Gets the element/div where all the tickets are located
    # Second specified element is the parent, it now searches from the perspective of the parent
    ticketElements = find_elements('firstChildren', parentElement)
    tickets = []

    for ticketElement in ticketElements:
        priceTextElement = find_element('ticketPriceText', ticketElement)
        nameTextElement = find_element('ticketNameText', ticketElement)
        price = float(priceTextElement.text[2:].replace(',', '.'))
        
        if serviceFee is not None: # Checks if we should check service fee
            if int(price) != 0: # Checks if service fee is needed
                price += serviceFee

        tickets.append({
            'name': nameTextElement.text,
            'price': price,

            'increaseButton': find_element('increaseTicketAmountButton', ticketElement),
            'decreaseButton': find_element('decreaseTicketAmountButton', ticketElement),
        })
    
    return tickets