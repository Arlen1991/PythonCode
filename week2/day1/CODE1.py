#__author:"arlen fang"
#date:2019/4/11

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")
#print(name,age,job,salary)


if salary.isdigit():
    salary = int(salary)
else:
    print("U must input digit")
    exit("U must input digit")#退出程序



msg = '''
------------info of %s-----------
    name:%s
    age:%d
    job:%s
    salary:%f
    you will be entired in %d years
------------end---------------
'''% (name,name,age,job,salary,65-age)
print(msg)
