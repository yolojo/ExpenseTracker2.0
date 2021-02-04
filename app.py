from Bankingbot import date_price
from Bankingbot import category
from Bankingbot import BankBot
import pandas as pd

mytrans = BankBot("YOUR LOGIN ID", "YOUR PASSWORD")
mytrans.get_account_name("BANK ACCOUNT NAME")
mytrans.get_date("DATE")
mytrans.get_transactions()

#print(date_price)
#print(category)

#for item in date_price:
#    if "Add" in item:
#       print(item)

df = pd.Dataframe(date_price, columns=["Date", "Transaction", "Amount"])
df
