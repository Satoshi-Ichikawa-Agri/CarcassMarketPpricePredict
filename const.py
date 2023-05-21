""" 定数やfunctionの管理 """
import os
import time
from datetime import date, datetime


class Const(object):
    """ 定数とfunction """
    
    WORKSPACE_DIR = os.getcwd() # 'C:\\Users\\daiko\\Develop_satoshi\\CarcassMarketPpricePredict'
    
    ZENNO_URL = 'https://www.jazmf.co.jp/market/list.html'
    DOWNLOAD_DIR = 'C:/Users/daiko/Downloads'
    OUTPUT_DIR = f'{ WORKSPACE_DIR }/output'
    
    INT_UNSET = -1 # int型valueのunset
    STRING_EMPTY = '' # str型valueのunset
    
    YEAR_MONTHS = ('4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月')
    LAST_YEAR_MONTHS = ('1月', '2月', '3月')


    DATE_NOW = datetime.now().strftime('%Y/%m/%d_%H:%M:%S') # 本日日時
    
    TODAY = date.today() # 本日日付(2023, 4, 12)
    DATE_TODAY = date.today().strftime('%Y/%m/%d') # 本日日付('2023/04/12')
    DATE_YEAR_AND_MONTH = date.today().strftime('%Y%m') # 当月('202304')
    

    @classmethod
    def check_target_date(cls, arg_list):
        """ Consoleの引数からtarget_dateを取得する
        python main.py 202303
        """
        if len(arg_list) == 1:
            target_date = None
        else:
            target_date = arg_list[1]
        return target_date


    @classmethod
    def is_null_or_empty(cls, value):
        """指定値がNoneもしくは空でないかをチェックする
        """
        if value is None or value == 'None':
            return True
        if len(value) == 0:
            return True
        
        return False


    @classmethod
    def date_replace(cls, value: str):
        """ 日付のReplace
        Parameters:
            value: ダウンロードA列の「日」の値(例01日,02日)
        """
        value_trance = value.replace('日', '') # 01~31
        
        return value_trance


    @classmethod
    def from_str_to_date(cls, value: str):
        """ 日付の型変換(str → date)
        """
        date_date = date.fromisoformat(value)
        
        return date_date


    @classmethod
    def remove_value(cls, value, start, end):
        """ 指定した範囲の文字列を削除する
        Parameters:
            value: 対象の値
            start: 開始位置
            end: 終了位置
        """
        return value[:start] + value[end + 1:]


    @classmethod
    def time_keeper(cls, seconds: int):
        """ Time Keeper """
        time.sleep(seconds)

