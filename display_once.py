#!/usr/bin/env python

from __future__ import print_function

import time

from colorclass import Color, Windows
from terminaltables import SingleTable
import argparse
import requests
import sys

parser = argparse.ArgumentParser(description="MINING\nPOOL\nHUB\nInformation Gatherer")
parser.add_argument('-a', metavar='api_key', required=True, help='API KEY from \'Edit Account\' page')
parser.add_argument('-i', metavar='id', help='USER ID from \'Edit Account\' page')
parser.add_argument('-c', metavar='crypto_currency', default='BTC', help='Which exchange currency to display total in (default BTC)')
parser.add_argument('-f', metavar='fiat_currency', help=' Not needed, extra column for displaying other fiat currency total')
args = parser.parse_args()

class MphInfo:
    def __init__(self, api_key, id, currency, fiat_currency):
        Windows.enable(auto_colors=True, reset_atexit=True)  # For just Windows
        self.key_     = api_key
        self.id_      = id
        self.cur_     = currency
        self.fcur_    = fiat_currency
        self.crypto_symbols_ = {}
        self.setSymbols()

        self.other_cur = False
        if args.f != None:
            self.other_cur = True

        self.balances_table_ = SingleTable([])

        # Print Balances
        self.getBalances()
        self.printBalances()


    def printBalances(self):
        print()
        print(self.balances_table_.table)

    def getMphJsonDict(self, method, coin=False, id=False):
        if coin == False and id == False:
            url="https://{}miningpoolhub.com/index.php?page=api&action={}&api_key={}&id={}".format("", method, self.key_, "")
            response = requests.get(url, timeout=10)
            json_dict = response.json()
            return json_dict #response

    def getValueInOtherCurrency(self, curency, amount, other_currency, use_dot=None):
        if curency.upper() == other_currency.upper(): # No need to convert
            return amount
        url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(curency.upper(), other_currency.upper())
        response = requests.get(url, timeout=10)
        json_dict = response.json()
        price = json_dict[other_currency.upper()]
        value = float(price) * float(amount)
        if use_dot != None:
            self.printDotInfo()
        return value

    def printDotInfo(self, info=None):
        if info == None:
            sys.stdout.write('.')
            sys.stdout.flush()
        else:
            sys.stdout.write(info)
            sys.stdout.flush()

    def getBalances(self):

        self.printDotInfo('Getting values and converting to other currencies...')

        sign = ""
        if self.other_cur:
            if self.fcur_ == 'TRY':
                sign = '₺'
            elif self.fcur_ == 'EUR':
                sign = '€'
            if self.fcur_ == 'AZN':
                sign = '₼'
            elif self.fcur_ == 'GBP':
                sign = '£'
            elif self.fcur_ == 'CNY' or self.fcur_ == 'JPY' :
                sign = '¥'
            elif self.fcur_ == 'AUD':
                sign = '$'
            elif self.fcur_ == 'ALL':
                sign = 'L'

        if self.cur_ == 'BTC':
            fave_crypto_sign = 'Ƀ'
        elif self.cur_ == 'ETH':
            fave_crypto_sign = '⧫'
        else:
            fave_crypto_sign = self.cur_


        json_dict = self.getMphJsonDict("getuserallbalances")

        coins = {}

        total_fave_crypto = 0.0

        for coin in json_dict["getuserallbalances"]["data"]:
            symbol = self.crypto_symbols_[coin["coin"]]
            balance = sum([
              coin["confirmed"],
              coin["unconfirmed"]
             ])
            balance_ex = sum([
              coin["ae_confirmed"],
              coin["ae_unconfirmed"],
              coin["exchange"]
             ])
            coins[symbol + "_balance"] = balance
            coins[symbol + "_exchange"] = balance_ex
            coin_total_balance = balance + balance_ex

            total_fave_crypto += self.getValueInOtherCurrency(symbol, coin_total_balance, self.cur_, True)
            coins[symbol + "_fiat_usd"] = self.getValueInOtherCurrency(symbol, balance, 'USD', True)
            if self.other_cur:
                coins[symbol + "_fiat_my_cur"] = self.getValueInOtherCurrency(symbol, balance, self.fcur_, True)


        total_usd = self.getValueInOtherCurrency(self.cur_, total_fave_crypto, 'USD', True)
        total_fiat = self.getValueInOtherCurrency(self.cur_, total_fave_crypto, self.fcur_, True)
        table_data = []

        title =[Color('{autoyellow}Total Balance{/autoyellow}\n'+ fave_crypto_sign +'{autocyan}' + str("%.6f" % total_fave_crypto) + '{/autocyan}'),
                Color('{autoyellow}Confirmed+{/autoyellow}\n{autoyellow}Unconfirmed{/autoyellow}'),
                Color('{autoyellow}Exchange+{/autoyellow}\n{autoyellow}AE_All{/autoyellow}'),
                Color('{autoyellow}Total{/autoyellow}\n${autocyan}' + str("%.2f" % total_usd) + '{/autocyan}'),
             ]

        if self.other_cur:
            title.append(Color('{autoyellow}Total{/autoyellow}\n' + sign + '{autocyan}' + str("%.2f" % total_fiat) + '{/autocyan}'),)

        table_data.append(title)

        for coin in json_dict["getuserallbalances"]["data"]:
            symbol = self.crypto_symbols_[coin["coin"]]

            coin_line = [
                    Color('{autocyan}' + coin["coin"].title() + '{/autocyan}'),
                    Color( str("%.9f" % coins[symbol + '_balance'])),
                    Color('{autored}' + str("%.6f" % coins[symbol + '_exchange']) + '{/autored}'),
                    Color('${autogreen}' + str("%.2f" % coins[symbol + '_fiat_usd']) + '{/autogreen}'),
                ]

            if self.other_cur:
                coin_line.append(Color(sign + '{autogreen}' + str("%.2f" % coins[symbol + '_fiat_my_cur']) + '{/autogreen}'))

            table_data.append(coin_line)

        self.balances_table_ = SingleTable(table_data)
        self.balances_table_.inner_heading_row_border = False
        self.balances_table_.inner_row_border = True
        self.balances_table_.justify_columns = {0: 'center', 1: 'center', 2: 'center'}

    # I just don't wanna see this lazy code in constructor lol
    def setSymbols(self):
        self.crypto_symbols_ = {
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
