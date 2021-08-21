# QuantK Huobi Python

This is a personal Huobi Python trade app repository, modified from the Huobi Python SDK and the original is:
https://github.com/HuobiRDCenter/huobi_Python.

Therefore, you'll find that all the request methods in the APP come from the official SDK. Based on these tool functions, we can implement our trading strategy conveniently.

## Quick Start

*The APP is compiled by Python 3.7 and above*

You can download and open the source code directly in your python project, and then you can follow below steps:

* Create the client instance such as the `quantk.py` file did.
* Call the interfaces provided by client.

```python
# Create generic client instance and get the timestamp
generic_client = GenericClient()
timestamp = generic_client.get_exchange_timestamp()
print(timestamp)

# Create the market client instance and get the latest btcusdt‘s candlestick
market_client = MarketClient()
list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 10)
LogInfo.output_list(list_obj)
```

## Usage

After above section, this APP should be already download to your local machine, this section introduce the HuoBi Python SDK and how to use it correctly.

The Official Huobi API document may help you to use this SDK: https://huobiapi.github.io/docs/spot/v1/en/#introduction

### File & Folder structure

This is the folder and package structure of SDK source code and the description

- **huobi**: The core of the SDK
  - **client**: The client that are responsible to access data, this is the external interface layer.
  - **connection**: Responsible to manage the remote server connection
  - **constant**: The constant configuration
  - **exception**: The wrapped exception
  - **model**: The server returned data model
  - **service**: The internal implementation for each **client**.
  - **utils**:The utility classes, including signature, json parser, logging etc.
- **performance**: This is for internal performance testing
- **tests**: This is for internal functional testing
- **example**: The main package is defined here, it provides the examples how to use **client** instance to access API and read response.
- **quantk.py**: The entry for custom use of the SDK, code your trade strategy here.
### Run examples

This SDK provides examples that under **/example** folder, if you want to run the examples to access private data, you need below additional steps:

1. Create an **API Key** first from Huobi official website
2. Create **privateconfig.py** into your **huobi** folder. The purpose of this file is to prevent submitting SecretKey into repository by accident, so this file is already added in the *.gitignore* file. 
3. Assign your API access key and secret key to `./huobi/constant/test.py` as below:
```python
p_api_key = "hrf5gdfghe-e74bebd8-2f4a33bc-e7963"
p_secret_key = "fecbaab2-35befe7e-2ea695e8-67e56"
```

If you don't need to access private data, you can ignore the API key.

