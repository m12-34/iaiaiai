"""
    封装登录请求
"""
import app


class UserLogin:

    # 登录请求
    def login(self,session,mobile,password):
        myData = {"mobile":mobile,
                  "password":password}
        return session.post(app.BASE_URL + "login",json= myData)


