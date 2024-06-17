import requests
import json


class AIProxyChat:
    def __init__(self):
        self.url = "https://api.aiproxy.io/v1/chat/completions"
        self.token = "Bearer sk-7YXV6hBPcbWhXS0z3vGTZk3t5PvRpQ1e7XipJHqWRO9ZwUbc"

    def process_response(self, response):
        result = json.loads(response.text)
        #print(result)  # 打印响应结果
        choices = result["choices"]
        content = choices[0]["message"]["content"]
        #print(content)
        return content

    def send_request(self, description,mode):
        print(mode)
        if mode=="1":
            tips=",Please translate the preceding into Chinese"
        elif mode =="2":
            tips=",Please translate the preceding into English"
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user",
                 "content": description+ tips }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token
        }

        response = requests.post(self.url, headers=headers, json=data)
        result=self.process_response(response)
        return result


