from tkinter import *

#设置tkinter窗口
root = Tk()
#绘制两个label,grid（）确定行列
Label(root,text="请输入作品名：").grid(row = 0,column =0)
Label(root,text="请输入作者名：").grid(row = 1,column =0)

#导入两个输入框
e1 = Entry(root)
e2 = Entry(root)

#设置输入框的位置
e1.grid(row =0 ,column =1)
e2.grid(row =1 ,column =1)

#输入内容获取函数print打印
def show():
    print("作品：《%s》"%e1.get())
    print("作者：%s" %e2.get())

#清除函数，清除输入框的内容
def dele():
    e1.delete(0,END)
    e2.delete(0,END)

#设置两个按钮，点击按钮执行命令 command= 命令函数
theButton1 = Button(root, text ="获取信息", width =10,command =show)
theButton2 = Button(root, text ="清除",width =10,command =dele)

#设置按钮的位置行列及大小
theButton1.grid(row =3 ,column =0,sticky =W, padx=10,pady =5)
theButton2.grid(row =3 ,column =1,sticky =E, padx=10,pady =5)



mainloop()
