from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from App.settings import config
from App.exts import db
import os
import datetime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, Integer, Text, BigInteger, DateTime, Column, Float, Table

class XsgDataModel(db.Model):
    __tablename__ = 'xsg_data'
    # specify the primary_key to db model
    index = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    name = db.Column(db.String)
    date = db.Column(db.String)
    count = db.Column(db.Numeric(12,2))
    ratio = db.Column(db.Numeric(12,2))
    create_time = db.Column(db.String)

class TodayAllModel(db.Model):
    __tablename__ = 'today_all'
    # specify the primary_key to db model
    index = db.Column(db.Integer, primary_key=True)
    
    # __table__ = db.Table('today_all', 
    #                     # db.Column('index', Integer, primary_key=True),
    #                     db.metadata, 
    #                     # db.Model.metadata, 
    #                     autoload=True, 
    #                     extend_existing=True,
    #                     autoload_with=db.engine)
    
class StockBreakLimitModel(db.Model):
    __tablename__ = 'new_stocks_breaklimit'
    index = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.Text)
    stock_name = db.Column(db.Text)
    stock_amount = db.Column(db.BigInteger)
    stock_price = db.Column(db.Numeric(12,2))
    stock_pe = db.Column('stock_pe', db.Numeric(12,2))
    break_limit_flag = db.Column('break_limit_flag', Text)
    break_limit_day = db.Column('break_limit_day', Text)
    high_limit_cnt = db.Column('high_limit_cnt', BigInteger)
    break_turnover = db.Column('break_turnover', db.Numeric(12,2))
    break_vol = db.Column('break_vol', db.Numeric(12,2))
    accum_vol_pre_breakday = db.Column('accum_vol_pre_breakday', db.Numeric(12,2))
    accum_vol_on_breakday = db.Column('accum_vol_on_breakday', db.Numeric(12,2))
    close_price_on_breakday = db.Column('close_price_on_breakday', db.Numeric(12,2))
    close_price_on_enddate = db.Column('close_price_on_enddate', db.Numeric(12,2))
    max_close_price_afterbreak = db.Column('max_close_price_afterbreak', db.Numeric(12,2))
    max_close_price_day = db.Column('max_close_price_day', Text)
    day_interval = db.Column('day_interval', BigInteger)
    firstday_open_ipo_price_ratio = db.Column('firstday_open_ipo_price_ratio', db.Numeric(12,2))
    breakday_close_open_price_ratio = db.Column('breakday_close_open_price_ratio', db.Numeric(12,2))
    breakday_close_ipo_price_ratio = db.Column('breakday_close_ipo_price_ratio', db.Numeric(12,2))
    enddate_close_break_price_ratio = db.Column('enddate_close_break_price_ratio', db.Numeric(12,2))
    belong_year = db.Column('belong_year', BigInteger)
    belong_week = db.Column('belong_week', BigInteger)
    belong_yearweek = db.Column('belong_yearweek', Text)
    jump_high_flag= db.Column('jump_high_flag', Text)
    jump_high_day = db.Column('jump_high_day', Text)
    jump_high_times = db.Column('jump_high_times', BigInteger)
    breakDayOccurTimes = db.Column('breakDayOccurTimes', BigInteger)
    belongYearWeekOccurTimes = db.Column('belongYearWeekOccurTimes', BigInteger)
    create_time = db.Column('create_time', DateTime)
    # __table__ = db.Table('new_stocks_breaklimit', 
    #                     # db.Column('index', Integer, primary_key=True),
    #                     db.metadata, 
    #                     # db.Model.metadata, 
    #                     autoload=True, 
    #                     extend_existing=True,
    #                     autoload_with=db.engine)
    pass

# class StClassifiedModel(db.Model):

#     # index = db.Column(db.Integer, primary_key=True)
#     # t_st_classified = Table(
#     # 'st_classified', db.metadata,
#     # Column('index', BigInteger, index=True),
#     # Column('code', Text),
#     # Column('name', Text),
#     # Column('create_time', DateTime))
class StClassifiedModel(db.Model):
    __tablename__ = 'st_classified'
    index = db.Column(db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    # create_time = db.Column('create_time', db.DateTime)

class CapTopsModel(db.Model):
    __tablename__ = 'cap_tops'
    index = db.Column(db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    count = db.Column('count', db.BigInteger)
    bamount = db.Column('bamount', db.Numeric(12,2))
    samount = db.Column('samount', db.Numeric(12,2))
    net = db.Column('net', db.Numeric(12,2))
    bcount = db.Column('bcount', db.BigInteger)
    scount = db.Column('scount', db.BigInteger)
    create_time = db.Column('create_time', db.DateTime)

class FundHoldings2020Q1Model(db.Model):
    __tablename__ = 'fund_holdings2020q1'
    index = db.Column('index', db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    name = db.Column('nums', db.Text)
    nlast = db.Column('nlast', db.Text)
    count = db.Column('count', db.Text)
    amount = db.Column('amount', db.Text)
    clast = db.Column('clast', db.Text)
    ratio = db.Column('ratio', db.Text)
    date = db.Column('date', db.Text)
    create_time = db.Column('create_time', db.DateTime)

class InstDetailModel(db.Model):
    __tablename__ = 'inst_detail'
    index = db.Column('index', db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    bamount = db.Column('bamount', db.Numeric(12,2))
    samount = db.Column('samount', db.Numeric(12,2))
    date = db.Column('date', db.Text)
    type_ = db.Column('type', db.Text)
    create_time = db.Column('create_time', db.DateTime)

class StockBasicsModel(db.Model):
    __tablename__ = 'stock_basics'
    index = db.Column('index', db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    outstanding = db.Column('outstanding', db.Numeric(12,2))
    totals = db.Column('totals', db.Numeric(12,2))
    totalAssets = db.Column('totalAssets', db.Numeric(12,2))
    esp = db.Column('esp', db.Numeric(12,2))
    bvps = db.Column('bvps', db.Numeric(12,2))
    pb = db.Column('pb', db.Numeric(12,2))
    pe = db.Column('pe', db.Numeric(12,2))
    reservedPerShare = db.Column('reservedPerShare', db.Numeric(12,2))
    rev = db.Column('rev', db.Numeric(12,2))
    profit = db.Column('profit', db.Numeric(12,2))
    gpr = db.Column('gpr', db.Numeric(12,2))
    npr = db.Column('npr', db.Numeric(12,2))
    holders = db.Column('holders', db.Numeric(12,2))
    industry = db.Column('industry', db.Text)
    area = db.Column('area', db.Text)
    timeToMarket = db.Column('timeToMarket', db.BigInteger)
    create_time = db.Column('create_time', db.DateTime)

"""
class TestUserModel(db.Model):
    __tablename__ = 'test_user'
    index = db.Column(db.BigInteger, primary_key=True)
    code = db.Column('code', db.Text)
    name = db.Column('name', db.Text)
    # create_time = db.Column('create_time', db.DateTime)

column = Column('text', Text, primary_key=False, unique=False)
try:
    # add_column(db.engine, 'xsg_data', column)
    # drop_column(db.engine, 'xsg_data', column)
    pass
except Exception as e:
    # drop_column(engine, 'xsg_data', column)
    print('error:', type(e), e)
else:
    pass
"""

"""
Base = automap_base()
class XsgDataModel(Base):
    __tablename__ = 'xsg_data'
    # specify the primary_key to db model
    index = db.Column(db.Integer, primary_key=True)

Base.prepare(db.get_engine(), reflect=True)
"""
# all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
# print('models.py all_table:', all_table)
