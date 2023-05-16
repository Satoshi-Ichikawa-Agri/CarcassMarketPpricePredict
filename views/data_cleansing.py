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


    def get_value(self, column, row):
        """ 対象セルの値を取得する
        """
        if column < 0 or row < 0:
            return ''
        value = str(self.ws_original.cell(row=row, column=column).value)
        
        if Const.is_null_or_empty(value):
            return ''
        
        return value


    def set_value(self, column, row, value):
        """ 対象セルに値をセットする
        """
        self.ws_summary.cell(column=column, row=row).value = self.type_conversion(value)


    def set_value_of_date(self, column, row, value):
        """ 対象セルに値をセットする(date型の値限定)
        """
        self.ws_summary.cell(column=column, row=row).value = value


    def get_market_date(self, row):
        """取得判断フラグとして、A列の市場日付を取得する
        """
        return self.get_value(1, row)


    def remove_date(self, value):
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
    
    
    def type_conversion(self, value):
        """ 型変換関数
        valueがない → str
        valueがある → int
        """
        if not Const.is_null_or_empty(value):
            value = int(value)

        return value
    
    
    def data_cleansing_process(self):
        """ データクレンジング処理 """

        model_list = []
        
        for row in range(1, 30):
            market_date = self.get_market_date(row)
            
            if '豚肉相場' in market_date:
                continue
            if Const.is_null_or_empty(market_date):
                continue
            if '全農建値' in market_date:
                break
            
            market_date = str(self.file_date) + Const.date_replace(market_date)
            model = CarcassMarketPrice()
            model.market_date = market_date
            
            model_list.append(model)
            
        print('データ件数: {}件'.format(len(model_list)))
        
        # 元データの値を取得する
        for i, model in enumerate(model_list):
            model: CarcassMarketPrice = model
            model.index = i
            row = i + 6
            
            # 全農建値
            model.zennoh_high_price = self.get_value(3, row)
            model.zennoh_middle_price = self.get_value(5, row)
            model.nationwide_slaughter = self.remove_date(self.get_value(8, row))
            # Tokyo
            model.tokyo_high_price = self.get_value(11, row)
            model.tokyo_middle_price = self.get_value(13, row)
            model.tokyo_ordinary_price = self.get_value(15, row)
            model.tokyo_outside_price = self.get_value(17, row)
            model.tokyo_head_count = self.get_value(19, row)
            # Saitama
            model.saitama_high_price = self.get_value(22, row)
            model.saitama_middle_price = self.get_value(24, row)
            model.saitama_ordinary_price = self.get_value(26, row)
            model.saitama_outside_price = self.get_value(28, row)
            model.saitama_head_count = self.get_value(30, row)
            # Yokohama
            model.yokohama_high_price = self.get_value(33, row)
            model.yokohama_middle_price = self.get_value(35, row)
            model.yokohama_ordinary_price = self.get_value(37, row)
            model.yokohama_outside_price = self.get_value(39, row)
            model.yokohama_head_count = self.get_value(41, row)
            # Osaka
            model.osaka_high_price = self.get_value(44, row)
            model.osaka_middle_price = self.get_value(46, row)
            model.osaka_ordinary_price = self.get_value(48, row)
            model.osaka_outside_price = self.get_value(50, row)
            model.osaka_head_count = self.get_value(52, row)
        
        # Summaryにセットする
        for model in model_list:
            model: CarcassMarketPrice = model
            row = model.index + 3
            
            self.set_value_of_date(1, row, Const.from_str_to_date(model.market_date))
            # 全農建値
            self.set_value(2, row, model.nationwide_slaughter)
            self.set_value(3, row, model.zennoh_high_price)
            self.set_value(4, row, model.zennoh_middle_price)
            # Tokyo
            self.set_value(5, row, model.tokyo_high_price)
            self.set_value(6, row, model.tokyo_middle_price)
            self.set_value(7, row, model.tokyo_ordinary_price)
            self.set_value(8, row, model.tokyo_outside_price)
            self.set_value(9, row, model.tokyo_head_count)
            # Saitama
            self.set_value(10, row, model.saitama_high_price)
            self.set_value(11, row, model.saitama_middle_price)
            self.set_value(12, row, model.saitama_ordinary_price)
            self.set_value(13, row, model.saitama_outside_price)
            self.set_value(14, row, model.saitama_head_count)
            # Yokohama
            self.set_value(15, row, model.yokohama_high_price)
            self.set_value(16, row, model.yokohama_middle_price)
            self.set_value(17, row, model.yokohama_ordinary_price)
            self.set_value(18, row, model.yokohama_outside_price)
            self.set_value(19, row, model.yokohama_head_count)
            # Osaka
            self.set_value(20, row, model.osaka_high_price)
            self.set_value(21, row, model.osaka_middle_price)
            self.set_value(22, row, model.osaka_ordinary_price)
            self.set_value(23, row, model.osaka_outside_price)
            self.set_value(24, row, model.osaka_head_count)
        
        self.wb_summary.save('豚枝肉相場_Summary.xlsx')
        
        self.wb_original.close()
        self.wb_summary.close()
