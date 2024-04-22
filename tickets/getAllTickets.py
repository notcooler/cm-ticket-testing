from utils.elementSearcher import find_element, find_elements

def get_all_tickets():
    parentElement = find_element('ticketsRow')
    ticketElements = find_elements('firstChildren', parentElement)
    tickets = []

    for ticketElement in ticketElements:
        priceTextElement = find_element('ticketPriceText', ticketElement)
        nameTextElement = find_element('ticketNameText', ticketElement)
        price = float(priceTextElement.text[2:].replace(',', '.'))
        if int(price) != 0: # Checks if service fee is needed
            price += 0.85

        tickets.append({
            'name': nameTextElement.text,
            'price': price,

            'increaseButton': find_element('increaseTicketAmountButton', ticketElement),
            'decreaseButton': find_element('decreaseTicketAmountButton', ticketElement),
        })
    
    return tickets