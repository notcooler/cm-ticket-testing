from selenium import webdriver

def run(driver: webdriver.Safari):
    if driver.title == "Yourticketprovider | Ticketshop":
        return True
    
    return False