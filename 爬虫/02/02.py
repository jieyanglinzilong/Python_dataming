import requests

formdata = {
    "type": "AUTO",
    "i":"i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue":"UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

url = "https://www.meitu131.com/hot/etagid78-0.html"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data = formdata, headers = headers)

print(response.text)




# 如果是json文件可以直接显示
#print (response.json())