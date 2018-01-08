from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator

#获取当前文件路径
dangQian = path.dirname(__file__)

# stopWords = {}
isCN = 1    #默认为中文分词
backColoringPath = '56841af526e6e.jpg'   #设置背景图片路径
textPath = 'xinWen.txt'       #要分析的文本路径
fontPath = 'HYTieXianHei-75J.ttf'       #为matplotlib设置中文字体路径
stopWordsPath = 'stopwords1893.txt'      #停用词词表路径
imgName1 = 'xww1.png'       #只按背景图片形状生成的图片名
imgName2 = 'xww2.png'       #按背景图片颜色、形状生成的图片名

myWordList = ['',]       #在结巴词库中添加新词

backColoring = imread(path.join(dangQian, backColoringPath))    #设置背景图

#设置词云属性
cY = WordCloud(
    font_path= fontPath,
    background_color= "white",
    max_words= 2000,     #词韵最大显示词数
    mask= backColoring,      #设置背景图片
    max_font_size= 100,     #字体最大值
    width=1000, height=860,     # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存
    margin=2,   #margin为词语边缘距离
)

#添加自己的词库分词
def addWord(alist):
    for itmes in alist:
        jieba.add_word(itmes)

addWord(myWordList)

text = open(path.join(dangQian, textPath)).read()

def jiebaClearText(text):

    myWordList2 = []
    segList = jieba.cut(text, cut_all= False)
    listStr = '/'.join(segList)
    fStop = open(stopWordsPath)
    try:
        fStopText = fStop.read()
        # fStopText = unicode(fStopText, 'utf-8')

    finally:
        fStop.close()

    fStopSegList = fStopText.split('\n')
    for myWord in listStr.split('/'):
        if not(myWord.strip() in fStopSegList and len(myWord.strip())) > 1:
            myWordList2.append(myWord)
    return ''.join(myWordList2)

if isCN:
    text = jiebaClearText(text)

# 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
cY.generate(text)

#从背景图片生成颜色值
imageColors = ImageColorGenerator(backColoring)

#绘制词云
plt.figure()
plt.imshow(cY)
plt.axis("off")
plt.show()

#保存图片
cY.to_file(path.join(dangQian, imgName1))

imageColors = ImageColorGenerator(backColoring)

plt.imshow(cY.recolor(color_func= imageColors))
plt.axis("off")

#绘制背景图片为颜色图片
plt.figure()
plt.imshow(backColoring, cmap= plt.cm.gray)
plt.axis('off')
plt.show()

#保存图片
cY.to_file(path.join(dangQian, imgName2))
