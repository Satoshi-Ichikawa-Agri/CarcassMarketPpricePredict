from CarcassMarketPpricePredict.constant import Const
from models.models import CarcassMarketPrice, create_table
from settings import DbSetting
from views.excel_operation import ExcelOperation


class DbInsert(object):
    def insert_carcass(self):
        """carcassテーブルにsummaryをinsert"""

        excel = ExcelOperation()

        wb_summary, ws_summary = excel.read_excel(
            Const.get_summary_file(), Const.SUMMARY_FILE_SHEET_NAME
        )

        # DB接続
        db_setting = DbSetting()
        session = db_setting.get_db_session()

        engine = create_table()

        # Summaryからデータを取得する
        for row in range(3, ws_summary.max_row + 1):
            market_date = excel.get_cell_value(ws_summary, row, 1)

            if Const.is_null_or_empty(market_date):
                break

            # 全農値
            nationwide_slaughter = excel.get_cell_value(ws_summary, row, 2)
            zennoh_high_price = excel.get_cell_value(ws_summary, row, 3)
            zennoh_middle_price = excel.get_cell_value(ws_summary, row, 4)
            # Tokyo
            tokyo_high_price = excel.get_cell_value(ws_summary, row, 5)
            tokyo_middle_price = excel.get_cell_value(ws_summary, row, 6)
            tokyo_ordinary_price = excel.get_cell_value(ws_summary, row, 7)
            tokyo_outside_price = excel.get_cell_value(ws_summary, row, 8)
            tokyo_head_count = excel.get_cell_value(ws_summary, row, 9)
            # Saitama
            saitama_high_price = excel.get_cell_value(ws_summary, row, 10)
            saitama_middle_price = excel.get_cell_value(ws_summary, row, 11)
            saitama_ordinary_price = excel.get_cell_value(ws_summary, row, 12)
            saitama_outside_price = excel.get_cell_value(ws_summary, row, 13)
            saitama_head_count = excel.get_cell_value(ws_summary, row, 14)
            # Yokohama
            yokohama_high_price = excel.get_cell_value(ws_summary, row, 15)
            yokohama_middle_price = excel.get_cell_value(ws_summary, row, 16)
            yokohama_ordinary_price = excel.get_cell_value(ws_summary, row, 17)
            yokohama_outside_price = excel.get_cell_value(ws_summary, row, 18)
            yokohama_head_count = excel.get_cell_value(ws_summary, row, 19)
            # Osaka
            osaka_high_price = excel.get_cell_value(ws_summary, row, 20)
            osaka_middle_price = excel.get_cell_value(ws_summary, row, 21)
            osaka_ordinary_price = excel.get_cell_value(ws_summary, row, 22)
            osaka_outside_price = excel.get_cell_value(ws_summary, row, 23)
            osaka_head_count = excel.get_cell_value(ws_summary, row, 24)

            model = CarcassMarketPrice(
                market_date=market_date,
                nationwide_slaughter=nationwide_slaughter,
                zennoh_high_price=zennoh_high_price,
                zennoh_middle_price=zennoh_middle_price,
                tokyo_high_price=tokyo_high_price,
                tokyo_middle_price=tokyo_middle_price,
                tokyo_ordinary_price=tokyo_ordinary_price,
                tokyo_outside_price=tokyo_outside_price,
                tokyo_head_count=tokyo_head_count,
                saitama_high_price=saitama_high_price,
                saitama_middle_price=saitama_middle_price,
                saitama_ordinary_price=saitama_ordinary_price,
                saitama_outside_price=saitama_outside_price,
                saitama_head_count=saitama_head_count,
                yokohama_high_price=yokohama_high_price,
                yokohama_middle_price=yokohama_middle_price,
                yokohama_ordinary_price=yokohama_ordinary_price,
                yokohama_outside_price=yokohama_outside_price,
                yokohama_head_count=yokohama_head_count,
                osaka_high_price=osaka_high_price,
                osaka_middle_price=osaka_middle_price,
                osaka_ordinary_price=osaka_ordinary_price,
                osaka_outside_price=osaka_outside_price,
                osaka_head_count=osaka_head_count,
            )

            session.add(model)
        session.commit()

        print("summaryのDBインサートが完了しました。")

        # 処理終了後にsummaryの値がある行を削除する
        for row in ws_summary.iter_rows(min_row=3):
            for cell in row:
                cell.value = None

        wb_summary.save(Const.get_summary_file())
        wb_summary.close()

        # DBと切断
        session.close()

        # エンジン破棄
        db_setting.dispose_db_engine(engine)
