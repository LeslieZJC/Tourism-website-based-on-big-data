import gensim
import pymysql
from gensim.models import Doc2Vec
from LDA import tourist_mysql
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans

TaggededDocument=gensim.models.doc2vec.TaggedDocument

doc_vec = []
def get_word():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='111111', database='crawler',
                           charset='utf8')
    cursor = conn.cursor()
    tourlist_list = tourist_mysql()
    cut_sentence = []
    x_train = []
    for tourist_num in tourlist_list:
        sql1 = "select provinces,sort,theme1,theme2,theme3,theme4,theme5,theme6 from preinfolabel where id=" + str(tourist_num) + ";"
        # 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数
        row_count = cursor.execute(sql1)
        # 取出结果集中一行数据
        # print(cursor.fetchone())
        strs = ''
        temp = [0,1,2,3,4,5,6,7]
        for line in cursor.fetchall():
            for i in temp:
                if (i != 7) :
                    strs+=(str(line[i])+' ')
                else :
                    strs+=str(line[i])
        cut_sentence.append(strs)
    for i, text in enumerate(cut_sentence):
        word_list = text.split(' ')
        doc_vec.append(word_list)
        l = len(word_list)-1
        word_list[l-1] = word_list[l-1].strip()
        document = TaggededDocument(word_list,tags=[i])
        x_train.append(document)
    print(x_train)
    return x_train

def train(x_train):
    model = Doc2Vec(x_train,min_count=1,window=3,vector_size=300,sample=1e-3,negative=5,workers=4)
    model.train(x_train,total_examples=model.corpus_count,epochs=10)
    model.save('doc2vec.model')


def get_vectors():
    list_lyrics = doc_vec
    infered_vectors_list = []
    print(list_lyrics)
    print("load doc2vec model...")
    model_dm = Doc2Vec.load("doc2vec.model")
    print("load train vectors...")
    for lyric in list_lyrics:
        vector = model_dm.infer_vector(lyric)
        infered_vectors_list.append(vector)
    vector_df = pd.DataFrame(np.matrix(infered_vectors_list))
    vector_df.to_csv("doc_vecs.csv", index=None, header=None)


def cluster(input_list):
    df = pd.read_csv("doc_vecs.csv", header=None)
    infered_vectors_list = list(df.iloc[:,:].values)
    infered_vectors_list.append(input_list)
    infered_vectors_list = np.array(infered_vectors_list)
    # print(infered_vectors_list)
    print("train kmean model...")
    kmean_model = KMeans(n_clusters=20)
    kmean_model.fit(infered_vectors_list)
    labels = kmean_model.predict(infered_vectors_list)
    # cluster_centers = kmean_model.cluster_centers_


    # print(labels)
    # print(cluster_centers)
    # sse = kmean_model.inertia_

    return kmean_model , labels

def init():
    x_train = get_word()
    # print(x_train)
    train(x_train)
    get_vectors()

