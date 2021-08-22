from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.utils import LogInfo

api_key = "cdgs9k03f3-0f3fcdba-7ca8754e-c21b7"
secret_key = "a6514e6d-1296c40e-d2c61cc2-03269"

account_client = AccountClient(api_key=api_key, secret_key=secret_key)
LogInfo.output(
    "====== (SDK encapsulated api) not recommend for low performance and frequence limitation ======")
print(
    api_key, secret_key
)
account_balance_list = account_client.get_account_balance()
if account_balance_list and len(account_balance_list):
    for account_obj in account_balance_list:
        account_obj.print_object()
        print()
