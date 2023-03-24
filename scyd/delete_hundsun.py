"""
删除测试数据
"""

import yaml,os,requests,jsonpath
from scyd.login_scyd import Login

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath,"test_data.yaml")

with open(yamlPath,"r",encoding='utf-8') as f:
    result = yaml.load(f.read(),Loader=yaml.FullLoader)

# 环境变量 qa or dev
envir = "dev"
access_token = Login(envir).center_login()
# print(access_token)



class DeleteTestDate(object):

    # 删除九宫格运营
    def delete_column(self):

        url = result['Center'][envir]['url'] + "/scyd/hundsun/icon/column/list"
        headers = {"access_token": access_token}
        params = {
            "colu_name": "九宫格运营栏目",
            "start": "1",
            "limit": "10000",
            "publish_type": 0
        }
        params2 = {
            "colu_name": "图标",
            "start": "1",
            "limit": "10000",
            "publish_type": 0
        }
        res_data = requests.get(url, headers=headers, params=params).json()
        res_data2 = requests.get(url, headers=headers, params=params2).json()

        colu_list = jsonpath.jsonpath(res_data, '$..list[*].serial_no')
        colu_list2 = jsonpath.jsonpath(res_data2, '$..list[*].serial_no')

        print(colu_list)
        print(colu_list2)

        try:
            # colu_list.extend(colu_list2)
            print(colu_list)
            for i in colu_list:
                # 下架九宫格
                url = result['Center'][envir]['url'] + "/scyd/hundsun/operation/set"
                headers = {"access_token": access_token}
                json = {
                    "serial_no": i,
                    "operation_type": 3,
                    "status": "0"
                }
                requests.post(url, headers=headers, json=json).json()
                # return res_data


                # 删除运营栏目
                url = result['Center'][envir]['url'] + "/scyd/hundsun/icon/column/delete"
                headers = {"access_token": access_token}
                json = {
                    "serial_nos": i
                }
                requests.post(url, headers=headers, json=json).json()

            print('九宫格运营已删除')
            # return res_data
        except Exception as e:
            print(e)

    # 删除九宫格图标
    def delete_icon(self):

        url = result['Center'][envir]['url'] + "/scyd/hundsun/icon/list"
        headers = {"access_token": access_token}
        params = {
            "icon_name": "九宫格图标",
            "start": "1",
            "limit": "10000"
        }
        res_data = requests.get(url, headers=headers, params=params).json()
        icon_list = jsonpath.jsonpath(res_data, '$..list..serial_no')
        try:
            for i in icon_list:
                url = result['Center'][envir]['url'] + "/scyd/hundsun/icon/delete"
                headers = {"access_token": access_token}
                json = {
                    "serial_nos": i
                }
                requests.post(url, headers=headers, json=json).json()

            print('九宫格图标已删除')
            # return res_data

        except Exception as e:
            print(e)
        # print(res_data)

    # 删除图标素材
    def delete_material(self):

        url = result['Center'][envir]['url'] + "/scyd/hundsun/operation/material/list"
        headers = {"access_token": access_token}
        params = {
            "material_origin_name": "素材图标",
            "start": "1",
            "limit": "10000"
        }
        res_data = requests.get(url, headers=headers, params=params).json()
        material_list = jsonpath.jsonpath(res_data, '$..list..serial_no')
        try:
            for i in material_list:
                url = result['Center'][envir]['url'] + "/scyd/hundsun/operation/material/delete"
                headers = {"access_token": access_token}
                json = {
                    "serial_nos": i
                }
                requests.post(url, headers=headers, json=json).json()

            print('图标素材已删除')
            # return res_data
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # pass
    del1 = DeleteTestDate().delete_column()
    del2 = DeleteTestDate().delete_icon()
    del3 = DeleteTestDate().delete_material()