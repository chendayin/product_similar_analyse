import gensim
from gensim.models import word2vec


def main():
    sentence = word2vec.Text8Corpus("data/itemName_seg.txt")
    model = gensim.models.Word2Vec(sentence, sg=1, size=200, window=5, min_count=0, negative=3, sample=0.001, hs=1,
                                   workers=6)

    model.save("model/itemProduct.w2v")
    print(f"success save model")


if __name__ == '__main__':
    main()
