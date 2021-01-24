import urllib
import threading
import gzip
from io import StringIO, BytesIO
from pip._vendor.distlib.compat import raw_input

lock = threading.Lock()
import zlib

global pn
pn = 0


def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print("正在存储" + filename)
    print(type(html))
    file = zlib.decompress(html, 16+zlib.MAX_WBITS)

    save(file)


def save(file):
    global pn
    try:
        pg = str(pn)

        print(pn)
        pn += 1
        lock.acquire()
        filenames = "尤果" + pg + ".html"
        with open(filenames, 'wb') as f:
            f.write(file)

    finally:
        lock.release()


def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''
    print("正在下载" + filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
               'Accept-Encoding': 'gzip, deflate'

               }

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()


def tiebaSpider(url, key, beginPage, endPage):
    """
        作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """
    pn = 1
    for page in range(beginPage, endPage + 1):
        pn = pn + 1

        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + str(pn) + key
        print(fullurl)
        # print fullurl

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)


# 模拟 main 函数
# 模拟 main 函数
if __name__ == "__main__":
    # kw = raw_input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入终止页："))

    url = "https://www.meitu131.com/nvshen/index_"
    key = ".html"

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol

    tiebaSpider(url, key, beginPage, endPage)
