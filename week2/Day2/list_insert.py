#__author:"arlen fang"
#date:2019/4/15
#
# li = ["alex","wusir","egon","女神","taibai"]
#
# #在指定位置插入元素insert
# li.insert(4,"sange")
# print(li)
# #在末尾插入 可迭代的对象  每个元素插入
# li.extend("123")
# print(li)
#
# #按索引删除元素 pop  默认删除最后一个
# deletname_name = li.pop(1)
# print(deletname_name,li)
# #按元素删除 remove
# li.remove("wusir")
# #清空列表
# li.clear()
# #删除列表
# del li
# li = ["alex","wusir","egon","女神","taibai"]
# del li[2:3]
# #切片删除
#
#
# #改元素  直接给列表元素赋值
#
# li[0] ==  "mamxjpi"
# print(li)

#列表嵌套

li = ["taibai","武藤兰","袁浩",['alex','liuneng',89],23]
print(li[1][1])
name=li[0].capitalize()
li[0] = name
print(li)
li[2] = "袁日天"
print(li)
li[3][0]=li[3][0].upper()
print(li)
