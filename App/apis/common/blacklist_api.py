from flask_restful import Api, Resource, reqparse, fields, marshal_with, marshal, abort
from App.models.common.models import BlackListModel
import datetime

parser_base = reqparse.RequestParser()
parser_base.add_argument('black_ip_address', type=str, required=False, help='Must supply black_ip_address')
parser_base.add_argument('ip_owner_id', type=int, default=1)
parser_base.add_argument('ip_owner_browser', type=str, required=True, help='Must supply ip_owner_browser')

blacklist_fields = {
    'black_ip_address': fields.String,
    'ip_request_url': fields.String,
    'ip_request_path': fields.String,
    'ip_request_referrer': fields.String,
    'ip_owner_id': fields.Integer,
    'ip_owner_useragent': fields.String,
    'ip_block_date': fields.DateTime,
    'ip_block_date_expiry': fields.DateTime,
}

single_blacklist_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(blacklist_fields),
}

multi_blacklist_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(blacklist_fields)),
}

class BlackListsResource(Resource):

    @marshal_with(multi_blacklist_fields)
    def get(self):
        black_list = BlackListModel.query.all()
        data = {
            'msg': 'black_list get OK',
            'status': '200',
            'data': black_list,
        }
        return data

    def post(self):
        return {'msg': 'black_list post ok'}

class BlackListResource(Resource):

    @marshal_with(single_blacklist_fields)
    def get(self, id):
        black_list_one = BlackListModel.query.get(id)
        data = {
            'msg': 'black_list_one get OK',
            'status': '200',
            'data': black_list_one,
        }
        return data

    @marshal_with(single_blacklist_fields)
    def post(self):

        # 上面定义了parser之后，可以不从request.form里获取参数
        # 使用下面方法获取
        args = parser_base.parse_args()
        black_ip_address = args.get('black_ip_address')
        ip_request_url = args.get('ip_request_url')
        ip_request_path = args.get('ip_request_path')
        ip_request_referrer = args.get('ip_request_referrer')
        ip_owner_id = args.get('ip_owner_id')
        ip_owner_useragent = args.get('ip_owner_browser')
        ip_block_date = datetime.datetime.now()

        blacklist_instance = BlackListModel()
        blacklist_instance.black_ip_address = black_ip_address
        blacklist_instance.ip_request_url = ip_request_url 
        blacklist_instance.ip_request_path = ip_request_path 
        blacklist_instance.ip_request_referrer = ip_request_referrer 
        blacklist_instance.ip_owner_id = ip_owner_id
        blacklist_instance.ip_owner_useragent = ip_owner_useragent
        blacklist_instance.ip_block_date = ip_block_date
        blacklist_instance.ip_block_date_expiry = ip_block_date + datetime.timedelta(minutes=10)
        blacklist_instance_flag = blacklist_instance.save()
        
        if blacklist_instance_flag:
            # data = {
            #     'msg': 'create success',
            #     'status': 201,
            #     # 需要使用marshal将对象先进行序列化
            #     'data': marshal(good_instance, single_good_field)
            # }
            # return data

            # 使用装饰器函数marshal_with进行序列化
            nested_data = {
                'msg': 'black_list_one create success',
                'status': 201,
                'data': blacklist_instance
            }
            return nested_data
        else:
            abort(400)
        return {'msg': 'black_list_one post ok'}
