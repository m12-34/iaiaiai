"""
封装增删改查请求

"""
import app

class UserEmp:
    # 增
    def get_emp_add(self,session,username,mobile):
        emp_data = {"username": username ,
                    "mobile": mobile,
                    "timeOfEntry": "2019-07-01",
                    "formOfEmployment": 1,
                    "workNumber": "1322131",
                    "departmentName": "开发部",
                    "departmentId": "1066240656856453120",
                    "correctionTime": "2019-11-30"}
        return session.post(app.BASE_URL + "user",json= emp_data,headers={"Authorization":"Bearer " + app.TOKEN} )
    # 改
    def get_emp_update(self,session,userId,username):
        return session.put(app.BASE_URL + "user/" + userId,
                           json = {"username":username},
                           headers={"Authorization":"Bearer " + app.TOKEN} )
    # 改)

    # 查
    def get_emp_check(self,session,userId):
        return session.get(app.BASE_URL + "user/" + userId,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 删
    def get_emp_delete(self,session,userId):
        return session.delete(app.BASE_URL + "user/" +userId,
                              headers={"Authorization": "Bearer " + app.TOKEN})