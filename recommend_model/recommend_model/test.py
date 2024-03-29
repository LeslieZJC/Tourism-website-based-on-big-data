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
    cursor= conn.cursor()
    sql1 = "select comment from commentlist where viewId=" + str(1)+";"
     # 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数
    cursor.execute(sql1)
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
    texts = []
    # loop through document list
    for i in doc_:
        # clean and tokenize document string
        stemmed_tokens = creat(str(i))
        # add tokens to list\
        # print(stemmed_tokens)
        texts.append(stemmed_tokens)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    x = range(1, 15)
    # z = [perplexity(i) for i in x]  #如果想用困惑度就选这个
    y = [coherence(i,corpus,dictionary,texts) for i in x]
    plt.plot(x, y)
    plt.xlabel('主题数目')
    plt.ylabel('coherence大小')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.title('主题-coherence变化情况')
    plt.show()
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
    return ldacm.get_coherence()
