# encoding: utf8
from fdfs_test import FileClient
from get_url import GetUrl
from get_fileurl import GetFileUrl
import datetime
if __name__ == '__main__':
    #  file_name = 'f54b358c5d6bb0515f542dcbf43f0b4c/group1/M00/00/A7/CAcbCFhzN2WAAn1kAJPqL047Q_o.10.mp4'
    file_test = FileClient()
    # images = GetFileUrl()
    # images.run()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Num = 0

    # print '正在写入文件。。。。。。。。。写入的时间是：{0}'.format(nowTime)
    # with open('./delete.list', 'r') as delete_list:
    with open('./ffff.txt', 'r') as delete_list:
        # print '正在删除...................删除的时间是：{0}'.format(nowTime)
        # [file_test.delete_file(file_name.strip()) for file_name in delete_list]

        for file_name in delete_list:
            Num += 1
            print '删除的文件是:{0}, 正在删除第{1}条,删除的时间是：{2}'.format(file_name, Num, nowTime)
            file_test.delete_file(file_name.strip())

