#coding=gb2312
__author__ = 'woei'
import urllib2
import json
from city import city
#ver 1.0.0
cityname = raw_input('������Ҫ��ѯ�ĳ���\n')
cityname = cityname.decode("gb2312")
citycode = city.get(cityname)
#print citycode
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
    context = urllib2.urlopen(url).read()
    info = context.decode('utf-8') #������Դ��ҳ�����й�
    #print info
    #{"weatherinfo":{"city":"����","cityid":"101230101","temp1":"7��","temp2":"19��","weather":"����ת��","img1":"n1.gif","img2":"d0.gif","ptime":"18:00"}}
    Items = info.replace('{"weatherinfo":{"','').replace('"}}','').replace('"','').split(',')
    print '��ѯ����:' , Items[0][Items[0].find(':')+1:].replace('"','')
    print '�¶�:' , Items[2][Items[2].find(':')+1:].replace('"','') , '��' , Items[3][Items[3].find(':')+1:].replace('"','')
    print '����״��:' , Items[4][Items[4].find(':')+1:].replace('"','')
    print '����ʱ��:' , Items[7][Items[7].find(':')+1:].replace('"','')
else:
    print('��������!')
	
