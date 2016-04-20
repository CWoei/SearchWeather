#coding=gb2312
__author__ = 'woei'
import urllib2
import json
from city import city
#ver 1.0.0
cityname = raw_input('请输入要查询的城市\n')
cityname = cityname.decode("gb2312")
citycode = city.get(cityname)
#print citycode
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
    context = urllib2.urlopen(url).read()
    info = context.decode('utf-8') #解码与源网页编码有关
    #print info
    #{"weatherinfo":{"city":"福州","cityid":"101230101","temp1":"7℃","temp2":"19℃","weather":"多云转晴","img1":"n1.gif","img2":"d0.gif","ptime":"18:00"}}
    Items = info.replace('{"weatherinfo":{"','').replace('"}}','').replace('"','').split(',')
    print '查询城市:' , Items[0][Items[0].find(':')+1:].replace('"','')
    print '温度:' , Items[2][Items[2].find(':')+1:].replace('"','') , '到' , Items[3][Items[3].find(':')+1:].replace('"','')
    print '天气状况:' , Items[4][Items[4].find(':')+1:].replace('"','')
    print '更新时间:' , Items[7][Items[7].find(':')+1:].replace('"','')
else:
    print('检索错误!')
	
