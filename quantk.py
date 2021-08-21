# public
from huobi.client.generic import GenericClient
from huobi.client.market import MarketClient
# private
from huobi.client.account import AccountClient
from huobi.client.margin import MarginClient
from huobi.client.algo import AlgoClient
from huobi.client.etf import EtfClient
from huobi.client.subuser import SubuserClient
from huobi.client.trade import TradeClient
from huobi.client.wallet import WalletClient

from huobi.constant import *
from huobi.utils import *


# 创建实例
generic_client = GenericClient()
market_client = MarketClient()

account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
algo_client = AlgoClient(api_key=g_api_key, secret_key=g_secret_key)
etf_client = EtfClient(api_key=g_api_key, secret_key=g_secret_key)
subuser_client = SubuserClient(api_key=g_api_key, secret_key=g_secret_key)
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
