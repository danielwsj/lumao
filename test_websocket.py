import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json

aip_key = "c866a91b-8b57-4c31-bf79-e922b2648052"
secret_key = "B67BF55B2A6F84EF472379B7C710468E"
pass_phrase = ""

flag = '0' #实盘0 模拟盘1
# account api
accountAPI = Account.AccountAPI(aip_key, secret_key, pass_phrase, False, flag)

#查看账户余额 Get Balance
result = accountAPI.get_account()