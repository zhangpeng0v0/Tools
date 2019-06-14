'''
基于tkinter模块的GUI
GUI是图形用户界面的缩写，图形化的用户界面对使用过计算机的人来说应该都不陌生，
在此也无需进行赘述。Python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter），
从这个名字就可以看出它是基于Tk的，Tk是一个工具包，最初是为Tcl设计的，
后来被移植到很多其他的脚本语言中，它提供了跨平台的GUI控件。
当然Tk并不是最新和最好的选择，也没有功能特别强大的GUI控件，事实上，
开发GUI应用并不是Python最擅长的工作，如果真的需要使用Python开发GUI应用，
wxPython、PyQt、PyGTK等模块都是不错的选择。

基本上使用tkinter来开发GUI应用需要以下5个步骤：

1、导入tkinter模块中我们需要的东西。
2、创建一个顶层窗口对象并用它来承载整个GUI应用。
3、在顶层窗口对象上添加GUI组件。
4、通过代码将这些GUI组件的功能组织起来。
5、进入主事件循环(main loop)。
下面的代码演示了如何使用tkinter做一个简单的GUI应用。
'''


import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('500x500')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

'''
需要说明的是，GUI应用通常是事件驱动式的，之所以要进入主事件循环就是要监听鼠标、
键盘等各种事件的发生并执行对应的代码对事件进行处理，因为事件会持续的发生，
所以需要这样的一个循环一直运行着等待下一个事件的发生。另一方面，
Tk为控件的摆放提供了三种布局管理器，通过布局管理器可以对控件进行定位，
这三种布局管理器分别是：Placer（开发者提供控件的大小和摆放位置）、
Packer（自动将控件填充到合适的位置）和Grid（基于网格坐标来摆放控件），此处不进行赘述。
'''