from card import Card
from user import User
from admin import Admin
import random
class ATM(object):
    def __init__(self,allUsers):
        self.allUsers = allUsers
        self._admin = Admin()
    def logIn(self):
        #用户登陆
        cardNum = int(input("请输入您的卡号："))
        print(self.allUsers)
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！操作失败")
            return -1
        if user.card.cardLock:
            print("账户已经被锁定！")
            return -1
        print(user)
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！操作失败,账户已经被锁定")
            user.card.cardLock = True
            return -1
        print("登陆成功！")
        return user
    def createUser(self):
        #向用户字典中添加一对键值对（卡号，用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误，开户失败")
            return -1
        onePasswd = input("请设置密码：")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！开户失败")
            return -1
        cardId = self.randomCardId()
        card = Card(cardId,onePasswd,prestoreMoney)
        user = User(name,idCard,phone,card)
        print(cardId)
        #存到字典
        self.allUsers[cardId] = user
        print("开户成功，请牢记 账户："+str(cardId)+" 密码： "+onePasswd)
    def searchUserInfo(self):
        #查询
        isadmin = input("是否是管理员y/n")
        if isadmin == 'y':
            Inputadmin = input("请输入管理员账号：")
            Inputpasswd = input("请输入管理员密码：")
            if self._admin.admin != Inputadmin:
                print("账号错误")
                return -1
            if self._admin.passwd != Inputpasswd:
                print("密码错误")
                return -1
            print("操作成功！请稍后...")
            n = 1
            for v in self.allUsers.values():
                print("第%d个用户："%(n))
                print("用户姓名：%s\n用户身份证：%s\n用户手机：%s\n用户卡号:%d\n卡密码：%s\n卡内余额：%d\n是否锁定：%s\n"%(v.name,v.idCard,v.phone,v.card.cardId,v.card.cardPasswd,v.card.cardMoney,v.card.cardLock))
                n += 1
        else:
            user = self.logIn()
            if isinstance(user,User):
                print("账号：%s   余额:%d"%(user.card.cardId,user.card.cardMoney))
    def getMoney(self):
        #取款
        user = self.logIn()
        if isinstance(user,User):
            temp = int(input("请输入你的取款金额:"))
            if temp < 0:
                temp = 0
            reQu = self.checkPasswd(user.card.cardPasswd)
            if reQu:
                if user.card.cardMoney < temp:
                    print("余额不足，取款失败......")
                    return -1
                user.card.cardMoney -= temp
                print("取款成功，卡内余额为%d" %(user.card.cardMoney))
                return 0
        return -1
    def saveMoney(self):
        #存钱
        user = self.logIn()
        if isinstance(user, User):
            temp = int(input("请输入你的存款金额:"))
            if temp < 0:
                temp = 0
                print("金额太小，存款失败!")
                return -1
            reQu = self.checkPasswd(user.card.cardPasswd)
            if reQu:
                user.card.cardMoney += temp
                print("取款成功，卡内余额为:%d" % (user.card.cardMoney))
                return 0
    def transferMoney(self):
        #转账
        user = self.logIn()
        if isinstance(user, User):
            idnum = int(input("请输入你要转账的卡号"))
            tra_user = self.allUsers.get(idnum)
            if not tra_user:
                print("该卡号不存在！！操作失败!")
                return -1
            if tra_user.card.cardLock:
                print("该账户已锁定，无法转账！")
                return -1
            temp = int(input("请输入你的转账金额："))
            if temp < 0:
                temp = 0
                print("金额太小，转账失败!")
                return -1
            reQu = self.checkPasswd(user.card.cardPasswd)
            if reQu:
                if temp > user.card.cardMoney:
                    print("卡内余额不足，转账失败！")
                    return -1
                user.card.cardMoney -= temp
                tra_user.card.cardMoney += temp
                print("转账成功，卡内余额为:%d" % (user.card.cardMoney))
                return 0
    def changePasswd(self):
        #改密
        user = self.logIn()
        if isinstance(user, User):
            onePasswd = input("请设置新密码：")
            rePasswd = input("请再输一次密码：")
            if onePasswd == rePasswd:
                user.card.cardPasswd = onePasswd
                print("密码设置成功！")
                return 0
    def lockUser(self):
        #锁定
        user = self.logIn()
        if isinstance(user,User):
            tempIdCard = input("请输入您的身份证号码：")
            if tempIdCard !=user.idCard:
                print("身份证输入错误！锁定失败......")
                return -1
            #锁定
            user.card.cardLock = True
            print("锁定成功！")
    def unLockUser(self):
        #解锁
        cardNum = int(input("请输入您的卡号："))
        print(self.allUsers)
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！操作失败!")
            return -1
        if not user.card.cardLock:
            print("该账户未锁定，可以继续使用！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！操作失败!")
            return -1
        user.card.cardLock = False
    def newCard(self):
        #补卡
        cardNum = int(input("请输入您需要补办的卡号："))
        print(self.allUsers)
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！操作失败!")
            return -1
        userofId = user.idCard
        idcd = input("请输入持卡人的身份证号：")
        if idcd == userofId:
            onePasswd = input("请设置新密码：")
            rePasswd = input("请再输一次密码：")
            if onePasswd == rePasswd:
                user.card.cardPasswd = onePasswd
                print("密码设置成功！")
                return 0
        print("身份证错误，补卡失败！")
    def killUser(self):
        #销户
        user = self.logIn()
        if isinstance(user, User):
            issure = input("确定销户？y/n")
            if issure == "y":
                userofId = user.idCard
                idcd = input("请输入持卡人的身份证号：")
                if idcd == userofId:
                    delUser = self.allUsers.pop(user.card.cardId)
                    print(str(delUser.card.cardId)+" 已经被注销！")
    def checkPasswd(self,realPasswd):
        #验证密码
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    def randomCardId(self):
        # 生成卡号
        while True:
            num = random.randint(100000,999999)
            if num not in self.allUsers.keys():
                return num