import jiagu
import jieba.analyse


def seg_txt(txt):
    return ' '.join(jieba.analyse.textrank(txt))


def main():
    fp = open("data/itemName.txt", encoding="utf8")
    fs = open("data/itemName_seg.txt", encoding="utf8", mode="a")
    g = map(seg_txt, fp.readlines())
    for i in g:
        if len(i.strip()) > 0:
            print(f"success insert {i} into txt")
            fs.write(i + '\n')


if __name__ == '__main__':
    main()
