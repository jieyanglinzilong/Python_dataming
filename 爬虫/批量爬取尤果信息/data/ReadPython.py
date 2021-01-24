# xpath_li.py

from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
text = '尤果2.html'
html = etree.parse(text, parser=parser)

result = html.xpath('//img/@src')
print(result[2])
for i in range(len(result)+1):
    print(result[i])
#注意这么写是不对的：
#因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠

#result = html.toString(html, encoding="utf-8" )
#print(result)

