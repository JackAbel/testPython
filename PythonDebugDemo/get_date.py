#! /bin/bash

import sys
import datetime
import time
import MySQLdb


tables=["stat_bk_sum"]
def isExist(sdate):
    try:
        conn = MySQLdb.connect(host='10.10.57.143', port=3306, user='ads', passwd='ads',db='statistics')
        #所有的查询，都在连接con的一个模块cursor上面运行的
        cursor = conn.cursor()
        for table in tables:
            sql = "select id from "+table+" where endtime='"+str(sdate)+"' limit 1"
            count = cursor.execute(sql)
            if (1 != count):
                return False
    except:
        return False
    conn.close()
    return True

if __name__=="__main__":
    if (len(sys.argv) > 1):
        sdate = sys.argv[1]
    else:
        sdate = datetime.date.today() + datetime.timedelta(-1)

    #循环处理
    while(True):
        try:
            if (isExist(sdate)):
                print "has date,exit..."
                break;
            else:
                print "no date,sleep 5m..."
                time.sleep(60*5)
        except:
            print "exception,sleep 1m..."
            time.sleep(60)
