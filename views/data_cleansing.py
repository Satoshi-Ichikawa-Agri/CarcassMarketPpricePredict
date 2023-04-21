import re
from openpyxl import load_workbook

from models.models import CarcassMarketPrice
from const import Const


class DataCleansing(object):
    
    def __init__(self, file_date):
        self.file_date = file_date
        
        # 対象のExcelファイルを指定する
        self.wb_original = load_workbook(f'download/豚肉相場一覧表_{ self.file_date }.xlsx')
        self.wb_summary = load_workbook('豚枝肉相場_Summary.xlsx')
        # 対象のシートを指定する
        self.ws_original = self.wb_original[f'豚肉相場一覧表_{ self.file_date }']
        self.ws_summary = self.wb_summary['Sheet1']


    def data_cleansing_process(self):
        """ データクレンジング処理
        """

        model_list = []
        
        # A列の日付情報を取得するとともに、モデルインスタンスを作成し、レコードの格納場所をつくる
        for row in range(1, 30):
            market_date = self.__get_market_date(row)
            
            if '豚肉相場' in market_date:
                get_file_market_date = self.__remove_value(market_date, 8, 50)
                continue
            if '全農建値' in market_date:
                continue
            if Const.is_null_or_empty(market_date):
                continue
            market_date = self.file_date + Const.date_replace(market_date)
            model = CarcassMarketPrice()
            model.market_date = market_date
            
            # 1レコードずつリストに格納する
            model_list.append(model)

        print('データ件数: {}件'.format(len(model_list)))
        
        # 枝肉データの値を取得する
        for i, model in enumerate(model_list):
            model: CarcassMarketPrice = model
            
            model.index = i
            row = i + 6
            
            # 全農建値
            model.zennoh_high_price = self.__get_value(3, row)
            model.zennoh_middle_price = self.__get_value(5, row)
            model.nationwide_slaughter = self.__remove_date(self.__get_value(8, row))
            
            # Tokyo
            model.tokyo_high_price = self.__get_value(11, row)
            model.tokyo_middle_price = self.__get_value(13, row)
            model.tokyo_ordinary_price = self.__get_value(15, row)
            model.tokyo_outside_price = self.__get_value(17, row)
            model.tokyo_head_count = self.__get_value(19, row)
            
            # Saitama
            model.saitama_high_price = self.__get_value(22, row)
            model.saitama_middle_price = self.__get_value(24, row)
            model.saitama_ordinary_price = self.__get_value(26, row)
            model.saitama_outside_price = self.__get_value(28, row)
            model.saitama_head_count = self.__get_value(30, row)
            
            # Yokohama
            model.yokohama_high_price = self.__get_value(33, row)
            model.yokohama_middle_price = self.__get_value(35, row)
            model.yokohama_ordinary_price = self.__get_value(37, row)
            model.yokohama_outside_price = self.__get_value(39, row)
            model.yokohama_head_count = self.__get_value(41, row)
            
            # Osaka
            model.osaka_high_price = self.__get_value(44, row)
            model.osaka_middle_price = self.__get_value(46, row)
            model.osaka_ordinary_price = self.__get_value(48, row)
            model.osaka_outside_price = self.__get_value(50, row)
            model.osaka_head_count = self.__get_value(52, row)
        
        
        for model in model_list:
            model: CarcassMarketPrice = model
            
            row = model.index + 3
            
            self.__set_value_of_date(1, row, Const.from_str_to_date(model.market_date))
            
            # 全農建値
            self.__set_value(2, row, model.nationwide_slaughter)
            self.__set_value(3, row, model.zennoh_high_price)
            self.__set_value(4, row, model.zennoh_middle_price)
            
            # Tokyo
            self.__set_value(5, row, model.tokyo_high_price)
            self.__set_value(6, row, model.tokyo_middle_price)
            self.__set_value(7, row, model.tokyo_ordinary_price)
            self.__set_value(8, row, model.tokyo_outside_price)
            self.__set_value(9, row, model.tokyo_head_count)
            
            # Saitama
            self.__set_value(10, row, model.saitama_high_price)
            self.__set_value(11, row, model.saitama_middle_price)
            self.__set_value(12, row, model.saitama_ordinary_price)
            self.__set_value(13, row, model.saitama_outside_price)
            self.__set_value(14, row, model.saitama_head_count)
            
            # Yokohama
            self.__set_value(15, row, model.yokohama_high_price)
            self.__set_value(16, row, model.yokohama_middle_price)
            self.__set_value(17, row, model.yokohama_ordinary_price)
            self.__set_value(18, row, model.yokohama_outside_price)
            self.__set_value(19, row, model.yokohama_head_count)
            
            # Osaka
            self.__set_value(20, row, model.osaka_high_price)
            self.__set_value(21, row, model.osaka_middle_price)
            self.__set_value(22, row, model.osaka_ordinary_price)
            self.__set_value(23, row, model.osaka_outside_price)
            self.__set_value(24, row, model.osaka_head_count)
        
        self.wb_summary.save('豚枝肉相場_Summary.xlsx')
        
        self.wb_original.close()
        self.wb_summary.close()


    def __get_value(self, column, row):
        """ 対象セルの値を取得する
        """
        # 行と列が0未満のときは空を返す
        if column < 0 or row < 0:
            return ''
        value = str(self.ws_original.cell(row=row, column=column).value)
        
        if Const.is_null_or_empty(value):
            return ''
        
        return value


    def __set_value(self, column, row, value):
        """ 対象セルに値をセットする
        """
        self.ws_summary.cell(column=column, row=row).value = self.__type_conversion(value)


    def __set_value_of_date(self, column, row, value):
        """ 対象セルに値をセットする(date型の値限定)
        """
        self.ws_summary.cell(column=column, row=row).value = value


    def __get_market_date(self, row):
        """取得判断フラグとして、A列の市場日付を取得する
        """
        return self.__get_value(1, row)


    def __remove_value(self, value, start, end):
        """ 指定した範囲の文字列を削除する
        Parameters:
            value: 対象の値
            start: 開始位置
            end: 終了位置
        """
        return value[:start] + value[end + 1:]
    
    
    def __remove_date(self, value):
        """ 豚肉相場一覧表_yyyymm.xlsxの「全国と畜頭数」列の値が
        数値と日付の情報となっているので、日付を削除する処理
        変更前: 68800 (2023/02/28)
        変更後: 68800
        """
        # 正規表現
        regex = r'\(\d{4}/\d{1,2}/\d{1,2}\)'
        # 正規表現で示して値だけ削除し、さらに空白を削除する
        removed_value = str.strip(re.sub(regex, '', value))
        
        return removed_value
    
    
    def __type_conversion(self, value):
        """ 型変換関数
        valueがない → str
        valueがある → int
        """
        if not Const.is_null_or_empty(value):
            value = int(value)

        return value
