import warnings
import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import re, numpy as np, pandas as pd, jieba
# 忽略警告
from jieba_code import creat

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
def word2vec_code():
    program = os.path.basename(sys.argv[0])  # 读取当前文件的文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    creat()
    # inp为输入语料, outp1为输出模型, outp2为vector格式的模型
    inp = 'key_word.txt'
    out_model = 'corpusSegDone_1.model'
    out_vector = 'corpusSegDone_1.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), vector_size=100, window=5, min_count=1,
                     workers=multiprocessing.cpu_count())
    #保存模型
    model.save(out_model)
    worklist={}
    # 保存词向量
    for word in model.wv.index_to_key:
        worklist[word]=list(model.wv[word])
    martix=[]
    for key in worklist:
        martix.append(worklist[key])
    embeddings = np.array(martix)#已经转换成了numpy向量
    # your_word=np.array(martix[2])
    # print(model.wv.most_similar([your_word],[],1))
    return embeddings,model