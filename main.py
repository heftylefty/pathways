import pandas as pd

def data_capture():
    name = input("who is this for: ")
    streams = int(input("number of revenue streams: "))
    amount = 0
    while streams != 0:

        freq = int(input("How many times per month pay is received: "))
        amount_a = int(input("Amount: "))

        amount += freq * amount_a
        streams -= 1
    test = {name: amount}
    print (test)

data_capture()
