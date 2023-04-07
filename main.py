""" 自動ダウンロードProgram
全農ミートフーズのホームページから、
豚肉相場一覧表_yyyymm.xlsxを自動で取得するプログラム

取得するタイミングは月1とし、翌月になるタイミングで前月の集計データを取得する
"""
from views.web_scraping import get_excel, file_move
from views.data_cleansing import data_cleansing_process

if __name__ == '__main__':
    # get_excel()
    # file_move()
    data_cleansing_process()
    
