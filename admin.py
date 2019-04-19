import time
class Admin(object):
    def __init__(self):
        self.admin = '1'
        self.passwd = '1'
    def printAdminView(self):

        print("*******************************************************************")
        print("*                                                                 *")
        print("*                         冉某人银行系统                          *")
        print("*                                                                 *")
        print("*                                                                 *")
        print("*                                                                 *")
        print("*                                                                 *")
        print("*                              V1.0                               *")
        print("*                                                                 *")
        print("*                                                                 *")
        print("*******************************************************************")

    def adminOption(self):
        Inputadmin = input("请输入管理员账号：")
        Inputpasswd = input("请输入管理员密码：")
        if self.admin != Inputadmin:
            print("账号错误")
            return -1
        if self.passwd != Inputpasswd:
            print("密码错误")
            return -1
        print("操作成功！请稍后...")
        time.sleep(1)
        return 0
    def sysFunctionView(self):
        print("********************************************************************")
        print("*           开户（1）                            查询（2）          *")
        print("*           取款（3）      冉某人银行系统         存款（4）          *")
        print("*           转账（5）                            改密（6）          *")
        print("*           锁定（7）                            解锁（8）          *")
        print("*           补卡（9）                            销户（0）          *")
        print("*                             退出（t）                             *")
        print("********************************************************************")