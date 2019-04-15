#__author:"arlen fang"
#date:2019/4/15

li = ["alex","wusir","egon","女神","taibai"]
# #增加 列表末尾增加一个元素
# li.append("arlen")
# print(li)
while 1 :
    user_name = input("input name:")
    if user_name.strip().upper() == "Q":
        break
    else:
        li.append(user_name)
        print(li)






