from lxml import etree
import requests
from requests.exceptions import ConnectionError
import pandas as pd

def get_page_index():
    base="https://sh.lianjia.com/zufang/pg"
    urls=[]
    for i in range(1,101,1):
        url=base+str(i)+"/"
        urls.append(url)
    return urls

def get_page_detail(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            html=response.content.decode("utf-8")
            return html
    except ConnectionError:
        print("Connect Error!!")
        return None

def parse_page_detail(html):
    dom_tree=etree.HTML(html)
    try:
        title=dom_tree.xpath('//li/div[2]/h2/a/text()')
        name=dom_tree.xpath('//li/div[2]//div/a/span/text()')
        catogery=dom_tree.xpath('//li/div[2]//div//span[1]//span/text()')
        size=dom_tree.xpath('//li/div[2]//div//span[2]/text()')
        region=dom_tree.xpath('//li/div[2]//div[1]//div[2]//div/a/text()')
        price =dom_tree.xpath("//li/div[2]//div[2]//span[@class='num']/text()")
        other=dom_tree.xpath('//li/div[2]//div[1]//div[2]//div/text()')
        name1=[]
        catogery1=[]
        size1=[]
        second_feature=[]
        third_feature=[]
        for n in name:
            name1.append(n[0:-2])
        for c in catogery:
            catogery1.append(c[0:-2])
        for s in range(0,60):
            if s % 2==0:
                tmp=size[s][0:-2]
                size1.append(tmp)
                second_feature.append(other[s])
            third_feature.append(other[s])
        return{
            "title":title,
            "name":name1,
            "catogery":catogery1,
            "size":size1,
            "region":region,
            "price":price,
            "second_feature":second_feature,
            "third_feature":third_feature,
            "other":other
        }

    except:
        pass

col=[ "title",
            "name",
            "catogery",
            "size",
            "region",
            "price",
            "second_feature",
            "third_feature",
            "other"]
df1=pd.DataFrame(columns=col)
i=0
if __name__=="__main__":
    urls=get_page_index()
    for url in urls:
        html=get_page_detail(url)
        result=parse_page_detail(html)
        i += 1
        print(i)
        try:
            df2=pd.DataFrame.from_dict(result,orient='index')
            df2=df2.transpose()
            df1=df1.append(df2,ignore_index=True,verify_integrity=True)
            print("Done")
        except:
            print("Error")
            pass

df1=df1.dropna()
df1.to_csv("result.csv")
df1.info()
