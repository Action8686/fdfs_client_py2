# -*- coding: UTF-8 -*-

import MySQLdb

import datetime
class GetUrl(object):
    def __init__(self):

        # 1、读取数据库插入时间，获取插入时间为1-2号之间的信息
        # 连接数据库
        self.db = MySQLdb.connect('172.00.00.00', '00', '00', '00')

        # 创建游标
        self.cursor = self.db.cursor()

        # 需要执行的sql语句，指定字段查询，可以节省时间，避免慢查询
        self.sql = "select NewsID,InsertDate from tbl_NewsDetails201806 where InsertDate between '2018-06-01' AND '2018-06-30'"
        self.linkNum = 1

    def geturl(self):
        now_time = datetime.datetime.now().strftime('%Y%m')

        # 查询
        try:
            self.cursor.execute(self.sql)
            results = self.cursor.fetchall()
            for row in results:
                NewsID = row[0]
                InsertDate = row[1]

                # 通过id，查询到文件表中文件的路径
                # print('文章的id是:{0}'.format(NewsID))
                sql1 = "SELECT FileDirectory FROM Im.tbl_NewsFileManager201806 WHERE NewsID='{0}'".format(NewsID)
                # print('执行的sql语句是：{0}'.format(sql1))
                self.cursor.execute(sql1)
                resultss = self.cursor.fetchall()

                with open('/home/action/Deskop/fdfs_client_py2/hhhh.txt', 'a+') as f:
                    for i in resultss:
                        imageurl = i[0]
                        print('文章的图片链接是：{0},图片的链接是第{1}条'.format(imageurl, self.linkNum))
                        print '正在写入文件。。。。。。。。。写入文件的时间是：{0}'.format(now_time)
                        f.write(imageurl + '\n')
                        self.linkNum +=1

                # 实现这条新闻，逻辑删除
                # sql = "UPDATE tbl_NewsDetails201807 set NewsOffline=1 WHERE NewsID='201807-5ae2b530-7e97-11e8-be87-fa163e560d98'"

                # 有文件的路径，进行删除


                #  打印结果
                # print("\n NewsID =%s,InsertDate =%s\n " % (NewsID, InsertDate))

        except:
            print("Error: unable to fetch data")  # 关闭数据库连接
            self.db.close()

if __name__ == '__main__':
    get = GetUrl()

    get.geturl()