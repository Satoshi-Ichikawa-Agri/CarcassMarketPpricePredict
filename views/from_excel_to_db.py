import csv
import MySQLdb
import openpyxl
from openpyxl import load_workbook

from const import Const


def process():
    pass



""" ここからはDB操作 """
# db = MySQLdb.connect(
#     database='dev_carcass_db',
#     user='root',
#     password='Asagakita40813011',
#     host='localhost',
#     port=3306
#     )

# cursor = db.cursor()

# create_table_query = """ CREATE TABLE IF NOT EXISTS carcass_market_price (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     market_date DATE NOT NULL,
#     nationwide_slaughter INT,
#     zennoh_high_price INT,
#     zennoh_middle_price INT,
#     tokyo_high_price INT,
#     tokyo_middle_price INT,
#     tokyo_ordinary_price INT,
#     tokyo_outside_price INT,
#     tokyo_head_count INT,
#     saitama_high_price INT,
#     saitama_middle_price INT,
#     saitama_ordinary_price INT,
#     saitama_outside_price INT,
#     saitama_head_count INT,
#     yokohama_high_price INT,
#     yokohama_middle_price INT,
#     yokohama_ordinary_price INT,
#     yokohama_outside_price INT,
#     yokohama_head_count INT,
#     osaka_high_price INT,
#     osaka_middle_price INT,
#     osaka_ordinary_price INT,
#     osaka_outside_price INT,
#     osaka_head_count INT
#     );"""

# cursor.execute(create_table_query)

# cursor.close()
# db.close()
