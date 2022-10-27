from operator import index
import pandas as pd
import random
print('=' * 20)
print('欢迎使用背菜本')
print('1.背菜序号第一页')
print('2.背菜序号第二页')
print('3.背水果序号第一页')
print('4.背水果序号第二页')
print('5.背模拟卷子')
print('6.退出背菜本')
print('=' * 20)
df1 = pd.read_csv(r"D:\mystudy\QA\Git hub\Google-Python\Interact_with_OS\menu1.csv")
df2 = pd.read_csv(r"D:\mystudy\QA\Git hub\Google-Python\Interact_with_OS\menu2.csv")
df3 = pd.read_csv(r"D:\mystudy\QA\Git hub\Google-Python\Interact_with_OS\menu3.csv")
df4 = pd.read_csv(r"D:\mystudy\QA\Git hub\Google-Python\Interact_with_OS\menu4.csv")
df5 = pd.read_csv(r"D:\mystudy\QA\Git hub\Google-Python\Interact_with_OS\menu5.csv")
while True:
  fun_num = input('请输入功能编号：')
  if fun_num == '1':  # 查看背菜本1
     i=random.randint(0,75)
     value = input("Please input the Id of {}: ".format(df1.iloc[i,1]+df1.iloc[i,2]))
     if value == df1.iloc[i,0]:
        print("You are right!")
     else:
        print("You are wrong! It should be {}! ".format(df1.iloc[i,0]))
  elif fun_num == '2':
     i=random.randint(0,69)
     value = input("Please input the Id of {}: ".format(df2.iloc[i,1]+df2.iloc[i,2]))
     if value == df2.iloc[i,0]:
        print("You are right!")
     else:
        print("You are wrong! It should be {}! ".format(df2.iloc[i,0]))
  elif fun_num == '3':
     i=random.randint(0,59)
     value = input("Please input the Id of {}: ".format(df3.iloc[i,1]+df3.iloc[i,2]))
     if value == df3.iloc[i,0]:
        print("You are right!")
     else:
        print("You are wrong! It should be {}! ".format(df3.iloc[i,0]))
  elif fun_num == '4':
     i=random.randint(0,46)
     value = input("Please input the Id of {}: ".format(df4.iloc[i,1]+df4.iloc[i,2]))
     if value == df4.iloc[i,0]:
        print("You are right!")
     else:
        print("You are wrong! It should be {}! ".format(df4.iloc[i,0]))
  elif fun_num == '5':
   
     i=random.randint(0,66)
     value = input("Please input the Id of {}: ".format(df5.iloc[i,1]+str(df5.iloc[i,2])))
     if value == df5.iloc[i,0]:
        print("You are right!")
     else:
        print("You are wrong! It should be {}! ".format(df5.iloc[i,0]))
  elif fun_num == '6':  # 退出
        print('退出成功')
        break

    
