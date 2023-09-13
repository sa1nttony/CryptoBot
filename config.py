import os

from dotenv import load_dotenv

os.chdir('../')
os.chdir(os.path.join('environments', 'CryptoBot'))

local_env = os.path.join(os.getcwd(), '.env')

if os.path.exists(local_env):
    load_dotenv(local_env)

TOKEN = os.getenv('TOKEN')

keys = {
    'биткоин': 'BTC',
    'эфир': 'ETH',
    'доллар': 'USD',
    'рубль': 'RUB',
    'евро': 'EUR',
    'тенге': 'KZT',
    'юань': 'CNY',
    'догекоин': 'DOGE',
}

commands = {'/help': 'Узнать о боте',
            '/values': 'Список доступных валют',
            '/convert': 'Начать конвертацию'}