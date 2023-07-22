""" model """
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Date

from const import Const
from settings import DbSetting


# SQLAlchemyのBASEClass
BASE = declarative_base()


class CarcassMarketPrice(BASE):
    """ Carcass Market Price Model """

    __tablename__ = "carcass_market_price"  # テーブル名

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主キー
    market_date = Column(Date, nullable=False)
    nationwide_slaughter = Column(Integer, nullable=True)
    zennoh_high_price = Column(Integer, nullable=True)
    zennoh_middle_price = Column(Integer, nullable=True)
    # TOKYO
    tokyo_high_price = Column(Integer, nullable=True)
    tokyo_middle_price = Column(Integer, nullable=True)
    tokyo_ordinary_price = Column(Integer, nullable=True)
    tokyo_outside_price = Column(Integer, nullable=True)
    tokyo_head_count = Column(Integer, nullable=True)
    # SAITAMA
    saitama_high_price = Column(Integer, nullable=True)
    saitama_middle_price = Column(Integer, nullable=True)
    saitama_ordinary_price = Column(Integer, nullable=True)
    saitama_outside_price = Column(Integer, nullable=True)
    saitama_head_count = Column(Integer, nullable=True)
    # YOKOHAMA
    yokohama_high_price = Column(Integer, nullable=True)
    yokohama_middle_price = Column(Integer, nullable=True)
    yokohama_ordinary_price = Column(Integer, nullable=True)
    yokohama_outside_price = Column(Integer, nullable=True)
    yokohama_head_count = Column(Integer, nullable=True)
    # OSAKA
    osaka_high_price = Column(Integer, nullable=True)
    osaka_middle_price = Column(Integer, nullable=True)
    osaka_ordinary_price = Column(Integer, nullable=True)
    osaka_outside_price = Column(Integer, nullable=True)
    osaka_head_count = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)


class CarcassMarketPriceExcel(object):
    """ SummaryExcel Model """

    def __init__(self):
        """Constructor"""
        self.index = Const.INT_UNSET  # for文のindex用
        # 全農値
        self.market_date = Const.STRING_UNSET
        self.nationwide_slaughter = Const.STRING_UNSET
        self.zennoh_high_price = Const.STRING_UNSET
        self.zennoh_middle_price = Const.STRING_UNSET
        # Tokyo
        self.tokyo_high_price = Const.STRING_UNSET
        self.tokyo_middle_price = Const.STRING_UNSET
        self.tokyo_ordinary_price = Const.STRING_UNSET
        self.tokyo_outside_price = Const.STRING_UNSET
        self.tokyo_head_count = Const.STRING_UNSET
        # Saitama
        self.saitama_high_price = Const.STRING_UNSET
        self.saitama_middle_price = Const.STRING_UNSET
        self.saitama_ordinary_price = Const.STRING_UNSET
        self.saitama_outside_price = Const.STRING_UNSET
        self.saitama_head_count = Const.STRING_UNSET
        # Yokohama
        self.yokohama_high_price = Const.STRING_UNSET
        self.yokohama_middle_price = Const.STRING_UNSET
        self.yokohama_ordinary_price = Const.STRING_UNSET
        self.yokohama_outside_price = Const.STRING_UNSET
        self.yokohama_head_count = Const.STRING_UNSET
        # Osaka
        self.osaka_high_price = Const.STRING_UNSET
        self.osaka_middle_price = Const.STRING_UNSET
        self.osaka_ordinary_price = Const.STRING_UNSET
        self.osaka_outside_price = Const.STRING_UNSET
        self.osaka_head_count = Const.STRING_UNSET


def create_table():
    """Create Table"""
    db_setting = DbSetting()
    engine = db_setting.get_db_engine()
    BASE.metadata.create_all(engine)

    return engine
