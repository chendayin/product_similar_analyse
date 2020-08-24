from gensim.models import Word2Vec
import jieba.analyse


def load_model(path):
    w2v = Word2Vec.load(path)
    return w2v


def main():
    w2v = load_model("model/itemProduct.w2v")
    txt = jieba.analyse.textrank("慈风阁 五帝钱真品开光古铜钱纯铜古币风水镇宅招财化煞葫芦挂件")
    print(txt)
    print(w2v.wv.most_similar(txt[1], topn=10))


if __name__ == '__main__':
    main()
