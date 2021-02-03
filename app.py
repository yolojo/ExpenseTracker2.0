from Bankingbot import date_price
from Bankingbot import category
from Bankingbot import BankBot
import pandas as pd

mytrans = BankBot("megaskidboy", "Salvation1")
mytrans.get_account_name("Miscellaneous - 8596")
mytrans.get_date("01/13/2021")
mytrans.get_transactions()

#print(date_price)
#print(category)

#for item in date_price:
#    if "Add" in item:
#       print(item)

df = pd.Dataframe(date_price, columns=["Date", "Transaction", "Amount"])
df
