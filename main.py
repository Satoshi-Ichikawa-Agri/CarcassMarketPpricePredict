""" 自動ダウンロードProgram
全農ミートフーズのホームページから、
豚肉相場一覧表_yyyymm.xlsxを自動で取得するプログラム
取得するタイミングは月1とし、翌月になるタイミングで前月の集計データを取得する

--願望--
出来ればタスクスケジューラで自動実行したいな
"""
import sys

from const import Const
from views.web_scraping import WebScraping
from views.data_cleansing import DataCleansing
from views.from_excel_to_db import DbInsert


def execute():
    """ 実行
    """
    # コマンドライン引数を取得する
    arg_list = sys.argv # 例：['main.py', '202303']
    
    web_scraping = WebScraping(Const.check_target_date(arg_list))
    file_date = web_scraping.processing()
    
    data_cleansing = DataCleansing(file_date)
    data_cleansing.data_cleansing_process()
    
    Const.time_keeper(5)
    db_insert = DbInsert()
    db_insert.insert_carcass()


if __name__ == '__main__':
    execute()
    print('全ての処理が終了しました。')

