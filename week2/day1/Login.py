#__author:"arlen fang"
#date:2019/4/11
_user = "arlen"
_passwd = "abc123"

for i in range(3):
    username = input("Username:")
    password = input("Password:")
    if username == _user and password == _passwd :
        print("Welcome to login....")
        break
    else:

        print("invalid username or password")
else:
    print("密码输入错误超过次数，已锁定")


#
# for i in range(1,100,2):
#     print("times:",i)