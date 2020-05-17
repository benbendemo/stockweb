import datetime
from App.exts import db

class BlackListModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    black_ip_address = db.Column(db.String(30))
    ip_request_url = db.Column(db.String(128))
    ip_request_path = db.Column(db.String(128))
    ip_request_referrer = db.Column(db.String(128))
    ip_owner_id = db.Column(db.String(20))
    ip_owner_useragent = db.Column(db.String(256))
    ip_block_date = db.Column(db.DateTime, default=datetime.datetime.now)
    ip_block_date_expiry = db.Column(db.DateTime, default=datetime.datetime.now)
    # ip_block_date = db.Column(DATETIME(fsp=3))
    # ip_block_date_expiry = db.Column(DATETIME(fsp=3))
