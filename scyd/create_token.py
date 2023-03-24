"""
获取验证码生成token并落入文件
"""

import yaml,os,requests,jsonpath,random

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath,"test_data.yaml")

with open(yamlPath,"r",encoding='utf-8') as f:
    result = yaml.load(f.read(),Loader=yaml.FullLoader)

# 环境变量 qa or dev
envir = "qa"



class Token(object):

    # 生成随机手机号
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "186", "187", "188", "189"]
    mobile = random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))
    print(mobile)

    #发送验证码
    def send_verifyCode(self):
        url = result['login'][envir]['url'] + "/yduser/v1/sms/send"
        json = {
            "mobile": self.mobile
        }
        res_data = requests.post(url, json=json).json()
        self.verifyCode = jsonpath.jsonpath(res_data, '$..verifyCode')
        # print(self.verifyCode)

    #手机号验证码登录
    def login(self):
        self.send_verifyCode()
        url = result['login'][envir]['url'] + "/yduser/v1/mobile/code/login"
        json = {
            "mobile": self.mobile,
            "verifyCode": self.verifyCode[0],
            "deviceId":"1aweeqrewr",
            "channelId":"1"

        }
        res_data = requests.post(url, json=json).json()
        print(res_data)
        access_token = jsonpath.jsonpath(res_data, '$..token')
        print(access_token)

        #写入文件






if __name__ == '__main__':
    s = Token()
    s.login()