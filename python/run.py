from spot_api import *


if __name__ == "__main__":
	api_key = "hWizJcxsuoJ9KVwAddovyjAwNiJzevuLwhXervsvg"
	secretkey = "BuQQM9mvli7cbhZyaxro9FeOWYzPzHl9nnXFGNb9v8"
	passphrase = "passphrase"

	#secretkey = "1"

	api = SpotAPI(api_key , secretkey , passphrase )
	
	# data = api.get_account_info()
	# print data

	data = api.trade_limit("buy" , "BTC_USDT", 12000, 2 , "abc")
	print data

	# data = api.cancel_order("BTC_USDT",109)
	# print data 

	# data = api.query_order("BTC_USDT",10000)
	# print data

	# data = api.query_open_order("BTC_USDT")
	# print data

	# data = api.query_recent_complete_orders("BTC_USDT", 5)
	# print data

	data = api.query_recent_trade("BTC_USDT",5)
	print data
