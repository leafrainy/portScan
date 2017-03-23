# coding:utf8
# 端口扫描工具
# 使用方式：python p.py -i 192.168.1.1 -p 22
# 2017-03-23
# leafrainy （leafrainy.cc）

import socket
import re
import sys

s = sys.argv
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def useNotic(s):
    print "请按照格式输入正确的参数"
    print "使用方法： python "+s[0]+" -i ip -p port"
    print "    示例： python "+s[0]+" -i 192.168.1.1 -p 22"

def inputInfo(s):
    if len(s) != 5:
    	useNotic(s)
    	exit(0)

    i = '-i'
    p = '-p'
    inputInfoList = []

    if i in s:
    	if s.index('-i') == 1:
    		if re.match(r"^\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*$", s[2]):
    			inputInfoList.append(s[2])
    		else:
    			print "请输入正确的IP地址"
    			useNotic(s)
    			exit(0)

    if p in s:
    	if s.index('-p') == 3:
    		if (int(s[4]) <= 65535)&(int(s[4])>0):
    			inputInfoList.append(s[4])
    		else:
    			print "请输入正确的端口号"
    			useNotic(s)
    			exit(0)

    return inputInfoList

def scanPort(ss,inputInfoList):
    print "扫描中。。。。"
    #tcp
    try:
        result = ss.connect_ex((inputInfoList[0],int(inputInfoList[1])))
        if result == 0:
        	print inputInfoList[1]+"  端口已开放"
        else:
        	print inputInfoList[1]+"  端口已关闭"
        ss.close()
    except:
    	print '端口扫描异常'



if __name__ == '__main__':

    inputInfoList = inputInfo(s)
    scanPort(ss,inputInfoList)