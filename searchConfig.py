searchConfig = {
    'key': {
        'type': 'type',
        'value': 'value',
    },
    'firstChildren': {
        'type': 'XPATH',
        'value': './*',
    },


    'ticketsRow': {
        'type': 'CSS_SELECTOR',
        'value': '.ticket-list__wrapper',
    },
    'increaseTicketAmountButton': {
        'type': 'XPATH',
        'value': './div/div/div[2]/div[2]/div[1]/button[2]',
    },
    'decreaseTicketAmountButton': {
        'type': 'XPATH',
        'value': './div/div/div[2]/div[2]/div[1]/button[1]',
    },
    'ticketPriceText': {
        'type': 'XPATH',
        'value': './div/div/div[2]/div[1]/strong/span',
    },
    'ticketNameText': {
        'type': 'XPATH',
        'value': './div/div/div[1]/div[1]/div[1]/span',
    },
    'totalText': {
        'type': 'CLASS_NAME',
        'value': 'summary-total-cost__test',
    },
}