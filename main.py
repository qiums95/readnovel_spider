import urllib.request
import urllib.parse
from lxml import etree
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"
}

# 小说主页https://www.readnovel.com/book/28483013107170404
url = "https://www.readnovel.com"  # 拼接链接/小说网站

zhuye = "https://www.readnovel.com/book/23522417501918504"  # 小说主页



request_z = urllib.request.Request(url=zhuye, headers=headers)

response_z = urllib.request.urlopen(request_z)

content_z = response_z.read().decode('utf-8')

tree_z = etree.HTML(content_z)

nexturl = tree_z.xpath('//a[@id="readBtn"]/@href')[0]  # 开始阅读按钮获取链接

url_into = url + nexturl  # url拼接

result_z = tree_z.xpath('//span[@id="J-catalogCount"]/text()')[0]  # 获取章节数

result_finditer = re.findall(r"\d+", result_z)[0]  # 提取章节数

x = 0
while x < int(result_finditer):  # 循环获取章节

    request = urllib.request.Request(url=url_into, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    tree = etree.HTML(content)

    result = tree.xpath('//h1[@class="j_chapterName"]/text()')[0]  # 标题
    result2 = tree.xpath('//div[@class="ywskythunderfont"]/p/text()')  # 正文
    nexturl = tree.xpath('//a[@id="j_chapterNext"]/@href')[0]  # 下一章链接
    url_into = url + nexturl  # url拼接

    print(result)

    i = 0  # 列表中的每个元素都分配了一个数字，它的位置，第一个位置是0，第二个位置是1，依此类推。
    while i < len(result2):  # len()方法返回列表元素个数。使用方法:len(list)
        print(result2[i])  # print输出
        i = i + 1

    x = x + 1
