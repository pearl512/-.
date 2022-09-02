# 创建时间： 2022/09/02 11:18 星期五
# 创建者：ykl

"""作业第一题"""
# 请注意：复制代码时再次检查是否有错误；第四行代码内容需要修改成符合自己的！
# 13、14、15、16行的代码不是连续复制粘贴的，需要输入一行后按下”Enter“再次输入14行，否则会报错。（IDEL是单行运行）

print("Hello World!")
print("I am XXXXX(your name), my id is XXXXX(your ID) ")
print("It's wonderful to learn python ")
name = input("enter your name :")
age = int(input("enter your age :"))
print(name, age)
print(name, age, sep=",")
a = input("enter a number:")
b = input("enter a number:")
c = a + b
print(c)    # why the result is 3456,how to get the correct answer?
c = int(a) + int(b)
print(c)


"""第二题"""

print("*"*50)
print("I'm begin to learn Python")
print("this is my first Python program")
name = input("enter your name :")
age = int(input("enter your age :"))

if age < 30:
    print(name, "You are  very young")
elif age <= 60:
    print(name, "you are adult")
else:
    print(name, "you are senior")

print(name, "Good Bye!")
print("*"*50)


"""第三题"""
s = float(input("数入英里："))
s2 = s*1.6
print(s, "mile=", s2, "km")
