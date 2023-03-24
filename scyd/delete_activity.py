"""
删除测试数据
"""

import yaml,os,requests,jsonpath
from scyd.login_scyd import Login
import pymysql

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath,"test_data.yaml")

with open(yamlPath,"r",encoding='utf-8') as f:
    result = yaml.load(f.read(),Loader=yaml.FullLoader)

# 环境变量 qa or dev
envir = "qa"
access_token = Login(envir).center_login()
# print(access_token)


class DeleteTestDate(object):

    '''连接MySQL数据库'''
    def connect(self):
        try:
            db = pymysql.connect(
                host=result['Mysql'][envir]['host'],
                port=result['Mysql'][envir]['port'],
                user=result['Mysql'][envir]['user'],
                passwd=result['Mysql'][envir]['passwd'],
                db=result['Mysql'][envir]['db'],
                charset=result['Mysql'][envir]['charset']
            )

            return db
        except Exception:
            raise Exception("数据库连接失败")

    def implement(self):
        '''执行SQL语句'''
        db = self.connect()
        cursor = db.cursor()
        sql = "SELECT activity_id FROM t_activity_info where del = 0 and activity_type = 2 AND activity_name  LIKE '%测试活动%'"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            activity_list = list(result)
            db.commit()
            # print('查询结果：', result)
            print(activity_list)
            # print(activity_list[0][0])
            # print(len(activity_list))
            return activity_list
        except Exception:
            db.rollback()
            print("查询失败")

        cursor.close()
        db.close()


    # 删除活动专区活动
    def delete_activity2(self):

        try:
            for i in self.implement():
                url = result['Center'][envir]['url'] + "/scyd/service/ydmanage/v1/point/activityOpera"
                headers = {"access_token": access_token}
                json = {
                    "menuId": "7a43497d-04e1-487a-be53-6ae3c732c595",
                    "activityId": i[0],
                    "operaType": 2,
                    "activityType": 2
                }
                # print(i[0])
                requests.post(url, headers=headers, json=json).json()

        except Exception as e:
            print(e)

        try:
            for i in self.implement():
                url = result['Center'][envir]['url'] + "/scyd/service/ydmanage/v1/point/activityOpera"
                headers = {"access_token": access_token}
                json = {
                    "menuId": "7a43497d-04e1-487a-be53-6ae3c732c595",
                    "activityId": i[0],
                    "operaType": 3,
                    "activityType": 2
                }
                # print(i[0])
                requests.post(url, headers=headers, json=json).json()

        except Exception as e:
            print(e)
if __name__ == '__main__':
    # pass
    # del1 = DeleteTestDate().implement()
    del2 = DeleteTestDate().delete_activity2()

