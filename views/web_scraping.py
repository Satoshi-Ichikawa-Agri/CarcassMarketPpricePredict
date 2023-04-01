from datetime import date
import os
import shutil
import time
from selenium import webdriver # Selenium Web自動操作
from selenium.webdriver.common.by import By # HTML要素の検索


def time_keeper(seconds: int):
    """ Time Keeper
    """
    time.sleep(seconds)


def get_excel():
    """ Auto Download
    """
    # Google Chrome
    driver = webdriver.Chrome()

    # 対象URLに接続
    url = 'https://www.jazmf.co.jp/market/list.html' # 全農ミートフーズ相場ページ
    driver.get(url)
    time_keeper(5) # 秒キープ
    
    # 本日日付を取得する
    today = date.today() # →datetime.date(2023, 3, 17)
    
    # class属性からターゲット要素を絞り込む
    if today.month == 4:
        # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
        target_elem = driver.find_element(By.CLASS_NAME, 'lastYear')
    else:
        target_elem = driver.find_element(By.CLASS_NAME, 'thisYear')

    target_elem = target_elem.text # →'4月\n5月\n6月\n7月\n8月\n9月\n10月\n11月\n12月\n1月\n2月\n3月'
    months = target_elem.split('\n') # →['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月']
    # 本日から見て前月の”月”を取得する
    previous_month = today.month - 1
    previous_month = str(previous_month) + "月" # →'M月'
    
    get_month = ''
    # monthsからターゲット月を取得する
    for month in months:
        if month == previous_month:
            get_month = month
            break
        continue

    # ターゲットのリンクテキスト名の要素を取得
    target_link = driver.find_element(By.LINK_TEXT, get_month)
    time_keeper(2) # 秒キープ
    
    # ターゲットリンクをクリック
    target_link.click()
    time_keeper(5) # 秒キープ
    
    # ブラウザのタブを切り替える(ページタブを切り替える)
    driver.switch_to.window(driver.window_handles[1])
    time_keeper(5) # 秒キープ
    
    # [Excel]ボタンの実行
    btn_excel = 'javascript:excelout()'
    driver.execute_script(btn_excel)
    
    time_keeper(15)
    driver.close()
    print('処理は終了しました。')


def file_move():
    """ ダウンロードファイルをワークフォルダにコピーする
    """
    download_dir = 'C:/Users/daiko/Downloads'
    file = '豚肉相場一覧表_202302.xlsx'
    download_file = os.path.join(download_dir, file)
    shutil.copy2(download_file, "download/")
