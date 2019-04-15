#__author:"arlen fang"
#date:2019/4/15

#只读列表  可循环查询 可切片
#儿子不能改 孙子可能可以改

tu = [1,2,3,'alex',[1,2,3,4,'taibai'],'cgon']
# print(tu[0:4])
# for i in tu :
#     print(i)
#
# tu[4][4] = tu[4][4].upper()
# for i in tu :
#     print(i)
#
#
# for i in range(100,0,-3):
#     print(i)

for i in range(len(tu)):
    if