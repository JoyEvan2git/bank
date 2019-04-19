from admin import Admin
from atm import ATM
import time
import os
import pickle
def main():
    #管理员对象
    admin = Admin()
    admin.printAdminView()
    # 数字是0，就会被认为是False 然后函数结束
    if admin.adminOption():
        return -1
    #存储所有用户的信息
    filepath = os.path.join(os.getcwd(), "alluser.data")
    try:
        with open(filepath,"rb")as f:
            allUsers = pickle.load(f)
    except FileNotFoundError:
        allUsers = {}
    atm = ATM(allUsers)

    while True:
        i = os.system("cls")
        admin.sysFunctionView()
        option = input("请输入您的操作：")
        if option == '1':
            atm.createUser()
        elif option == '2':
            atm.searchUserInfo()
            time.sleep(5)
        elif option == '3':
            atm.getMoney()
        elif option == '4':
            atm.saveMoney()
        elif option == '5':
            atm.transferMoney()
        elif option == '6':
            atm.changePasswd()
        elif option == '7':
            atm.lockUser()
        elif option == '8':
            atm.unLockUser()
        elif option == '9':
            atm.newCard()
        elif option == '0':
            atm.killUser()
        elif option == 't':
            if not admin.adminOption():
                print("退出系统")
                return -1
        with open(filepath, "wb")as f:
            pickle.dump(allUsers, f)
        time.sleep(1)
if __name__ == '__main__':
    main()

