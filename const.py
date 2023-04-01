""" 定数やfunctionの管理
"""
import os
from datetime import date, datetime


class Const(object):
    """ 定数とfunction
    """
    
    WORKSPACE_DIR = os.getcwd() # workspaceのdirectory_path
    
    INT_UNSET = -1 # int型valueのunset
    STRING_EMPTY = "" # str型valueのunset

    DATE_NOW = datetime.now().strftime('%Y/%m/%d_%H:%M:%S') # 本日日時
    DATE_TODAY = date.today().strftime('%Y/%m/%d') # 本日日付
    
    DELIMITER = '/'
    TRANCE_DATE = {
        "年": DELIMITER,
        "月": DELIMITER,
        "日": DELIMITER,
        ".": DELIMITER,
        "-": DELIMITER,
    }

    # Market Region
    TOKYO = "東京"
    SAITAMA = "さいたま"
    YOKOHAMA = "横浜"
    OSAKA = "大阪"
    ZENNO = "全農建値"


    @classmethod
    def date_replace(cls, value: str):
        """ 日付のReplace
        Parameters:
            value: ダウンロードA列の「日」の値(例01日,02日)
        """
        value_trance = int(value.replace('日', '')) # 1~31
        return value_trance
