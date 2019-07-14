from client import Client
from consts import *


class SpotAPI(Client):

    def __init__(self, api_key, api_seceret_key, passphrase, use_server_time=False):
        Client.__init__(self, api_key, api_seceret_key, passphrase, use_server_time)

    # query spot account info
    def get_account_info(self):
        return self._request_without_params(POST, SPOT_BALANCE)

    # trade_limit
    def trade_limit(self, _type , symbol, price , volume,  unique):
        params = { "type":_type , "volume":volume , "price":price , "symbol": symbol , "unique":unique}
        return self._request_with_params( POST, SPOT_TRADE_LIMIT , params )

    # cancel_order
    def cancel_order(self, symbol, order_id ):
        params = { "symbol":symbol , "order_id":order_id }
        return self._request_with_params( POST, SPOT_CANCEL_ORDER , params )

    # query order
    def query_order(self ,symbol , order_id ):
        params = { "symbol":symbol , "order_id":order_id }
        return self._request_with_params( POST, SPOT_QUERY_ORDER , params )

    # query symbol's open order
    def query_open_order(self, symbol):
        params = { "symbol":symbol }
        return self._request_with_params( POST,  SPOT_QUERY_OEPN_ORDER , params )

    # query complete orders
    def query_recent_complete_orders(self, symbol, limit):
        params = { "symbol":symbol, "limit":limit}
        return self._request_with_params( POST,  SPOT_QUERY_RECENT_COMPLETE_ORDER , params )

    # query recent_trade
    def query_recent_trade(self, symbol , limit):
        params = { "symbol":symbol, "limit":limit}
        return self._request_with_params( POST,  SPOT_QUERY_RECENT_TRADE , params )

