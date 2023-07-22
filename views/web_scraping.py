"""Get Download File Module"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from const import Const


class WebScraping(object):
    """ Web Scraping """

    def __init__(self, target_date):
        self.target_date = target_date

    def file_move(self, file_date):
        """ ダウンロードファイルをワークフォルダにコピーする """
        to_copy_dir = str(Const.get_project_store_download_directory())
        download_file = Const.make_document_path(
            Const.WINDOWS_DOWNLOAS_DIR, f"豚肉相場一覧表_{ file_date }.xlsx")
        Const.file_copy(download_file, to_copy_dir)

    def download_excel(self):
        """ 引数指定をしない場合の処理
        当月から見て、前月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(2)

        # class属性からターゲット要素を絞り込む
        if Const.TODAY.month == 4:
            # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
            target_elem = driver.find_element(By.CLASS_NAME, "lastYear")
        else:
            target_elem = driver.find_element(By.CLASS_NAME, "thisYear")

        months = target_elem.text.split("\n")  # →["4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "1月", "2月", "3月"]
        previous_month = str(Const.TODAY.month - 1) + "月"  # 本日から見て前月の”月”を取得する →"M月"

        # monthsからターゲット月を取得する(※HTMLからの要素なので注意)
        get_month = ""
        for month in months:
            if month == previous_month:
                get_month = month
                break
            continue

        # ターゲットのリンクテキスト名の要素を取得
        target_link = driver.find_element(By.LINK_TEXT, get_month)
        driver.execute_script("arguments[0].click();", target_link)
        Const.time_keeper(2)

        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(2)

        # [Excel]ボタンの実行
        driver.execute_script("javascript:excelout()")
        Const.time_keeper(5)

        driver.close()
        print("Excelを取得しました。")

        # return用で前月を取得する
        previous_month_return = int(Const.DATE_YEAR_AND_MONTH) - 1  # yyyymm-1

        return previous_month_return

    def download_excel_specify(self):
        """ 引数指定をする場合の処理
        引数の月の枝肉市場結果を取得する。
        """
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(Const.ZENNO_URL)
        Const.time_keeper(2)

        # 引数を年と月に分ける
        target_year = int(self.target_date[0:4])
        if self.target_date[4] == "0":
            target_month = self.target_date[5] + "月"  # 1~9月
        else:
            target_month = self.target_date[4:6] + "月"  # 10~12月

        # class属性からターゲット要素を絞り込む
        # this_year_or_last_year_flag: 当年度:True, 昨年度:False
        if target_year == Const.TODAY.year + 1 and target_month in Const.LAST_YEAR_MONTHS:
            # 翌年かつ1-3月であるとき(=当年度)
            target_elem = driver.find_element(By.CLASS_NAME, "thisYear")
            this_year_or_last_year_flag = True
        elif target_year == Const.TODAY.year and target_month in Const.YEAR_MONTHS:
            # 今年かつ4-12月であるとき(=当年度)
            target_elem = driver.find_element(By.CLASS_NAME, "thisYear")
            this_year_or_last_year_flag = True
        elif target_year == Const.TODAY.year and target_month in Const.LAST_YEAR_MONTHS:
            # 今年かつ1-3月である(=昨年度)
            target_elem = driver.find_element(By.CLASS_NAME, "lastYear")
            this_year_or_last_year_flag = False
        elif target_year == Const.TODAY.year - 1 and target_month in Const.YEAR_MONTHS:
            # 昨年かつ4-12月である
            target_elem = driver.find_element(By.CLASS_NAME, "lastYear")
            this_year_or_last_year_flag = False
        else:
            # 上記に該当しない場合は処理を終了
            return

        months = target_elem.text.split("\n")  # →["4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "1月", "2月", "3月"]

        # monthsからターゲット月を取得する
        get_month = ""
        for month in months:
            if month == target_month:
                get_month = month
                break
            continue

        # ターゲットのリンクテキスト名の要素を取得
        target_link = driver.find_elements(By.LINK_TEXT, get_month)
        if this_year_or_last_year_flag:
            driver.execute_script("arguments[0].click();", target_link[0])
        elif not this_year_or_last_year_flag:
            if len(target_link) == 1:
                # 昨年度かつ、当年度に同一月が生成されていないとき
                driver.execute_script("arguments[0].click();", target_link[0])
            else:
                # 昨年度かつ、当年度に同一月が生成されているとき
                driver.execute_script("arguments[0].click();", target_link[1])
        else:
            return
        Const.time_keeper(2)

        # ブラウザのタブを切り替える(ページタブを切り替える)
        driver.switch_to.window(driver.window_handles[1])
        Const.time_keeper(2)

        # [Excel]ボタンの実行
        driver.execute_script("javascript:excelout()")
        Const.time_keeper(5)

        driver.close()
        print("Excelを取得しました。")

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
        except Exception as e:
            print("例外が発生しました。", {e})
            return
        finally:
            self.file_move(file_date)
            print("コピーしました。")
            return file_date
