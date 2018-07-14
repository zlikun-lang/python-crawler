# Python 词云库测试
# https://amueller.github.io/word_cloud/index.html
# https://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py
import jieba as jieba
from jieba import analyse
from matplotlib import pyplot
from wordcloud import WordCloud

# 读取小说《遮天》文本内容
text = open(r'./.data/遮天.txt', 'r', encoding='utf-8').read()

# 使用 jieba 分词
# 添加自定义分词
[jieba.add_word(k) for k in ['', '']]
# 删除无用分词，这样做不是办法啊，太多了
# 另外，怎么感觉很多词还是没有删掉？！
[jieba.del_word(k) for k in ['没有', '一个', '他们', 'www.13800100',
                             '138', 'Com', '像是', '什么', '这是',
                             '一片', '看书', '首发', '化成', '而今',
                             '这个', '文字', '这样', '所有人', '若是',
                             '而后', '全部', '全都', '出手', '无比',
                             '你们', '见到', '心中', '可以', '真的',
                             '一道', '一种', '看书网', '所有', '不是',
                             '这里', '一声', '但是', '这片', '一位', '个人',
                             '浑身', '可是', '一切', '下来', '一座', '众人',
                             '字首', '一样', '怎么', '很多', '此地', '可能',
                             '那个', '就是', '出来', '', '', '',
                             '', '', '', '', '', '',
                             ]]

# 按词性分词(避免过多的形容词、副词等)
# https://www.cnblogs.com/adienhsuan/p/5674033.html
# allow_pos = ('n', 'nr', 'ns', 'nt', 'a', 'an', 'd')

# 取Top50的词生成词云
# https://github.com/fxsjy/jieba#基于-tf-idf-算法的关键词抽取
tags = analyse.extract_tags(text, topK=50, withWeight=False)
# 实测按词性分词非常慢
# tags = analyse.extract_tags(text, topK=50, withWeight=False, allowPOS=allow_pos)
print(tags)
new_text = ' '.join(tags)

# 生成词云，需要指定支持中文的字体，否则无法生成中文词云
wc = WordCloud(
    # 设置词云图片背景色，默认黑色
    # background_color='white',
    # 设置词云最大单词数
    max_words=200,
    # 设置词云中字号最大值
    # max_font_size=80,
    # 设置词云图片宽、高
    width=1024,
    height=768,
    # 设置词云文字字体(美化和解决中文乱码问题)
    font_path=r'../../assets/fonts/FZXingKai-S04S.TTF'
).generate(new_text)

# 绘图(标准长方形图)
pyplot.imshow(wc, interpolation='bilinear')
# pyplot.figure()
pyplot.axis('off')
# 直接打印图片
# pyplot.show()
# 将图片输出到文件
wc.to_file(r'./.data/wc_zhetian.png')
