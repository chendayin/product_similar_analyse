import time

from Mysql_pool_utils import MyPoolDB
from gensim.models import Word2Vec
import multiprocessing
import jieba.analyse

DB_POOL = MyPoolDB(host="192.168.1.114", user="wst_cfg", password="5560203@Wst", db_base="taobao_live", max_num=20)
W2V_PATH = "model/itemProduct.w2v"
MODEL = Word2Vec.load(W2V_PATH)


def process(itemId, itemName, db, cursor):
    top2 = jieba.analyse.textrank(itemName)[:2]
    try:
        rank1 = MODEL.wv.most_similar(top2[0])[0][0]
    except:
        rank1 = ''
    try:
        rank2 = MODEL.wv.most_similar(top2[1])[0][0]
    except:
        rank2 = ''

    sql = """
        REPLACE INTO taobao_goods_title_topn VALUES ({},'{}','{}')
    """.format(itemId, itemName, rank1 + ',' + rank2)
    try:
        cursor.execute(sql)
        db.commit()
        print(f"success insert into record  {itemName}----{top2}")
    except:
        pass


def root(i, value):
    db = DB_POOL.get_connect()
    while True:
        sql = """
            SELECT itemId,itemName FROM source_taobao_live_product_now_new_20200824 GROUP BY itemId LIMIT {},1000
        """.format(i * 5 + value.value)
        cursor = db.cursor()
        cursor.execute(sql)
        for lst in cursor.fetchall():
            process(lst[0], lst[1], db, cursor)
        value.value += 1000


def main():
    value = multiprocessing.Value("i", 0)
    jobs = [multiprocessing.Process(target=root, args=(i, value)) for i in range(5)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
