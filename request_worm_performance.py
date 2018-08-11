#!/usr/bin/python
#coding:utf-8
import requests
import time
def request_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"



    

if __name__ == '__main__':
    url = "https://www.baidu.com"
    start_time=time.perf_counter()
    for i in range(100):
        request_html(url)
    end_time=time.perf_counter()

    print("time : ")
    print(end_time - start_time)