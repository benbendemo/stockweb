import requests
import hashlib
import base64
import time
import datetime
from flask import current_app, request
from functools import wraps
from App.exts import db
from App.models.common.models import BlackListModel

def add_ip_into_blacklist():
    black_ip_one = BlackListModel(black_ip_address=request.remote_addr,
                                    ip_request_url=request.url,
                                    ip_request_path=request.path,
                                    ip_request_referrer=request.referrer,
                                    ip_owner_id=10,
                                    ip_owner_useragent=request.user_agent.string,
                                    ip_block_date=datetime.datetime.now(),
                                    ip_block_date_expiry=datetime.datetime.now()+datetime.timedelta(minutes=10),
                                    )
    try:
        db.session.add_all([black_ip_one])
    except Exception as e:
        print('write_blacklist error value:', e)
        print('write_blacklist error type:', type(e))
        db.rollback()
    else:
        db.session.commit()

def check_ip_in_blacklist(ip_addr):
    
    blacklist_instance = BlackListModel.query.filter(BlackListModel.black_ip_address==ip_addr)
    if blacklist_instance.count() == 0:
        return False
    
    # Use `first` to fetch the first one; use `-1` to fetch the last one
    blacklist_one = blacklist_instance[-1]

    # If blacklist_one is None, it means `ip_addr` not blocked 
    if blacklist_one is not None:
        if blacklist_one.ip_block_date_expiry > datetime.datetime.now():
            return True
    return False

def _decorator(func):
    @wraps(func)
    def _wrap(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f'{request.host_url} takes {t2-t1} seconds')
        return res
    return _wrap

def encode_content(content):
    encode_content = base64.standard_b64encode(content.encode('UTF-8')).decode('UTF-8')
    print('getnews encode_content:', encode_content)

    psk1 = 'CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk'
    psk2 = 'pOq3kRIxs26rmRtsUTJvBn9Z'
    psk_encode_content = psk1 + encode_content + psk2
    print('getnews psk_encode_content:', psk_encode_content)
    
    encode_content_2 = base64.standard_b64encode(psk_encode_content.encode('UTF-8')).decode('UTF-8')
    print('getnews encode_content_2:', encode_content_2)
    return encode_content_2

def send_sms(phone):
    url = 'https://api.netease.im/sms/sendcode.action'
    WYYX_APP_KEY = 'c2ddbc9a092c318f5e7f137c8bda5711'
    WYYX_APP_SECRET = 'b5df98f7dbd4'
    nonce = hashlib.new('sha512', str(time.time()).encode('UTF-8')).hexdigest()
    print('sendsms nonce:', type(nonce), nonce)
    curr_time = str(int(time.time()))
    print('sendsms curr_time:', type(curr_time), curr_time)
    sha1 = hashlib.sha1()
    sha1.update((WYYX_APP_SECRET + nonce + curr_time).encode('UTF-8'))
    print('sendsms sha1:', type(sha1), sha1)
    check_sum = sha1.hexdigest()
    # check_sum = hashlib.sha1().update((WYYX_APP_SECRET + nonce + curr_time).encode('UTF-8')).hexdigest()
    print('sendsms check_sum:', type(check_sum), check_sum)
    header = {
        'AppKey': WYYX_APP_KEY,
        'Nonce': nonce,
        'CurTime': curr_time,
        'CheckSum': check_sum
    }
    post_data = {
        'mobile': phone
    }
    resp = requests.post(url, data=post_data, headers=header)
    return resp
