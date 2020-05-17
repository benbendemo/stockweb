from flask_restful import (Api, 
                            Resource, 
                            reqparse, 
                            fields, 
                            marshal_with, 
                            marshal)
from App.models.stockdata.models import (XsgDataModel, 
                                            TodayAllModel, 
                                            StockBreakLimitModel, 
                                            StClassifiedModel,
                                            CapTopsModel,
                                            FundHoldings2020Q1Model,
                                            InstDetailModel,
                                            StockBasicsModel)

"""
parser_base = reqparse.RequestParser()
parser_base.add_argument('index', type=str, required=False, help='Must supply index')
parser_base.add_argument('code', type=str, required=True, help='Must supply code')
parser_base.add_argument('name', type=str, required=True, help='Must supply name')
parser_base.add_argument('date', type=str, required=True, help='Must supply date')
parser_base.add_argument('count', type=str, required=True, help='Must supply count')
parser_base.add_argument('ratio', type=str, required=True, help='Must supply ratio')
parser_base.add_argument('create_time', type=str, help='Must supply create_time')
"""

stockdata_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    # 'date': fields.String,
    # 'count': fields.String,
    # 'ratio': fields.String,
    # 'create_time': fields.String,
}

st_classified_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'create_time': fields.String,
}

stock_breaklimit_fields = {
    'index': fields.Integer,
    'stock_code': fields.String,
    'stock_name': fields.String,
    'stock_amount': fields.Float,
    'stock_price': fields.Float,
    'stock_pe': fields.Float,
    'break_limit_day': fields.String,
}

cap_tops_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'count': fields.Float,
    'bamount': fields.Float,
    'samount': fields.Float,
    'net': fields.Float,
    'bcount': fields.Integer,
    'scount': fields.Integer,
    'create_time': fields.String,
}

fund_holdings_2020q1_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'nums': fields.String,
    'nlast': fields.String,
    'count': fields.String,
    'amount': fields.String,
    'clast': fields.String,
    'ratio': fields.String,
    'date': fields.String,
    'create_time': fields.String,
}

inst_detail_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'bamount': fields.Float,
    'samount': fields.Float,
    'date': fields.String,
    'type_': fields.String,
    'create_time': fields.String,
}

stock_basics_fields = {
    'index': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'outstanding': fields.Float,
    'totals': fields.Float,
    'totalAssets': fields.Float,
    'esp': fields.Float,
    'bvps': fields.Float,
    'pb': fields.Float,
    'pe': fields.Float,
    'reservedPerShare': fields.Float,
    'rev': fields.Float,
    'profit': fields.Float,
    'gpr': fields.Float,
    'npr': fields.Float,
    'holders': fields.Float,
    'industry': fields.String,
    'area': fields.String,
    'timeToMarket': fields.Integer,
    'create_time': fields.String,
}

single_cap_tops_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(cap_tops_fields),
}

multi_cap_tops_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(cap_tops_fields)),
}

single_fund_holdings_2020q1_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(fund_holdings_2020q1_fields),
}

multi_fund_holdings_2020q1_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(fund_holdings_2020q1_fields)),
}

single_inst_detail_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(inst_detail_fields),
}

multi_inst_detail_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(inst_detail_fields)),
}

single_stock_basics_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(stock_basics_fields),
}

multi_stock_basics_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(stock_basics_fields)),
}

single_stockdata_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(stockdata_fields),
}

multi_stockdata_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(stockdata_fields)),
}

multi_stock_breaklimit_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(stock_breaklimit_fields)),
}

multi_st_classified_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(st_classified_fields)),
}

multi_test_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(st_classified_fields)),
}

class XsgDataResource(Resource):

    @marshal_with(multi_stockdata_fields)
    def get(self):

        xsg_data_list = XsgDataModel.query.all()
        
        data = {
            'msg': 'xsg_data_list get OK',
            'status': '200',
            'data': xsg_data_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'xsg_data_list post ok'}

class XsgDataOneResource(Resource):

    @marshal_with(single_stockdata_fields)
    def get(self, id):

        xsg_data_one = XsgDataModel.query.get(id)
        # print('xsg_data_one:', type(xsg_data_one), dir(xsg_data_one), xsg_data_one)

        data = {
            'msg': 'xsg_data_one get OK',
            'status': '200',
            'data': xsg_data_one,
        }
        return data

    def post(self):
        return {'msg': 'xsg_data_one post ok'}

class TodayAllResource(Resource):

    @marshal_with(multi_stockdata_fields)
    def get(self):

        today_all_list = TodayAllModel.query.all()
        
        data = {
            'msg': 'today_all_list get OK',
            'status': '200',
            'data': today_all_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)


    def post(self):
        return {'msg': 'today_all_list post ok'}

class StockBreakLimitResource(Resource):

    @marshal_with(multi_stock_breaklimit_fields)
    def get(self):

        stock_break_limit_list = StockBreakLimitModel.query.all()
        print('stock_break_limit_list:',len(stock_break_limit_list))
        data = {
            'msg': 'stock_break_limit get OK',
            'status': '200',
            'data': stock_break_limit_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'stock_break_limit post ok'}

class StClassifiedResource(Resource):

    @marshal_with(multi_st_classified_fields)
    def get(self):

        st_classified_list = StClassifiedModel.query.all()
        print('st_classified_list:',len(st_classified_list))
        data = {
            'msg': 'st_classified get OK',
            'status': '200',
            'data': st_classified_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'st_classified post ok'}

class CapTopsResource(Resource):

    @marshal_with(multi_cap_tops_fields)
    def get(self):

        cap_tops_list = CapTopsModel.query.all()
        data = {
            'msg': 'cap_tops_list get OK',
            'status': '200',
            'data': cap_tops_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'cap_tops_list post ok'}

class FundHoldings2020Q1Resource(Resource):

    @marshal_with(multi_fund_holdings_2020q1_fields)
    def get(self):

        fund_holdings_2020q1_list = FundHoldings2020Q1Model.query.all()
        data = {
            'msg': 'fund_holdings_2020q1_list get OK',
            'status': '200',
            'data': fund_holdings_2020q1_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'fund_holdings_2020q1_list post ok'}

class InstDetailResource(Resource):

    @marshal_with(multi_inst_detail_fields)
    def get(self):

        inst_detail_list = InstDetailModel.query.all()
        data = {
            'msg': 'inst_detail_list get OK',
            'status': '200',
            'data': inst_detail_list,
        }
        return data
        # return marshal(data, multi_stockdata_fields)

    def post(self):
        return {'msg': 'inst_detail_list post ok'}

class StockBasicsResource(Resource):

    @marshal_with(multi_stock_basics_fields)
    def get(self):

        stock_basics_list = StockBasicsModel.query.all()
        data = {
            'msg': 'stock_basics_list get OK',
            'status': '200',
            'data': stock_basics_list,
        }
        return data

    def post(self):
        return {'msg': 'stock_basics_list post ok'}
