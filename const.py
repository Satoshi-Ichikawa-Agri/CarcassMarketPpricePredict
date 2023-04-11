""" 定数やfunctionの管理
"""
import os
import time
from datetime import date, datetime


class Const(object):
    """ 定数とfunction
    """
    
    ZENNO_URL = 'https://www.jazmf.co.jp/market/list.html'
    DOWNLOAD_DIR = 'C:/Users/daiko/Downloads'
    
    WORKSPACE_DIR = os.getcwd() # workspaceのdirectory_path
    
    INT_UNSET = -1 # int型valueのunset
    STRING_EMPTY = '' # str型valueのunset

    DATE_NOW = datetime.now().strftime('%Y/%m/%d_%H:%M:%S') # 本日日時
    DATE_TODAY = date.today().strftime('%Y/%m/%d') # 本日日付
    
    DELIMITER = '/'
    TRANCE_DATE = {
        '年': DELIMITER,
        '月': DELIMITER,
        '日': DELIMITER,
        '.': DELIMITER,
        '-': DELIMITER,
    }

    # Market Region
    TOKYO = '東京'
    SAITAMA = 'さいたま'
    YOKOHAMA = '横浜'
    OSAKA = '大阪'
    ZENNO = '全農建値'


    @classmethod
    def get_target_date(cls, arg_list):
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
        value_trance = int(value.replace('日', '')) # 1~31
        
        return value_trance


    @classmethod
    def time_keeper(cls, seconds: int):
        """ Time Keeper
        """
        time.sleep(seconds)

