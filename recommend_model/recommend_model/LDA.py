import matplotlib
import pymysql
from gensim import corpora, models
import gensim
from gensim.models import LdaModel, CoherenceModel
import matplotlib as plt
from jieba import analyse

from jieba_code import creat
# 创建连接对象
def connect_mysql():
    tourist_mysql()
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='111111', database='crawler', charset='utf8')
    # 查询 SQL 语句
    tourist_list = tourist_mysql()
    for tourist_word in tourist_list:
        cursor= conn.cursor()
        sql1 = "select comment from commentlist where viewId=" + str(tourist_word)+";"
        # 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数
        row_count = cursor.execute(sql1)
        # print("SQL 语句执行影响的行数%d" % row_count)
        # 取出结果集中一行数据
        # print(cursor.fetchone())
        doc_ = []
        for line in cursor.fetchall():
            # print(line)
            # 获取单个字段的值
            # print(line[0])
            doc_.append(str(line[0]))
            # print("pos的值" + line[0])
        # print(doc_)
        cursor.scroll(0,mode='absolute')
        ans_ = LDA_code(doc_)
        #插入到表中
        sql2 = "UPDATE preinfolabel SET theme1='"+ans_[0]+"',theme2='"+ans_[1]+"',theme3='"+ans_[2]+"',theme4='"+ans_[3]+"',theme5='"+ans_[4]+"',theme6='"+ans_[5]+"' where id="+str(tourist_word)+";"
        print(sql2)
        cursor.execute(sql2)
        print("insert success")
        cursor.close()
        conn.commit()
    # 关闭连接
    conn.close()


def tourist_mysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='111111', database='crawler',
                           charset='utf8')
    # 获取游标对象
    tourist_list = []
    cursor = conn.cursor()
    # 查询 SQL 语句
    sql = "select id from simpleinfo;"
    # 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数
    row_count = cursor.execute(sql)
    # print("SQL 语句执行影响的行数%d" % row_count)
    # 取出结果集中一行数据
    # print(cursor.fetchone())
    for line in cursor.fetchall():
        # print(line)
        # 获取单个字段的值
        tourist_list.append(int(line[0]))
        # print("pos的值" + line[0])
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return tourist_list

def perplexity(num_topics,corpus,dictionary):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=30)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
    print(ldamodel.log_perplexity(corpus))
    return ldamodel.log_perplexity(corpus)


# 计算coherence
def coherence(num_topics,corpus,dictionary,data_set):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=30, random_state=1)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=10))
    ldacm = CoherenceModel(model=ldamodel, texts=data_set, dictionary=dictionary, coherence='c_v')
    print(ldacm.get_coherence())
    return ldacm.get_coherence()

def LDA_code(doc_set):

    # list for tokenized documents in loop
    texts = []
    # loop through document list
    for i in doc_set:
        # clean and tokenize document string
        stemmed_tokens=creat(str(i))
        # add tokens to list\
        # print(stemmed_tokens)
        texts.append(stemmed_tokens)
    # print(texts)
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # 压缩词向量，去掉出现的文章小于2的词，和在50%的文章都出现的词，整体长度限制在500
    dictionary.filter_extremes(no_below=2, no_above=0.5, keep_n=500)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    # lda模型，num_topics设置主题的个数
    ldamodel = LdaModel(corpus, num_topics=6, id2word = dictionary, passes=30,random_state = 1)
    # print(ldamodel.print_topics(num_topics=6, num_words=1))  #每个主题输出1个单词
    ans_=[]
    for topic in ldamodel.print_topics(num_words=1):
        for i in topic[1:]:
            ans_.append(i[7:-1])
    # print(ans_)
    return ans_

# x = range(1,15)
# # z = [perplexity(i) for i in x]  #如果想用困惑度就选这个
# y = [coherence(i) for i in x]
# plt.plot(x, y)
# plt.xlabel('主题数目')
# plt.ylabel('coherence大小')
# plt.rcParams['font.sans-serif']=['SimHei']
# matplotlib.rcParams['axes.unicode_minus']=False
# plt.title('主题-coherence变化情况')
# plt.show()