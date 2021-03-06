import pyperclip
import random
import datetime
import time
import ExtractQuotes
import sqlite3
from sqlite3 import Error

positiveQuoteBank = []

def main():
    while (True):
        rng = random.randrange(1, 10)
        rngCodeBankIndex = random.randrange(0,5)
        x = datetime.datetime.now()
        #randomCode = codeBank[rngCodeBankIndex].format(x.strftime("%X"),rng)
        randomCode = niceCompBank[rngCodeBankIndex]
        pyperclip.copy(randomCode)
        pyperclip.paste()
        time.sleep(10)


def testMain():
    database = "C:\SQlite\positiveQuote.db"
    # create a database connection
    conn = ExtractQuotes.create_connection(database)
    rng = 90
    positiveQuoteBank = ExtractQuotes.read_quotes(conn,rng)
    while(True):
        rngCodeBankIndex = random.randrange(0, 50)
        posQuote = positiveQuoteBank[rngCodeBankIndex]
        #print("'{}' - {}".format(posQuote[1],posQuote[0]))
        pyperclip.copy("'{}' - {}".format(posQuote[1],posQuote[0]))
        pyperclip.paste()
        time.sleep(10)



testMain()

#main()
