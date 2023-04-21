""" model
"""
from const import Const


class CarcassMarketPrice(object):
    """ 枝肉相場データの一時格納テーブル
    """
    def __init__(self):
        self.index = Const.INT_UNSET # for文のindex用
        # 全農値
        self.market_date = Const.STRING_EMPTY
        self.nationwide_slaughter = Const.STRING_EMPTY
        self.zennoh_high_price = Const.STRING_EMPTY
        self.zennoh_middle_price = Const.STRING_EMPTY
        # Tokyo
        self.tokyo_high_price = Const.STRING_EMPTY
        self.tokyo_middle_price = Const.STRING_EMPTY
        self.tokyo_ordinary_price = Const.STRING_EMPTY
        self.tokyo_outside_price = Const.STRING_EMPTY
        self.tokyo_head_count = Const.STRING_EMPTY
        # Saitama
        self.saitama_high_price = Const.STRING_EMPTY
        self.saitama_middle_price = Const.STRING_EMPTY
        self.saitama_ordinary_price = Const.STRING_EMPTY
        self.saitama_outside_price = Const.STRING_EMPTY
        self.saitama_head_count = Const.STRING_EMPTY
        # Yokohama
        self.yokohama_high_price = Const.STRING_EMPTY
        self.yokohama_middle_price = Const.STRING_EMPTY
        self.yokohama_ordinary_price = Const.STRING_EMPTY
        self.yokohama_outside_price = Const.STRING_EMPTY
        self.yokohama_head_count = Const.STRING_EMPTY
        # Osaka
        self.osaka_high_price = Const.STRING_EMPTY
        self.osaka_middle_price = Const.STRING_EMPTY
        self.osaka_ordinary_price = Const.STRING_EMPTY
        self.osaka_outside_price = Const.STRING_EMPTY
        self.osaka_head_count = Const.STRING_EMPTY
