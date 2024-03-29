import random
import pymysql
from gensim.models import Doc2Vec
import doc2vec_code

def predict():
    input_list = input_()
    model_dm = Doc2Vec.load("doc2vec.model")
    vector = model_dm.infer_vector(input_list)
    model , labels_all = doc2vec_code.cluster(vector)
    labels_all = list(labels_all)
    # print(labels_all)
    labels = labels_all[-1]
    # print(labels)
    ans_list = []
    sum = 0
    random_start = random.randint(0,1000)
    num = random_start
    for label in labels_all[random_start:-1]:
        num = num + 1
        if(label == labels):
            ans_list.append(num)
            sum = sum + 1
        if(sum == 25):
            break
    #ans_list就是景点的id号的列表
    print(ans_list)
    return ans_list

def input_():
    input_list = []
    province = str(input())
    sort = str(input())
    theme1 = str(input())
    theme2 = str(input())
    theme3 = str(input())
    theme4 = str(input())
    theme5 = str(input())
    theme6 = str(input())
    input_list.append(province)
    input_list.append(sort)
    input_list.append(theme1)
    input_list.append(theme2)
    input_list.append(theme3)
    input_list.append(theme4)
    input_list.append(theme5)
    input_list.append(theme6)
    return input_list

predict()
