#!/usr/bin/env python

from __future__ import print_function
from colorclass import Color, Windows
from terminaltables import SingleTable
import requests
import argparse
import json
import time

parser = argparse.ArgumentParser(description="MINING\nPOOL\nHUB\nInformation Gatherer")
parser.add_argument('-a', metavar='api_key', required=True, help='API KEY from \'Edit Account\' page')
parser.add_argument('-i', metavar='id', help='USER ID from \'Edit Account\' page')
parser.add_argument('-c', metavar='currency', default='btc', help='Which exchange currency to display total in (default btc)')
parser.add_argument('-f', metavar='fiat_currency', default='usd', help='Which fiat currency to display total in')
args = parser.parse_args()

class MphInfo:
    def __init__(self, api_key, id, currency, fiat_currency):
        Windows.enable(auto_colors=True, reset_atexit=True)  # For just Windows
        self.key_     = api_key
        self.id_      = id
        self.cur_     = currency
        self.fcur_    = fiat_currency
        self.symbols_ = {}
        self.setSymbols()

        # Print Balances
        self.printBalances()

    def getJson(self, method, coin=False, id=False):
        if coin == False and id == False:
            url="https://{}miningpoolhub.com/index.php?page=api&action={}&api_key={}&id={}".format("", method, self.key_, "")
            raw_response = requests.get(url).text
            response = json.loads(raw_response)
            return response

    def getValueInOurCoin(self, symbol, amount, compare=args.c):
        if symbol.upper() == compare.upper():
            return amount
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(symbol.lower(), compare.lower())
        raw_response = requests.get(url).text
        response = json.loads(raw_response)
        price = response["ticker"]["price"]
        value = float(price) * float(amount)
        return value


    def printBalances(self):

        response = self.getJson("getuserallbalances")

        coins = {}
        for coin in response["getuserallbalances"]["data"]:
            symbol = self.symbols_[coin["coin"]]
            balance = sum([
              coin["confirmed"],
              coin["unconfirmed"],
              coin["ae_confirmed"],
              coin["ae_unconfirmed"],
              coin["exchange"]
             ])
            coins[symbol] = balance

        dummybtc = 0.99999999
        dummyusd = 998.88888888

        table_data = [
            [Color('{autoyellow}Total Balance{/autoyellow}\n{autocyan}' + str(dummybtc) + '{/autocyan} BTC\n{autogreen}' + str(dummyusd) + '{/autogreen} USD'),
             Color('{autoyellow}Wallet{/autoyellow}\n{autoyellow}Total{/autoyellow}\n{autoyellow}Value{/autoyellow}'),
             Color('{autoyellow}Total{/autoyellow}\n{autoyellow}USD{/autoyellow}\n{autoyellow}Value{/autoyellow}'),
             Color('{autoyellow}Exchange{/autoyellow}\n{autoyellow}Total{/autoyellow}\n{autoyellow}Value{/autoyellow}'),
            ], # Title


            [Color('{autocyan}Bitcoin{/autocyan}'),        Color( str(dummybtc)), Color('{autogreen}' + str(dummyusd) + '{/autogreen}'), Color('{autored}' + str(dummybtc) + '{/autored}')],
            [Color('{autocyan}Zcash{/autocyan}'),          Color( str(dummybtc)), Color('{autogreen}' + str(dummyusd) + '{/autogreen}'), Color('{autored}' + str(dummybtc) + '{/autored}')],
            [Color('{autocyan}Digibyte-Skein{/autocyan}'), Color( str(dummybtc)), Color('{autogreen}' + str(dummyusd) + '{/autogreen}'), Color('{autored}' + str(dummybtc) + '{/autored}')],
            [Color('{autocyan}Zclassic{/autocyan}'),       Color( str(dummybtc)), Color('{autogreen}' + str(dummyusd) + '{/autogreen}'), Color('{autored}' + str(dummybtc) + '{/autored}')],
        ]
        table_instance = SingleTable(table_data)
        table_instance.inner_heading_row_border = False
        table_instance.inner_row_border = True
        table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
        print (table_instance.table)

    # I just don't wanna see this lazy code in constructor lol
    def setSymbols(self):
        self.symbols_ = {
            "adzcoin": "ADZ",
            "auroracoin": "AUR",
            "bitcoin": "BTC",
            "bitcoin-cash": "BCH",
            "bitcoin-gold": "BTG",
            "dash": "DSH",
            "digibyte": "DGB",
            "digibyte-groestl": "DGB",
            "digibyte-skein": "DGB",
            "digibyte-qubit": "DGB",
            "ethereum": "ETH",
            "ethereum-classic": "ETC",
            "expanse": "EXP",
            "feathercoin": "FTC",
            "gamecredits": "GAME",
            "geocoin": "GEO",
            "globalboosty": "BSTY",
            "groestlcoin": "GRS",
            "litecoin": "LTC",
            "maxcoin": "MAX",
            "monacoin": "MONA",
            "monero": "XMR",
            "musicoin": "MUSIC",
            "myriadcoin": "XMY",
            "myriadcoin-skein": "XMY",
            "myriadcoin-groestl": "XMY",
            "myriadcoin-yescrypt": "XMY",
            "sexcoin": "SXC",
            "siacoin": "SC",
            "startcoin": "START",
            "verge": "XVG",
            "vertcoin": "VTC",
            "zcash": "ZEC",
            "zclassic": "ZCL",
            "zcoin": "XZC",
            "zencash": "ZEN"
        }

def main():
    m = MphInfo(args.a, args.i, args.c, args.f)

if __name__ == '__main__':
    main()
