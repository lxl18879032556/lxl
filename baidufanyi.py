import json

import requests

url = "https://fanyi.baidu.com/basetrans"

headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"}

querry_str = input("请输入:")

data = {
    "querry":querry_str,
    "from":"zh",
    "to":"en"
}


response = requests.post(url,data=data,headers=headers)

dict_res = json.loads(response.text)   # loads
result = dict_res["trans"][0]["dst"]
print("%s翻译结果：%s"%(querry_str,result))




