import jieba
import jieba.analyse as analyse

#分词
def stripdata(Test):
    # jieba 默认启用了HMM（隐马尔科夫模型）进行中文分词
    seg_list = jieba.cut(Test,cut_all=True)  # 分词
    #获取字典，去除停用词
    line = "/".join(seg_list)
    word = stripword(line)
    #print(line)
    #列出关键字
    return word

#停用词分析
def stripword(seg):
    wordlist = []
    #获取停用词表
    stop = open('中文停用词表.txt', 'r+', encoding='utf-8')
    stopword = stop.read().split("\n")+["。'","!'", "！'","；'","，'",'景区','不错','一定','世界','特别','很多','风景','得以','真的',
                                        '特别','不到','没有','比较','非常','一个','值得','景色','推荐','太多','住宿','随便','一次','有点',
                                        '位于','里面',"。。'","。。。'","！！！'","！！'",'一座','游玩','项目','看到','小时','分钟','景点',
                                        '喜欢','今天','——','明天','后天','感觉','下次',"'【","'】","】'",'一条','一天',"～'","？'",", '",
                                        '地方','不多','需要','一下','旅游','》，',"……'",'一下',"、'",'”，',"~'",'一点','一片','一起',"～～'"]
    #遍历分词表
    for key in seg.split('/'):
        #print(key)
        #去除停用词，去除单字，去除重复词
        if not(key.strip() in stopword) and (len(key.strip()) > 1) and not(key.strip() in wordlist) :
            wordlist.append(key)
    # print(wordlist)
    #停用词去除END
    stop.close()
    return wordlist

def creat(text):
    # Rawdata = open('text.txt','r+',encoding='utf-8')
    # text = Rawdata.read()
    #调用分词
    # print(text)
    # keywords =analyse.textrank(text, topK=20)
    # print(keywords)
    wordlist=stripdata(text)
    #END
    # Rawdata.close()
    return wordlist