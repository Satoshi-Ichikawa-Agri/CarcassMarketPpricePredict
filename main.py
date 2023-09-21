import sys

from CarcassMarketPpricePredict.constant import Const
from views.web_scraping import WebScraping
from views.data_cleansing import DataCleansing
from views.from_excel_to_db import DbInsert


def execute():
    """実行"""

    arg_list = sys.argv  # 例：["main.py", "202303"]

    # Scraping
    web_scraping = WebScraping(Const.check_target_date(arg_list))
    file_date = web_scraping.processing()

    # Data Cleansing
    data_cleansing = DataCleansing(file_date)
    data_cleansing.data_cleansing_process()

    # Table Insert
    Const.time_keeper(5)
    db_insert = DbInsert()
    db_insert.insert_carcass()


if __name__ == "__main__":
    print("----- 処理を開始しました。-----")
    execute()
    print("----- 全ての処理が終了しました。-----")
