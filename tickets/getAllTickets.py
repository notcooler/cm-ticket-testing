from utils.elementSearcher import findElement, findElements

# This function is used to get all avaiable tickets from the page and fetch their data
def getAllTickets(driver, serviceFee: float = None):
    parentElement = findElement('ticketsRow', driver) # Gets the element/div where all the tickets are located
    # Second specified element is the parent, it now searches from the perspective of the parent
    ticketElements = findElements('firstChildren', parentElement)
    tickets = []

    for ticketElement in ticketElements:
        priceTextElement = findElement('ticketPriceText', ticketElement)
        nameTextElement = findElement('ticketNameText', ticketElement)
        price = float(priceTextElement.text[2:].replace(',', '.'))
        
        if serviceFee is not None: # Checks if we should check service fee
            if int(price) != 0: # Checks if service fee is needed
                price += serviceFee

        tickets.append({
            'name': nameTextElement.text,
            'price': price,

            'increaseButton': findElement('increaseTicketAmountButton', ticketElement),
            'decreaseButton': findElement('decreaseTicketAmountButton', ticketElement),
        })
    
    return tickets