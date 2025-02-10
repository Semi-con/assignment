# 导入tkineter库
import tkinter

window = tkinter.Tk()
window.title('Calculator')
# 设置窗口大小
window.geometry('400x400')

def add(n):
    # 获取到n1文本框的值
    n1 = inp.get()
    # 清空文本框
    inp.delete(0,len(n1))
    # 插入原来的加上新输入参数n
    inp.insert(0,n1+str(n))

# 执行计算方法
def calc():
    n1 = inp.get()
    inp.delete(0,len(n1))
    # 把文本框的字符串用eval当代码执行一次，再插入到文本框
    inp.insert(0,str(eval(n1)))

# 清空文本框
def clear():
    n1 = inp.get()
    inp.delete(0,len(n1))

# 删除最后一个字符
def back():
    n1 = inp.get()
    inp.delete(len(n1)-1,len(n1))

# 计算绝对值
def ab():
    n1 = inp.get()
    inp.delete(0,len(n1))
    inp.insert(0,str(eval(n1)*-1))

# 设置一个文本框
inp = tkinter.Entry(window, width=25)
# 在第0行，第0个，合并5列
inp.grid(row=0,column=0,columnspan=5)


# 用for循环 创建 123 456 789 9个按钮
for i in range(0,3):
    for j in range(1,4):
      n = j+i*3
      btn=tkinter.Button(window, text=str(j+i*3),width=5, command=lambda n=n:add(n))
      btn.grid(row=i+2,column=j-1)

# 删除按钮(窗口,宽度，文本，执行命令).grid(1行,0列)
tkinter.Button(window,width=5, text="C", command=clear).grid(row=1,column=0)
tkinter.Button(window,width=5, text="←", command=back).grid(row=1,column=1)
tkinter.Button(window,width=5, text="+/-", command=ab).grid(row=1,column=2)

# 删除按钮(窗口,宽度，文本，背景色，文本颜色，执行命令并传入参数).grid(1行,4列)
tkinter.Button(window,width=5, text="+",bg="#f70",fg="#fff",command=lambda:add("+")).grid(row=1,column=4)
tkinter.Button(window,width=5, text="-", bg="#f70",fg="#fff",command=lambda:add("-")).grid(row=2,column=4)
tkinter.Button(window,width=5, text="×",bg="#f70",fg="#fff",command=lambda:add("*")).grid(row=3,column=4)
tkinter.Button(window,width=5, text="÷",bg="#f70",fg="#fff",command=lambda:add("/")).grid(row=4,column=4)
tkinter.Button(window,width=12,text="0", command=lambda:add("0")).grid(row=5,column=0,columnspan=2)
tkinter.Button(window,width=5,text="=", bg="#f70",fg="#fff",command=calc).grid(row=5,column=4)
tkinter.Button(window,width=5, text=".", command=lambda:add(".")).grid(row=5,column=2)

# 进入消息循环
window.mainloop()
