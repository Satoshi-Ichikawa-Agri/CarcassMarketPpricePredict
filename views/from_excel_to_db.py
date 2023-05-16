import MySQLdb
from openpyxl import load_workbook


class DbInsert(object):
    """"""
    
    def insert_carcass(self):
        """ carcassテーブルにsummaryをinsert """

        wb_summary = load_workbook('豚枝肉相場_Summary.xlsx')
        ws_summary = wb_summary['Sheet1']
        
        # DBに接続
        db = MySQLdb.connect(
            database='dev_carcass_db',
            user='root',
            password='Asagakita40813011',
            host='localhost',
            port=3306
        )
        
        # table create
        create_table_query = """ CREATE TABLE IF NOT EXISTS carcass_market_price (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            market_date DATE NOT NULL,
            nationwide_slaughter INT,
            zennoh_high_price INT,
            zennoh_middle_price INT,
            tokyo_high_price INT,
            tokyo_middle_price INT,
            tokyo_ordinary_price INT,
            tokyo_outside_price INT,
            tokyo_head_count INT,
            saitama_high_price INT,
            saitama_middle_price INT,
            saitama_ordinary_price INT,
            saitama_outside_price INT,
            saitama_head_count INT,
            yokohama_high_price INT,
            yokohama_middle_price INT,
            yokohama_ordinary_price INT,
            yokohama_outside_price INT,
            yokohama_head_count INT,
            osaka_high_price INT,
            osaka_middle_price INT,
            osaka_ordinary_price INT,
            osaka_outside_price INT,
            osaka_head_count INT
            );"""
        
        cursor = db.cursor()
        
        cursor.execute(create_table_query)
        db.commit()

        # Summaryからデータを取得する
        for row in range(3, ws_summary.max_row + 1):
            market_date = ws_summary.cell(row, 1).value
            if market_date == None or market_date == 'None':
                break
            
            # 全農値
            nationwide_slaughter = ws_summary.cell(row, 2).value
            zennoh_high_price = ws_summary.cell(row, 3).value
            zennoh_middle_price = ws_summary.cell(row, 4).value
            # Tokyo
            tokyo_high_price = ws_summary.cell(row, 5).value
            tokyo_middle_price = ws_summary.cell(row, 6).value
            tokyo_ordinary_price = ws_summary.cell(row, 7).value
            tokyo_outside_price = ws_summary.cell(row, 8).value
            tokyo_head_count = ws_summary.cell(row, 9).value
            # Saitama
            saitama_high_price = ws_summary.cell(row, 10).value
            saitama_middle_price = ws_summary.cell(row, 11).value
            saitama_ordinary_price = ws_summary.cell(row, 12).value
            saitama_outside_price = ws_summary.cell(row, 13).value
            saitama_head_count = ws_summary.cell(row, 14).value
            # Yokohama
            yokohama_high_price = ws_summary.cell(row, 15).value
            yokohama_middle_price = ws_summary.cell(row, 16).value
            yokohama_ordinary_price = ws_summary.cell(row, 17).value
            yokohama_outside_price = ws_summary.cell(row, 18).value
            yokohama_head_count = ws_summary.cell(row, 19).value
            # Osaka
            osaka_high_price = ws_summary.cell(row, 20).value
            osaka_middle_price = ws_summary.cell(row, 21).value
            osaka_ordinary_price = ws_summary.cell(row, 22).value
            osaka_outside_price = ws_summary.cell(row, 23).value
            osaka_head_count = ws_summary.cell(row, 24).value
        
        
            insert_query = """ INSERT INTO carcass_market_price (
                market_date,
                nationwide_slaughter,
                zennoh_high_price,
                zennoh_middle_price,
                tokyo_high_price,
                tokyo_middle_price,
                tokyo_ordinary_price,
                tokyo_outside_price,
                tokyo_head_count,
                saitama_high_price,
                saitama_middle_price,
                saitama_ordinary_price,
                saitama_outside_price,
                saitama_head_count,
                yokohama_high_price,
                yokohama_middle_price,
                yokohama_ordinary_price,
                yokohama_outside_price,
                yokohama_head_count,
                osaka_high_price,
                osaka_middle_price,
                osaka_ordinary_price,
                osaka_outside_price,
                osaka_head_count
                ) VALUE (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                );"""
            
            data = [
                market_date,
                nationwide_slaughter,
                zennoh_high_price,
                zennoh_middle_price,
                tokyo_high_price,
                tokyo_middle_price,
                tokyo_ordinary_price,
                tokyo_outside_price,
                tokyo_head_count,
                saitama_high_price,
                saitama_middle_price,
                saitama_ordinary_price,
                saitama_outside_price,
                saitama_head_count,
                yokohama_high_price,
                yokohama_middle_price,
                yokohama_ordinary_price,
                yokohama_outside_price,
                yokohama_head_count,
                osaka_high_price,
                osaka_middle_price,
                osaka_ordinary_price,
                osaka_outside_price,
                osaka_head_count
            ]
        
            cursor.execute(insert_query, data)
            db.commit()
            print('INSERTが成功した。')

        cursor.close()
        db.close()
        print('summaryのDBインサートが完了しました。')


        # 処理終了後にsummaryの値がある行を削除する
        for row in ws_summary.iter_rows(min_row=3):
            for cell in row:
                cell.value = None

        wb_summary.save('豚枝肉相場_Summary.xlsx')
        wb_summary.close()
