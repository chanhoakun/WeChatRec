# -*- coding:utf-8 -*-  

import itchat, time, sys
  
reload(sys)  
sys.setdefaultencoding('utf8')   

from itchat.content import *

@itchat.msg_register([TEXT, SHARING, PICTURE, RECORDING, VIDEO])
def text_reply(msg):
    msg.user.send(u'【自动回复】你好，我现在有事无法立即查看你的微信消息并回复。如果你有要紧的事，请给我发短信或者打电话。我的电话号码为****,当然我上线看到消息后也会立即回复你，谢谢。')

itchat.auto_login(enableCmdQR=-2)

itchat.run(True)

