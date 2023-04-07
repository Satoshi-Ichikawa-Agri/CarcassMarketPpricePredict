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


def set_value(column, row, value):
    """ 対象セルに値をセットする
    """
    ws_summary.cell(column=column, row=row).value = value


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
    
    model_list = []
    
    # A列の日付情報を取得するとともに、モデルインスタンスを作成し、レコードの格納場所をつくる
    for row in range(1, 30):
        market_date = get_market_date(row)
        
        if is_null_or_empty(market_date):
            continue
        
        if '豚肉相場' in market_date:
            market_date = remove_value(market_date, 8, 50)
        
        model = CarcassMarketPrice()
        model.market_date = market_date
        
        # 1レコードずつリストに格納する
        model_list.append(model)
    
    
    print('データ件数: {}件'.format(len(model_list)))
    
    # セルの値を取得する
    for i, model in enumerate(model_list):
        model: CarcassMarketPrice = model
        model.index = i
        row = i + 1
        
        # 全農建値
        model.nationwide_slaughter = get_value(8, row)
        model.zennoh_high_price = get_value(3, row)
        model.zennoh_middle_price = get_value(5, row)
        
        # Tokyo
        model.tokyo_high_price = get_value(11, row)
        model.tokyo_middle_price = get_value(13, row)
        model.tokyo_ordinary_price = get_value(15, row)
        model.tokyo_outside_price = get_value(17, row)
        model.tokyo_head_count = get_value(19, row)
        
        # Saitama
        model.saitama_high_price = get_value(22, row)
        model.saitama_middle_price = get_value(24, row)
        model.saitama_ordinary_price = get_value(26, row)
        model.saitama_outside_price = get_value(28, row)
        model.saitama_head_count = get_value(30, row)
        
        # Yokohama
        model.yokohama_high_price = get_value(33, row)
        model.yokohama_middle_price = get_value(35, row)
        model.yokohama_ordinary_price = get_value(37, row)
        model.yokohama_outside_price = get_value(39, row)
        model.yokohama_head_count = get_value(41, row)
        
        # Osaka
        model.osaka_high_price = get_value(44, row)
        model.osaka_middle_price = get_value(46, row)
        model.osaka_ordinary_price = get_value(48, row)
        model.osaka_outside_price = get_value(50, row)
        model.osaka_head_count = get_value(52, row)
    
    
    for model in model_list:
        model: CarcassMarketPrice = model
        row = model.index + 3
        
        set_value(1, row, model.market_date)
        
        # 全農建値
        set_value(2, row, model.nationwide_slaughter)
        set_value(3, row, model.zennoh_high_price)
        set_value(4, row, model.zennoh_middle_price)
        
        # Tokyo
        set_value(5, row, model.tokyo_high_price)
        set_value(6, row, model.tokyo_middle_price)
        set_value(7, row, model.tokyo_ordinary_price)
        set_value(8, row, model.tokyo_outside_price)
        set_value(9, row, model.tokyo_head_count)
        
        # Saitama
        set_value(10, row, model.saitama_high_price)
        set_value(11, row, model.saitama_middle_price)
        set_value(12, row, model.saitama_ordinary_price)
        set_value(13, row, model.saitama_outside_price)
        set_value(14, row, model.saitama_head_count)
        
        # Yokohama
        set_value(15, row, model.yokohama_high_price)
        set_value(16, row, model.yokohama_middle_price)
        set_value(17, row, model.yokohama_ordinary_price)
        set_value(18, row, model.yokohama_outside_price)
        set_value(19, row, model.yokohama_head_count)
        
        # Osaka
        set_value(20, row, model.osaka_high_price)
        set_value(21, row, model.osaka_middle_price)
        set_value(22, row, model.osaka_ordinary_price)
        set_value(23, row, model.osaka_outside_price)
        set_value(24, row, model.osaka_head_count)
    
    wb_summary.save('豚枝肉相場_Summary.xlsx')
    
wb_original.close()
wb_summary.close()
