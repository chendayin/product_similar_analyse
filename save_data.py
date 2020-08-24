import pandas as pd
from sqlalchemy import create_engine

INFO = {'user': 'wst_cfg',
        'password': '5560203@Wst',
        'host': '192.168.1.114',
        'port': 3306,
        'database': 'taobao_live'
        }

ENGINE = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s' % INFO)


def read_chuck(size=1024):
    sql = "SELECT itemName FROM source_taobao_live_product_now_new_20200824 GROUP BY itemId"
    g = pd.read_sql(sql, ENGINE, chunksize=size)
    return g


def save_txt(txt: pd.DataFrame):
    txt.to_csv("data/itemName.txt", encoding="utf8", mode="a", header=None, index=None)
    print("success insert txt ")


def main():
    for itemName in read_chuck():
        save_txt(itemName)


if __name__ == '__main__':
    main()
