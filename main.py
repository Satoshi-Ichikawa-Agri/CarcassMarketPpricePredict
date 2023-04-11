""" 自動ダウンロードProgram
全農ミートフーズのホームページから、
豚肉相場一覧表_yyyymm.xlsxを自動で取得するプログラム
取得するタイミングは月1とし、翌月になるタイミングで前月の集計データを取得する
"""
import sys
import traceback

from const import Const
from views.web_scraping import WebScraping
from views.data_cleansing import DataCleansing


def execute():
    """ 実行
    """
    # コマンドライン引数を取得する
    # arg_list = sys.argv
    
    # web_scraping = WebScraping(Const.get_target_date(arg_list))
    # web_scraping.processing()
    
    web_scraping = WebScraping()
    web_scraping.file_move()
    
    # data_cleansing = DataCleansing()
    # data_cleansing.data_cleansing_process()


if __name__ == '__main__':
    execute()

