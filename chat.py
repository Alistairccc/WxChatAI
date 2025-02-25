import requests

# 初始化消息列表
message_list = []

while True:
    # 获取用户输入
    text = input("请输入:")
    if text.lower() == 'quit':
        # 如果用户输入 'quit'，则退出循环
        break
    # 创建用户消息字典
    user_dict = {"role": "user", "content": text}
    # 将用户消息添加到消息列表中
    message_list.append(user_dict)

    try:
        # 发送 POST 请求到本地 API
        res = requests.post(
            url="http://localhost:11434/api/chat",
            json={
                "model": "deepseek-r1:1.5b",
                "messages": message_list,
                "stream": False
            }
        )
        # 检查响应状态码
        res.raise_for_status()
        # 将响应内容解析为 JSON 格式
        data_dict = res.json()
        # 提取响应消息字典
        res_msg_dict = data_dict['message']
        # 打印模型的回复
        print(res_msg_dict['content'])
        # 将模型的回复添加到消息列表中，以便后续对话
        message_list.append(res_msg_dict)
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print(f"请求发生错误: {e}")
    except KeyError as e:
        # 处理 JSON 解析异常
        print(f"响应数据格式错误: {e}")