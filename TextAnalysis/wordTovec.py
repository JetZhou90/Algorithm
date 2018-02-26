import gensim
import jieba
import os
from gensim.models import word2vec
import logging
import numpy as np
# f=open('text.txt','a')
# for filename in os.listdir(r'txt'):
#     if (filename != 'Thumbs.db'):
#         if filename.find('.'):
#             txt=open('txt/'+filename,'r',encoding='gbk')
#             lines=txt.readlines()
#
#             for line in lines:
#                 line=line.replace('\t','').replace('\n','').replace('，','').replace('。','').replace('：','')
#                 line=line.replace('？','').replace('！','').replace('”','').replace('“','').replace('‘','').replace('’','').replace('…','')
#                 line=line.replace('（','').replace('）','').replace('、','')
#                 word=jieba.cut(line)
#                 f.write(' '.join(word))
# f.close()

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences =word2vec.Text8Corpus(u"text.txt")
for i in range(80):
    model=word2vec.Word2Vec(sentences,size=150,alpha=0.0001,window=1,workers=2,min_count=200)
print(model.wv.similarity('丁典','丁大哥'))

# for i in range(10):
#     model=word2vec.Word2Vec(sentences,size=150,alpha=0.001)
#     print(i,model)
#     model2 = word2vec.Word2Vec(s, size=150, alpha=0.001)
#     print(i, model2)
#
# y1=model.most_similar(u'狄云',topn=10)
# for item in y1:
#     print(item)
# y2=model2.most_similar(u'狄云',topn=10)
# for item in y1:
#     print(item)







