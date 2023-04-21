import os
import shutil
from selenium import webdriver # Selenium Web自動操作
from selenium.webdriver.common.by import By # HTML要素の検索

from const import Const


class WebScraping(object):
    """ Web Scraping
    """
    def __init__(self, target_date):
        self.target_date = target_date


    def file_move(self, file_date):
        """ ダウンロードファイルをワークフォルダにコピーする
        """
        download_dir = Const.DOWNLOAD_DIR
        download_file = f'豚肉相場一覧表_{ file_date }.xlsx'
        carcass_file = os.path.join(download_dir, download_file)
        shutil.copy2(carcass_file, os.path.join(Const.WORKSPACE_DIR, 'download/'))


    def download_excel(self):
        """ 引数指定をしない場合の処理
        当月から見て、前月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome()
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(2)
        
        # class属性からターゲット要素を絞り込む
        if Const.TODAY.month == 4:
            # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        else:
            target_elem = driver.find_element(By.CLASS_NAME, 'thisYear')

        months = target_elem.text.split('\n') # →['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月']
        previous_month = str(Const.TODAY.month - 1) + '月' # 本日から見て前月の”月”を取得する →'M月'
        
        # monthsからターゲット月を取得する(※HTMLからの要素なので注意)
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
        Const.time_keeper(2)
        
        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(2)
        
        # [Excel]ボタンの実行
        driver.execute_script('javascript:excelout()')
        Const.time_keeper(5)
        
        driver.close()
        print('Excelを取得しました。')
        
        # return用で前月を取得する
        previous_month_return = int(Const.DATE_YEAR_AND_MONTH) -1 # yyyymm-1
        
        return previous_month_return
    
    
    def download_excel_specify(self):
        """ 引数指定をする場合の処理
        引数の月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome()
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(2)
        
        # 引数を年と月に分ける
        target_year = int(self.target_date[0:4])
        target_month = self.target_date[5:6] + '月'
        
        # class属性からターゲット要素を絞り込む
        if target_year == Const.TODAY.year and target_month in Const.YEAR_MONTHS:
            # 今年かつ4-12月であるとき
            target_elem = driver.find_element(By.CLASS_NAME, 'thisYear')
        elif target_year == Const.TODAY.year and target_month in Const.LAST_YEAR_MONTHS:
            # 今年かつ1-3月である
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        elif target_year == Const.TODAY.year -1 and target_month in Const.YEAR_MONTHS:
            # 昨年かつ4-12月である
            target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
        else:
            # 上記に該当しない場合は処理を終了
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
        driver.execute_script('arguments[0].click();', target_link)
        Const.time_keeper(2)
        
        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(2)
        
        # [Excel]ボタンの実行
        driver.execute_script('javascript:excelout()')
        Const.time_keeper(5)
        
        driver.close()
        print('Excelを取得しました。')
        
        file_date = int(self.target_date)
        
        return file_date


    def processing(self):
        """ Web Scraping processing
        return: 
            file_date: int型のターゲット年月(例:202303)
        """
        file_date = Const.INT_UNSET
        
        try:
            if self.target_date is None:
                file_date = self.download_excel()
            else:
                file_date = self.download_excel_specify()
        except:
            print('例外が発生しました。')
            return
        finally:
            self.file_move(file_date)
            print('コピーしました。')
            return file_date
