import itchat
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import pyqrcode


deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train("chatterbot.corpus.chinese")


class sqlite3Helper:

    def __init__(self):
        pass

    def saving_msg(self,account,msg):
        pass

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    response = deepThought.get_response(msg['Text'])
    print("from",msg['FromUserName'],msg['Text'])
    print("to",response)
    itchat.send(msg="This is a AI's response\n " + str(response) ,toUserName=msg['FromUserName'])

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/QR1.jpg"
itchat.auto_login(hotReload=True)

itchat.run()


