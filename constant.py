"""共通利用の定数と関数"""
from pathlib import Path
import shutil
import time
from datetime import date, datetime


class Const(object):
    INT_UNSET = -1
    STRING_UNSET = ""

    SUMMARY_FILE_NAME = "summary.xlsx"
    SUMMARY_FILE_SHEET_NAME = "summary"

    WINDOWS_DOWNLOAS_DIR = "C:\\Users\\daiko\\Downloads"
    PROJECT_STORE_PATH = (
        "C:\\Users\\daiko\\Data_Store\\carcass_market_price_predict_store"
    )

    ZENNO_URL = "https://www.jazmf.co.jp/market/list.html"

    YEAR_MONTHS = ("4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月")
    LAST_YEAR_MONTHS = ("1月", "2月", "3月")

    DATE_NOW = datetime.now().strftime("%Y/%m/%d_%H:%M:%S")  # 本日日時
    TODAY = date.today()  # 本日日付(2023, 4, 12)
    DATE_TODAY = date.today().strftime("%Y/%m/%d")  # 本日日付("2023/04/12")
    DATE_YEAR_AND_MONTH = date.today().strftime("%Y%m")  # 当月("202304")

    @classmethod
    def get_home_directory(cls) -> Path:
        """Get HOME directory

        Args:
            value (str): Noneもしくは空であるかを確認する値
        Returns:
            bool: (例: Noneや空の場合はTrue、値が存在すればFalse)
        """
        return Path.home()

    @classmethod
    def get_current_directory(cls) -> Path:
        """Get CURRENT directory"""
        return Path.cwd()

    @classmethod
    def get_project_directory(cls) -> Path:
        """Get Project directory"""
        return cls.get_current_directory()

    @classmethod
    def get_project_store_directory(cls) -> Path:
        """Get Project Store directory"""
        project_store_path = Path(cls.PROJECT_STORE_PATH)

        return project_store_path

    @classmethod
    def get_project_store_download_directory(cls) -> Path:
        """Get download directory"""
        download_path = cls.get_project_store_directory().joinpath("download")

        return download_path

    @classmethod
    def get_project_store_output_directory(cls) -> Path:
        """Get output directory"""
        output_path = cls.get_project_store_directory().joinpath(
            "output_samary"
        )

        return output_path

    @classmethod
    def make_document_path(cls, dir, file_name: str) -> str:
        """Make Docs path"""
        dir_str = str(dir)
        doc_path = Path(dir_str).joinpath(file_name)

        return str(doc_path)

    @classmethod
    def get_summary_file(cls) -> str:
        """get summary file"""
        sammary_file = cls.get_current_directory().joinpath(
            cls.SUMMARY_FILE_NAME
        )

        return str(sammary_file)

    @classmethod
    def get_downloaded_file(cls, file_date) -> str:
        """get downloaded file"""
        download_file = cls.get_project_store_download_directory().joinpath(
            f"豚肉相場一覧表_{ file_date }.xlsx"
        )

        return str(download_file)

    @classmethod
    def check_target_date(cls, arg_list):
        """Consoleの引数からtarget_dateを取得する
        python main.py 202303
        """
        if len(arg_list) == 1:
            target_date = None
        else:
            target_date = arg_list[1]

        return target_date

    @classmethod
    def is_null_or_empty(cls, value):
        """Noneや空の判定"""
        if value is None:
            return True
        if value == "None":
            return True
        if value == "" or len(value) == 0:
            return True

        return False

    @classmethod
    def date_replace(cls, value: str):
        """日付のReplace
        Parameters:
            value: ダウンロードA列の「日」の値(例01日,02日)
        """
        value_trance = value.replace("日", "")  # 01~31

        return value_trance

    @classmethod
    def from_str_to_date(cls, value: str):
        """日付の型変換(str → date)"""
        date_date = date.fromisoformat(value)

        return date_date

    @classmethod
    def remove_value(cls, value, start, end):
        """指定した範囲の文字列を削除する
        Parameters:
            value: 対象の値
            start: 開始位置
            end: 終了位置
        """
        return value[:start] + value[end + 1 :]

    @classmethod
    def time_keeper(cls, seconds: int):
        """Time Keeper"""
        time.sleep(seconds)

    @classmethod
    def file_copy(cls, original_file, copy_to):
        """File Copy"""
        shutil.copy2(original_file, copy_to)
