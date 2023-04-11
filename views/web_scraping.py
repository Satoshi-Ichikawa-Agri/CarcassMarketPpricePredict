from datetime import date
import os
import shutil
from selenium import webdriver # Selenium Web自動操作
from selenium.webdriver.common.by import By # HTML要素の検索

from const import Const


class WebScraping(object):
    """
    """
    def __init__(self, target_date=None):
        self.target_date = target_date


    def processing(self):
        """ Auto Download
        """
        if self.target_date is None:
            self.__get_excel()
        else:
            self.__get_excel_specify()


    def file_move(self):
        """ ダウンロードファイルをワークフォルダにコピーする
        """
        download_dir = Const.DOWNLOAD_DIR
        download_file = '豚肉相場一覧表_202302.xlsx'
        carcass_file = os.path.join(download_dir, download_file)
        shutil.copy2(carcass_file, os.path.join(Const.WORKSPACE_DIR, 'download/'))


    def __get_excel(self):
        """ 引数指定をしない場合の処理
        当月から見て、前月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome()
        # 対象URLに接続
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(5)
        
        # 本日日付を取得する
        today = date.today() # →datetime.date(2023, 3, 17)
        
        # class属性からターゲット要素を絞り込む
        if today.month == 4:
            # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        else:
            target_elem = driver.find_element(By.CLASS_NAME, 'thisYear')

        months = target_elem.text.split('\n') # →['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月']
        
        # 本日から見て前月の”月”を取得する
        previous_month = str(today.month - 1) + "月" # →'M月'
        
        # monthsからターゲット月を取得する
        get_month = ''
        for month in months:
            if month == previous_month:
                get_month = month
                break
            continue

        # ターゲットのリンクテキスト名の要素を取得
        target_link = driver.find_element(By.LINK_TEXT, get_month)
        Const.time_keeper(2)
        driver.execute_script('arguments[0].click();', target_link)
        # target_link.click()
        Const.time_keeper(5)
        
        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(5)
        
        # [Excel]ボタンの実行
        driver.execute_script('javascript:excelout()')
        
        Const.time_keeper(10)
        driver.close()
        
        return int(get_month)
    
    
    def __get_excel_specify(self):
        """ 引数指定をする場合の処理
        引数の月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome()
        # 対象URLに接続
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(5)
        
        # 引数を年と月に分ける
        target_year = int(self.target_date[0:4])
        target_month = self.target_date[5:6] + '月'
        
        # 本日日付を取得する
        today = date.today() # →datetime.date(例:2023, 3, 17)
        
        # class属性からターゲット要素を絞り込む
        if target_year == today.year:
            target_elem = driver.find_element(By.CLASS_NAME, 'thisYear')
        elif target_year == today.year and target_month == 4:
            # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        elif target_year < today.year:
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        else:
            return

        months = target_elem.text.split('\n') # →['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月']
        
        # monthsからターゲット月を取得する
        get_month = ''
        for month in months:
            if month == target_month:
                get_month = month
                break
            continue

        # ターゲットのリンクテキスト名の要素を取得
        target_link = driver.find_element(By.LINK_TEXT, get_month)
        Const.time_keeper(2)
        target_link.click()
        Const.time_keeper(5)
        
        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(5)
        
        # [Excel]ボタンの実行
        btn_excel = 'javascript:excelout()'
        driver.execute_script(btn_excel)
        
        Const.time_keeper(10)
        driver.close()
        
        return int(get_month)
