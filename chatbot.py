import itchat
import pyrebase

def pushData(username,data):
    config = {
            "apiKey": "",
            "authDomain": "",
            "databaseURL": "",
            "projectId: ": "",
            "storageBucket": "",
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    result = db.child('wechat_data').child(username).push(data)
    return result


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    sender = msg['FromUserName']
    reciver = msg['ToUserName']
    msg = msg['Text']
    result = pushData(username=sender,data=msg)
    print("From {} : {}, Result : {}".format(sender,msg,result))


itchat.auto_login(hotReload=True,enableCmdQR=-2)
itchat.run()


