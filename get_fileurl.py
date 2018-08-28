# -*- coding: UTF-8 -*-

import MySQLdb

import datetime
from multiprocessing import Process
from DBUtils.PooledDB import PooledDB

class GetFileUrl(object):
    def __init__(self):

        # 1、读取数据库插入时间，获取插入时间为1-2号之间的信息
        # 连接数据库
        self.pool = PooledDB(MySQLdb, 5, host='172.18.00.00', user='00', passwd='00', db='00', port=3306)

        # 创建游标
        # self.cursor = self.db.cursor()
        self.conn = self.pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        self.cur = self.conn.cursor()
        # 需要执行的sql语句，指定字段查询，可以节省时间，避免慢查询
        self.linkNum = 1

    def getfileurl(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 查询
        try:
            # 通过id，查询到文件表中文件的路径
            # print('文章的id是:{0}'.format(NewsID))
            sql1 = "SELECT FileDirectory FROM Im.tbl_NewsFileManager"
            # print('执行的sql语句是：{0}'.format(sql1))
            self.cur.execute(sql1)
            resultss = self.cur.fetchall()

            with open('/home/action/Deskop/fdfs_client_py2/ffff.txt', 'a+') as f:
                for i in resultss:
                    imageurl = i[0]
                    print('文章的图片链接是：{0},图片的链接是第{1}条,时间是：{2}, 获取的数据库是：{3}'.format(imageurl, self.linkNum, now_time, '数据库1'))
                    f.write(imageurl + '\n')
                    self.linkNum +=1


        except:
            print("Error: unable to fetch data")  # 关闭数据库连接
            # self.db.close()
            self.cur.close()
            self.conn.close()

    def getfileurltwo(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 查询
        try:
            # 通过id，查询到文件表中文件的路径
            # print('文章的id是:{0}'.format(NewsID))
            sql1 = "SELECT FileDirectory FROM Im.tbl_NewsFileManager201806"
            # print('执行的sql语句是：{0}'.format(sql1))
            self.cur.execute(sql1)
            resultss = self.cur.fetchall()

            with open('/home/action/Deskop/fdfs_client_py2/ffff.txt', 'a+') as f:
                for i in resultss:
                    imageurl = i[0]
                    print('文章的图片链接是：{0},图片的链接是第{1}条,时间是：{2}, 获取的数据库是：{3}'.format(imageurl, self.linkNum, now_time,'数据库2'))
                    f.write(imageurl + '\n')
                    self.linkNum +=1


        except:
            print("Error: unable to fetch data")  # 关闭数据库连接
            # self.db.close()
            self.cur.close()
            self.conn.close()

    def run(self):
            tester_process = Process(target=self.getfileurl)
            tester_process.start()

            getter_process = Process(target=self.getfileurltwo)
            getter_process.start()



if __name__ == '__main__':
    get = GetFileUrl()

    get.getfileurl()