from tranco import Tranco
t = Tranco(account_email="abc@xyz.eu", api_key="123ABC")


latest_list = t.list()
date_list = t.list(date='2019-02-25')

latest_list.top(10000)

print(latest_list)