Regarding the difference between public data and private data you can find details in [Client](#Client) section below.

### Client

In the HuoBi Python SDK, the client is the struct to access the Huobi API. In order to isolate the private data with public data, and isolated different kind of data, the client category is designated to match the API category. 

All the client is listed in below table. Each client is very small and simple, it is only responsible to operate its related data, you can pick up multiple clients to create your own application based on your business.

| Data Category | Client        | Privacy | API Protocol       |
| ------------- | ------------- | ------- | ------------------ |
| Generic       | GenericClient | Public  | Rest               |
| Market        | MarketClient  | Public  | Rest, WebSocket    |
| Account       | AccountClient | Private | Rest, WebSocket v2 |
| Wallet        | WalletClient  | Private | Rest               |
| Trade         | TradeClient   | Private | Rest, WebSocket v2 |
| Margin        | MarginClient  | Private | Rest               |
| ETF           | ETFClient     | Private | Rest               |

#### Customized Host
The client class support customized host so that you can define your own host, refer to example in later section.

#### Public and Private

There are two types of privacy that is correspondent with privacy of API:

**Public client**: It invokes public API to get public data (Generic data and Market data), therefore you can create a new instance without applying an API Key.

```python
// Create a GenericClient instance
generic_client = GenericClient()

// Create a MarketClient instance with customized host
market_client = MarketClient(url="https://api-aws.huobi.pro")
```

**Private client**: It invokes private API to access private data, you need to follow the API document to apply an API Key first, and pass the API Key to the init function

```python
// Create an AccountClient instance with APIKey
account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)

// Create a TradeClient instance with API Key and customized host
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url="https://api-aws.huobi.pro")
```

The API key is used for authentication. If the authentication cannot pass, the invoking of private interface will fail.

#### Rest and WebSocket

There are two protocols of API, Rest and WebSocket

**Rest**: It invokes Rest API and get once-off response, it has two basic types of method: GET and POST

**WebSocket**: It establishes WebSocket connection with server and data will be pushed from server actively. There are two types of method for WebSocket client:

- Request method: The method name starts with "Request-", it will receive the once-off data after sending the request.
- Subscription: The method name starts with "Subscribe-", it will receive update after sending the subscription.

In this python SDK, some clients support both Rest and WebSocket protocols, the method name are prefixed and can be easily identified, take TradeClient as an example, the method prefix and their examples are:

- **get**: get_order, get_matchresult
- **post**: post_create_order, post_batch_cancel_open_order
- **req**: req_order_list
- **sub**: sub_order_update


## Request example

### Reference data

#### Exchange timestamp

```python
generic_client = GenericClient()
list_obj = generic_client.get_exchange_symbols()
```

#### Symbol and currencies

```python
generic_client = GenericClient()
list_symbol = generic_client.get_exchange_symbols()
list_currency = generic_client.get_reference_currencies()
```

### Market data

#### Candlestick

```python
market_client = MarketClient()
list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 10)
```

#### Depth

```python
market_client = MarketClient()
depth = market_client.get_pricedepth("btcusdt", DepthStep.STEP0, depth_size)
```

#### Latest trade

```python
market_client = MarketClient()
list_obj = market_client.get_market_trade(symbol="btcusdt")
```

#### Historical

```python
market_client = MarketClient()
list_obj = market_client.get_history_trade("btcusdt", 6)
```

### Account

*Authentication is required.*

#### Get account balance

```python
account_client = AccountClient(api_key=g_api_key, secret_key=g_secret_key)
account_balance_list = account_client.get_account_balance()
```

### Wallet

*Authentication is required.*

#### Withdraw

```python
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id = wallet_client.post_create_withdraw(address="xxxxxx",
                                                     amount=40, currency="trx", fee=1,
                                                     chain=None, address_tag=None)
```

#### Cancel withdraw

```python
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
withdraw_id_ret = wallet_client.post_cancel_withdraw(withdraw_id=withdraw_id)
```

#### Withdraw and deposit history

```python
wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key)
list_deposit_history = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.DEPOSIT, currency=None, from_id=1, size=10, direct=QueryDirection.PREV)
list_withdraw_history = wallet_client.get_deposit_withdraw(op_type=DepositWithdraw.WITHDRAW, currency=None, from_id=1, size=10, direct=QueryDirection.NEXT)
```

### Trading

*Authentication is required.*

#### Create order

```python
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.BUY_LIMIT, source=OrderSource.API, amount=4.0, price=1.292)
```

#### Cancel order

```python
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
canceled_order_id  = trade_client.cancel_order(symbol_test, order_id)
```

#### Cancel open orders

```python
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
result  = trade_client.cancel_open_orders(account_id=g_account_id)
```

#### Get order info

```python
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
orderObj = trade_client.get_order(order_id=order_id)
```

#### Historical orders

```python
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = trade_client.get_history_orders(symbol="btcusdt", start_time=None, end_time=None, size=20, direct=None)
```

### Margin Loan

*Authentication is required.*

These are examples for cross margin

#### Apply loan

```python
margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
loan_id = margin_client.post_create_margin_order(symbol="eosusdt", currency="usdt", amount=loan_amount)
```

#### Repay loan

```python
margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
transfer_id = margin_client.post_repay_margin_order(loan_id=7440184, amount=100.004083)
```

#### Loan history

```python
margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = margin_client.get_margin_loan_orders(symbol="eosusdt")
```

## Subscription example

### Subscribe trade update

```python
def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()
    print()

market_client = MarketClient()
market_client.sub_trade_detail("btcusdt,eosusdt", callback)
```

### Subscribe candlestick update

```python
def callback(candlestick_event: 'CandlestickEvent'):
    candlestick_event.print_object()
    print("\n")

def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN1, callback, error)
```

### Subscribe order update

*Authentication is required.*

```python
def callback(upd_event: 'OrderUpdateEvent'):
    print("---- order update : ----")
    upd_event.print_object()
    print()

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, init_log=True)
trade_client.sub_order_update("eosusdt", callback)
```

### Subscribe account change

*Authentication is required.*

```python
def callback(account_change_event: 'AccountChangeEvent'):
    account_change_event.print_object()
    print()

account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              init_log=True)
account_client.sub_account_update(AccountBalanceMode.TOTAL, callback)
```

