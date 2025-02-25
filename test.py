from wxauto import WeChat
WX = WeChat()
WX.SendMsg(msg='你好', who='文件传输助手')
while True:
    msg_dict = WX.GetNextNewMessage()
    for username, msg_list in msg_dict.items():
        print("昵称:", username)

        for msg in msg_list:
            print("\t消息", msg.type, msg.content)

