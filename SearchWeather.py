#coding=gb2312
__author__ = 'woei'
import urllib2
import json
from city import city
cityname = raw_input('请输入要查询的城市\n')
cityname = cityname.decode("gb2312")
citycode = city.get(cityname)
print citycode
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
    context = urllib2.urlopen(url).read()
    print context.decode('utf-8')  #解码与源网页编码有关
else:
    print('检索错误!')
	
