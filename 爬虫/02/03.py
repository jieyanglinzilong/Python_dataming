
# 导入urllib.request库
import urllib.request

# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("https://www.meitu131.com/hot/etagid78-0.html")
print(response.info())
# 类文件对象支持文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()
with open('data.html', 'wb') as f:
    f.write(html)


print (html)