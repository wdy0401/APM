# -*- coding: utf-8 -*-
"""
Created on 2018-01-02

@author: ccc
"""

"""
这是一个多因子测试程序 
目的是复制华泰证券多因子报告的策略
数据来源为wind
麻雀为动量策略
"""

"""
使用class办法
    get_factor

"""

"""
对于每支股票:算出or维护每日 每个因子的数值 
对于每个因子:维护每日 每支股票各个因子的值 这与股票中是双重维护的关系
对于特定因子:若能计算衍生因子,视为新的因子
将所有股票进行排序与因子效果测试
将股票分成若干group,分别进行排序与因子效果测试

挑选出有效因子,对于通过有效因子对收益进行回测
"""
import os

import pandas as pd

from datetime import datetime
today=datetime.today()

import tushare as ts

from WindPy import *
w.start()

    
class Stock(object):
    def __init__(self, code): 
        self.code = code
        self.kfile="./price/"+code+".csv"
        if(code[0]=="0" or code[0]=="3") and len(code)==6:   
            self.exchg='SZ'
        elif code[0]=="6" and len(code)==6:
            self.exchg='SH'
        else:
            print(f"ERROR code ##{code}##")
    def init_price(self):
        self.load_price()
        #self.download_price()
        #self.join_price()
    def load_price(self):
        if os.path.exists(self.kfile):
            self.k=pd.DataFrame.from_csv("./price/"+code+".csv")
        else:
            print(f"ERROR{stock.code} file")
    def download_price(self):
        if os.path.exists(self.kfile) and os.path.getsize(self.kfile)>100:
            return
        a=w.wsd(f"{self.code}.{self.exchg}",\
                "open,high,low,close,volume,amt,dealnum,chg","2008-01-01",\
                f"{today.year}-{today.month}-{today.day}",\
                "PriceAdj=F")#收盘 成交 总量 持仓 结算
        self.k=pd.DataFrame(a.Data,index=a.Fields,columns=a.Times).T
        self.save_price()
    def join_price(self):
        pass
    def save_price(self):
        if hasattr(self, 'k'):
            self.k.to_csv("./price/"+code+".csv")
    def init_ret(self):
        pass
    def get_fct(self,fctname):
        pass
    
#kk=ts.get_today_all()
#kk.to_csv("today_all.csv")
kk=pd.DataFrame.from_csv("today_all.csv")

sdict=dict()
for code in [str(x) for x in kk.code]:
    if len(code)!=6:
        continue
    if code[0]=='9':
        continue
    #print(code)
    sdict[code]=Stock(code)

    sdict[code].load_price()
    #sdict[code].init_price()
    #sdict[code].save_price()

    #sdict[code].download_price()

for stock in sdict.values():
    if hasattr(stock, 'k'):
        print(f"{stock.code}")
    else:
        print(f"ERROR{stock.code}")

#ts实在是不稳定啊 
#import tushare as ts
#
#class Stock(object):
#    def __init__(self, code):
#        self.code = code
#    def init_price(self):
#        self.k=ts.get_h_data(code,start="2010-01-01")
#    def save_price(self):
#        self.k.to_csv("./price/"+code+".csv")
#    def init_ret(self):
#        pass
#    def get_fct(self,fctname):
#        pass
#    
#sdict=dict()
#
#
#
##kk=ts.get_today_all()
#
#for code in kk['code']:
#    print(code)
#    sdict[code]=Stock(code)
#    sdict[code].init_price()
#    sdict[code].save_price()
#    