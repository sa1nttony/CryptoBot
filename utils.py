import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            ticker_quote = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось найти валюту {quote}')

        try:
            ticker_base = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось найти валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Некорректное значение количества - {amount}')

        if ticker_quote == ticker_base:
            raise ConvertionException(f'Невозможно конфертировать валюту {ticker_quote} в эту же валюту.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={ticker_quote}&tsyms={ticker_base}')
        price = json.loads(r.content)[ticker_base]
        price = price * amount
        return price