from CarcassMarketPpricePredict.constant import Const
from models.models import CarcassMarketPriceExcel
from views.excel_operation import ExcelOperation


class DataCleansing(object):
    """Data Cleansing"""

    def __init__(self, file_date):
        self.file_date = file_date

    def data_cleansing_process(self):
        """Data Cleansing"""

        excel = ExcelOperation()

        # ダウンロードファイルのOpen(豚枝肉相場一覧)
        wb_original, ws_original = excel.read_excel(
            Const.get_downloaded_file(self.file_date),
            f"豚肉相場一覧表_{ self.file_date }",
        )

        # SummaryファイルのOpen
        wb_summary, ws_summary = excel.read_excel(
            Const.get_summary_file(), Const.SUMMARY_FILE_SHEET_NAME
        )

        model_list = []

        for row in range(1, 30):
            market_date = excel.get_market_date(ws_original, row)

            if "豚肉相場" in market_date:
                continue
            if Const.is_null_or_empty(market_date):
                continue
            if "全農建値" in market_date:
                break

            market_date = str(self.file_date) + Const.date_replace(market_date)
            model = CarcassMarketPriceExcel()
            model.market_date = market_date

            model_list.append(model)

        print("データ件数: {}件".format(len(model_list)))

        # 元データの値を取得する
        for i, model in enumerate(model_list):
            model: CarcassMarketPriceExcel = model
            model.index = i
            row = i + 6

            # 全農建値
            model.zennoh_high_price = excel.get_cell_value(ws_original, row, 3)
            model.zennoh_middle_price = excel.get_cell_value(
                ws_original, row, 5
            )
            model.nationwide_slaughter = excel.remove_date(
                excel.get_cell_value(ws_original, row, 8)
            )
            # Tokyo
            model.tokyo_high_price = excel.get_cell_value(ws_original, row, 11)
            model.tokyo_middle_price = excel.get_cell_value(
                ws_original, row, 13
            )
            model.tokyo_ordinary_price = excel.get_cell_value(
                ws_original, row, 15
            )
            model.tokyo_outside_price = excel.get_cell_value(
                ws_original, row, 17
            )
            model.tokyo_head_count = excel.get_cell_value(ws_original, row, 19)
            # Saitama
            model.saitama_high_price = excel.get_cell_value(
                ws_original, row, 22
            )
            model.saitama_middle_price = excel.get_cell_value(
                ws_original, row, 24
            )
            model.saitama_ordinary_price = excel.get_cell_value(
                ws_original, row, 26
            )
            model.saitama_outside_price = excel.get_cell_value(
                ws_original, row, 28
            )
            model.saitama_head_count = excel.get_cell_value(
                ws_original, row, 30
            )
            # Yokohama
            model.yokohama_high_price = excel.get_cell_value(
                ws_original, row, 33
            )
            model.yokohama_middle_price = excel.get_cell_value(
                ws_original, row, 35
            )
            model.yokohama_ordinary_price = excel.get_cell_value(
                ws_original, row, 37
            )
            model.yokohama_outside_price = excel.get_cell_value(
                ws_original, row, 39
            )
            model.yokohama_head_count = excel.get_cell_value(
                ws_original, row, 41
            )
            # Osaka
            model.osaka_high_price = excel.get_cell_value(ws_original, row, 44)
            model.osaka_middle_price = excel.get_cell_value(
                ws_original, row, 46
            )
            model.osaka_ordinary_price = excel.get_cell_value(
                ws_original, row, 48
            )
            model.osaka_outside_price = excel.get_cell_value(
                ws_original, row, 50
            )
            model.osaka_head_count = excel.get_cell_value(ws_original, row, 52)

        # Summaryにセットする
        for model in model_list:
            model: CarcassMarketPriceExcel = model
            row = model.index + 3

            excel.set_value_of_date(
                ws_summary, row, 1, Const.from_str_to_date(model.market_date)
            )
            # 全農建値
            excel.set_value_type_converted(
                ws_summary, row, 2, model.nationwide_slaughter
            )
            excel.set_value_type_converted(
                ws_summary, row, 3, model.zennoh_high_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 4, model.zennoh_middle_price
            )
            # Tokyo
            excel.set_value_type_converted(
                ws_summary, row, 5, model.tokyo_high_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 6, model.tokyo_middle_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 7, model.tokyo_ordinary_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 8, model.tokyo_outside_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 9, model.tokyo_head_count
            )
            # Saitama
            excel.set_value_type_converted(
                ws_summary, row, 10, model.saitama_high_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 11, model.saitama_middle_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 12, model.saitama_ordinary_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 13, model.saitama_outside_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 14, model.saitama_head_count
            )
            # Yokohama
            excel.set_value_type_converted(
                ws_summary, row, 15, model.yokohama_high_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 16, model.yokohama_middle_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 17, model.yokohama_ordinary_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 18, model.yokohama_outside_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 19, model.yokohama_head_count
            )
            # Osaka
            excel.set_value_type_converted(
                ws_summary, row, 20, model.osaka_high_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 21, model.osaka_middle_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 22, model.osaka_ordinary_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 23, model.osaka_outside_price
            )
            excel.set_value_type_converted(
                ws_summary, row, 24, model.osaka_head_count
            )

        # Summaryファイル自体を上書き保存(後のDBINSERT終了後に削除処理がある)
        excel.save_excel(wb_summary, Const.get_summary_file())

        # 名前を付けて保存(Summaryの退避)
        excel.save_and_close_excel(
            wb_summary,
            Const.make_document_path(
                Const.get_project_store_output_directory(),
                f"豚枝肉相場_Summary{ self.file_date }.xlsx",
            ),
            True,
        )

        # ダウンロードファイルは不要の為、Close
        excel.save_and_close_excel(wb_original)

        del excel
