"""
导出意见反馈
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

class ExportFeedback(object):

    def exportExcel(self):
        url = result['Center'][envir]['url'] + "/scyd/service/ydmanage/v1/feedback/exportExcel"
        headers = {"access_token": access_token}
        params = {
            "mobile": "",
            "appName": "",
            "appVersion": ""
        }
        res_data = requests.get(url, headers=headers, params=params)
        res_data.encoding = 'utf-8'
        print(res_data.encoding)





if __name__ == '__main__':
    exp = ExportFeedback().exportExcel()