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


from huobi.utils import LogInfo

# 自己的火币账户的access_key, secret_key 火币每个主账号能创建200个子账号，尽
# 量使用子账号操作,防范风险. 切不能向任何人公开你的secret_key以确保账户安全
ACCESS_KEY = 'eca33195-b76d0c49-940b00d7-mn8ikls4qg'
SECRET_KEY = '128b5bc0-9c05462a-22c9646b-e7c34'


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
