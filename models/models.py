""" model
"""
from const import Const


class CarcassMarketPrice(object):
    """ Summary
    """
    # Constructor
    def __init__(self):
        # 全農値
        self.market_date = Const.STRING_EMPTY
        self.nationwide_slaughter = Const.STRING_EMPTY
        self.zennoh_high_price = Const.INT_UNSET
        self.zennoh_middle_price = Const.INT_UNSET
        
        # Tokyo
        self.tokyo_high_price = Const.INT_UNSET
        self.tokyo_middle_price = Const.INT_UNSET
        self.tokyo_ordinary_price = Const.INT_UNSET
        self.tokyo_outside_price = Const.INT_UNSET
        self.tokyo_head_count = Const.INT_UNSET
        
        # Saitama
        self.saitama_high_price = Const.INT_UNSET
        self.saitama_middle_price = Const.INT_UNSET
        self.saitama_ordinary_price = Const.INT_UNSET
        self.saitama_outside_price = Const.INT_UNSET
        self.saitama_head_count = Const.INT_UNSET
        
        # Yokohama
        self.yokohama_high_price = Const.INT_UNSET
        self.yokohama_middle_price = Const.INT_UNSET
        self.yokohama_ordinary_price = Const.INT_UNSET
        self.yokohama_outside_price = Const.INT_UNSET
        self.yokohama_head_count = Const.INT_UNSET
        
        # Osaka
        self.osaka_high_price = Const.INT_UNSET
        self.osaka_middle_price = Const.INT_UNSET
        self.osaka_ordinary_price = Const.INT_UNSET
        self.osaka_outside_price = Const.INT_UNSET
        self.osaka_head_count = Const.INT_UNSET


