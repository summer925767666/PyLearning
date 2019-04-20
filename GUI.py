# 第三方GUI库：Tkinter wxPython PyQt PyGtk

# Tkinter
from tkinter import *  # 导入模块

#点击按钮切换画布的背景颜色
def shift_color(event):
    global color_index#全局变量的使用！！！
    colors = ["red", "green", "blue"]
    canvas.config(bg=colors[color_index % len(colors)])
    color_index += 1


root = Tk()  # 创建主窗体

label = Label(root, text="Welcome to Python")  # 创建文字
canvas = Canvas(root, bg="white")  # 创建画布
button = Button(root, text="shift color")  # 创建按钮

# 使用pack布局
label.pack()
canvas.pack()
button.pack()

#绑定事件
color_index=0
button.bind("<Button-1>", func=shift_color)

root.mainloop()  # 主窗口进入主事件循环
