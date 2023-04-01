from openpyxl import load_workbook

from models.models import CarcassMarketPrice
from const import Const


# 対象のExcelファイルを指定する
wb_original = load_workbook('download/豚肉相場一覧表_202302.xlsx')
wb_summary = load_workbook('豚枝肉相場_Summary.xlsx')
# 対象のシートを指定する
ws_original = wb_original['豚肉相場一覧表_202302']
ws_summary = wb_summary['Sheet1']


def is_null_or_empty(value):
    """指定値がNoneもしくは空でないかをチェックする
    """
    if value is None:
        return True
    if len(value) == 0:
        return True
    
    return False


def get_value(column, row):
    """ 対象セルの値を取得する
    """
    # 行と列が0未満のときは空を返す
    if column < 0 or row < 0:
        return ""
    value = str(ws_original.cell(row=row, column=column).value)
    
    if is_null_or_empty(value):
        return ""
    
    return value


def get_market_date(row):
    """取得判断フラグとして、A列の市場日付を取得する
    """
    return get_value(1, row)


def remove_value(value, start, end):
    """ 指定した範囲の文字列を削除する
    Parameters:
        value: 対象の値
        start: 開始位置
        end: 終了位置
    """
    return value[:start] + value[end + 1:]


def data_cleansing_process():
    """ データクレンジング処理
    """
    
    # for i in range(1, ws_original.max_row + 1):
    #     for j in range(1, ws_original.max_column + 1):
    #         ws_summary.cell(row=i+2,column=j).value = ws_original.cell(row=i, column=j).value
    
    model_list = []
    
    for row in range(1, 30):
        market_date = get_market_date(row)
        print(market_date)
        
        if is_null_or_empty(market_date):
            continue
        
        
        if '豚肉相場' in market_date:
            market_date = remove_value(market_date, 8, 50)
            print(market_date)
            # print('{}は日付を取得した'.format(market_date))
        
        model = CarcassMarketPrice()
        model.market_date = market_date
        
        model_list.append(model) # 1レコードずつリストに格納する
    print('データ件数: {}件'.format(len(model_list)))
    

    # for i, model in enumerate(model_list):
    #     model: CarcassMarketPrice = model
        
    #     model.market_date = STRING_EMPTY
    #     model.nationwide_slaughter = STRING_EMPTY
    #     model.zennoh_high_price = INT_UNSET
    #     model.zennoh_middle_price = INT_UNSET
        
    #     # Tokyo
    #     model.tokyo_high_price = INT_UNSET
    #     model.tokyo_middle_price = INT_UNSET
    #     model.tokyo_ordinary_price = INT_UNSET
    #     model.tokyo_outside_price = INT_UNSET
    #     model.tokyo_head_count = INT_UNSET
        
    #     # Saitama
    #     model.saitama_high_price = INT_UNSET
    #     model.saitama_middle_price = INT_UNSET
    #     model.saitama_ordinary_price = INT_UNSET
    #     model.saitama_outside_price = INT_UNSET
    #     model.saitama_head_count = INT_UNSET
        
    #     # Yokohama
    #     model.yokohama_high_price = INT_UNSET
    #     model.yokohama_middle_price = INT_UNSET
    #     model.yokohama_ordinary_price = INT_UNSET
    #     model.yokohama_outside_price = INT_UNSET
    #     model.yokohama_head_count = INT_UNSET
        
    #     # Osaka
    #     model.osaka_high_price = INT_UNSET
    #     model.osaka_middle_price = INT_UNSET
    #     model.osaka_ordinary_price = INT_UNSET
    #     model.osaka_outside_price = INT_UNSET
    #     model.osaka_head_count = INT_UNSET
