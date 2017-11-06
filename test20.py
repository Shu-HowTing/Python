#爬虫
# import urllib.request
# html = urllib.request.urlopen("http://placekitten.com/g/320/240")
# img = html.read()
# f = open('cat.jpg','wb')
# f.write(img)
# f.close()
import urllib.request
import urllib.parse
import json
#content  = input("请输入要翻译的内容：")
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
data = {'i':'我爱你',
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':dict,
        'client':'fanyideskweb',
        'salt':'1496069605685',
        'sign':'04031ac747ac2028b3f9cf3cdfd9cbf6',
        'action':'FY_BY_CLICKBUTTON',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'ue':'UTF-8',
        'typoResult':'true'
        }
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)
# target = json.loads(html)
# print("翻译结果：%s" % target['translateResult'][0][0]['tgt'])

