from flask_restful import Api
# from .users_api import UsersResource, UserResource
from .stockdata.stockdata_api import (XsgDataResource, 
                            XsgDataOneResource, 
                            TodayAllResource,
                            StockBreakLimitResource,
                            StClassifiedResource,
                            CapTopsResource,
                            FundHoldings2020Q1Resource,
                            InstDetailResource,
                            StockBasicsResource,
                            )
from .common.blacklist_api import BlackListsResource, BlackListResource

restapi = Api()

def init_restapi(app):
    restapi.init_app(app)

restapi.add_resource(XsgDataResource, '/xsg_data/')
restapi.add_resource(XsgDataOneResource, '/xsg_data/<int:id>/')
restapi.add_resource(TodayAllResource, '/today_all/')
restapi.add_resource(StockBreakLimitResource, '/stock_breaklimit/')
restapi.add_resource(BlackListsResource, '/blacklists/')
restapi.add_resource(BlackListResource, '/blacklist/<int:id>')
restapi.add_resource(StClassifiedResource, '/st_classified/')
restapi.add_resource(CapTopsResource, '/cap_tops/')
restapi.add_resource(FundHoldings2020Q1Resource, '/fund_holdings2020q1/')
restapi.add_resource(InstDetailResource, '/inst_detail/')
restapi.add_resource(StockBasicsResource, '/stock_basics/')
