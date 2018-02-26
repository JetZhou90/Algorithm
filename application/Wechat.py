import itchat,time,re
from itchat.content import  *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match=re.search('年',msg['Text']).span()
    if match:
        itchat.send((''),msg['FromUserName'])

@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
    itchat.send(('图片已收到，谢谢'),msg['FromUserName'])

itchat.auto_login(True)
itchat.run()
