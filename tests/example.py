from selenium import webdriver
from utils import check_assertion
import unittest

def run(driver: webdriver.Safari):
    check_assertion(driver.title == "Yourticketprovider | Ticketshop", "Title is not correct!")