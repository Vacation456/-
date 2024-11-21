## 我的python课程设计：链接数据库端口

###### 前期准备：

1.安装好pymssql库

2.配置好Sql Sever端口

3.在py文件中导入数据库

4.在数据库中建立自己需要的表格



## 一.  配置数据库端口具体操作

~~~电脑身份登录Sql sever management，服务器名称需要记住（在pycharm中会用到）

~~~

**找到对象资源管理器的第一个，单击鼠标右键后出现以下页面：**



**点击属性，进入页面后点击安全性，会出现：**



**服务器身份验证选中第二个（SQL Sever 和Window 身份验证）模式之后点击确定。**

**步骤二：建立一个空数据库，并且建立一个专属用户**
**建立专属用户和空数据库的原因是防止以后对数据库操作失误时影响到其它的数据库。**

**首先需要点击新建查询并且执行以下操作：**

**create database soft2104**
**执行会出现一个soft2104的新数据库（soft2104我的数据库名称，后续需要放在pycharm里）**

**如果你觉得数据库难听可以执行如下操作进行删除数据库：（不过需要新建一个数据库）**

**use master --删数据库**
**drop database soft2104 --删数据库** 
**建立好数据库后双击安全性：**



 **双击登录名后点击鼠标右键，点击新建登录名：**



**编辑一个登录名（yu这个是我的用户名，后续需要放在pycharm里）**



**接下来点击SQL Sever 身份验证输入密码，随便起一个密码，忘了可以再更改。在这里我就用123456代替（123456是我的密码，后续需要放在pycharm里）。**

 **接下来把强制实施密码策略的对号给点掉（不然后来会遇到各种登录问题）**



 **变成这样：**



**点击用户映射，将你的数据库打勾：**



**将下边的db_ower对勾选中：**



 **点击确定，之后进行验证：**



 **点击电脑和叉的标志退出服务器断开连接，之后点击电脑和绿线的标志连接服务器**

**** 

**点击SQL Sever 身份验证输入账号密码如果成功的连接，就会进入数据库，你只能对你用户对应下的数据库进行各种操作：**

**** 

 **如果你的SQL Sever没有打开密码功能就会出现以下提示：**

**标题: 连接到服务器 ------------------------------  无法连接到 LAPTOP-40O6HVDS。  ------------------------------ 其他信息:  已成功与服务器建立连接，但是在登录过程中发生错误。 (provider: Shared Memory Provider, error: 0 - 管道的另一端上无任何进程。) (Microsoft SQL Server，错误: 233)**  

**步骤三：打开1433 端口**
**首先需要检测自身的 1433 端口是否打开（一般默认的都是关闭的需要自己打开）**

**1433应该是电脑的一个端口，可以链接电脑的（其实不需要知道是什么）**

**点击：win和R，输入cmd点击回车出现如下界面：**



**输入telnet localhost  1433并点击回车**

**一般会出现一下错误：**

**'telnet' 不是内部或外部命令，也不是可运行的程序**

**解决办法：**

**点击：win和R，输入control点击回车出现如下界面：**



**点击程序（不要点到卸载程序）**



 **点击启动或关闭Windows 功能**



**将Telnet客户端对号选中，点击确定，会经过大概1分钟左右的等待页面**

**再次重复win和R，输入cmd点击，输入telnet localhost  1433并点击回车出现以下错误：**

**正在连接localhost...无法打开到主机的连接。 在端口 1433: 连接失败**

**（你已经成功了一半了）**

**打开以下程序：**



**找不到就在搜索框里输入sql**

**** 

 **打开之后会出现以下界面：**



 **禁用所有上述出现的程序（必须先这么做）**

**点击SQL Sever网络配置，然后点击MSSQLSEVER的协议：**



 **双击这个TCP/IP，进入之后将TCP/IP的启用改为 是**



**点击IP地址：**



 **将IP1、IP2的启用改为是，观察TCP端口是不是1433。（一共改两个）**



**往下滑出现IPAll，观察其TCP端口是不是1433，最后别忘记点应用（不是点击确定）。**



 **经过上述操作后重启电脑，重新打开该软件，然后再将下边的东西改成启动，SQL Sever代理启动失败与否不会影响SQL Sever的使用。**



**点击：win和R，输入cmd点击回车，并在其中输入telnet localhost  1433 当页面跳转到以下页面则说明你的1433配置成功：**

**空**



## 二.具体的python代码

```python
"""------------------------ 餐饮管理系统 ------------------------"""

import pymssql
from tkinter import *


def TianjiaZhuoTai(TableNumber, TableRongliang, TableZhuangTai, TableWeizhi):  # 添加桌台，sql 更改

    tablenumber = int(TableNumber)
    tablerongliang = int(TableRongliang)
    tablezhuangtai = TableZhuangTai
    tableweizhi = TableWeizhi

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')  # 连接数据库，  选项别为：服务器名,账户,密码,数据库名
    cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行

    sql = """insert into 桌台(TableNumber,TableRongliang,TableZhuangTai,TableWeizhi) values ('%d','%d','%s','%s')"""  # 对 "订单细节"表格进行 添加数据
    sql = sql % (tablenumber, tablerongliang, tablezhuangtai, tableweizhi)  # 使用参数替代

    cursor.execute(sql)  # 执行sql语句
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


def ShanChuZhuoTai(Number):  # 删除桌台，主要进行 更改
    number = int(Number)
    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    cursor.execute("delete from 桌台 where TableNumber ={}".format(number))
    connect.commit()
    cursor.close()
    connect.close()


def ZhuoTai():
    global winNew# 桌台管理     管理员对桌台进行 增删 管理
    winNew = Toplevel(root)
    winNew.geometry('580x540')
    winNew.title('桌台管理')

    lb1 = Label(winNew, text="当前桌台信息如下：")
    lb1.pack()
    lb2 = Label(winNew, text="")
    lb2.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select * from 桌台"
    cursor.execute(sql)
    row = cursor.fetchone()
    S = "桌台号     桌台容量 桌台状态 所在楼层   " + '\n'  # 定义一个字符串
    while row:  # 循环读取所有结果
        S = S + str(row) + '\n'
        row = cursor.fetchone()
    lb2.config(text=S)

    lb8 = Label(winNew, text="请输入要添加的桌台号：")
    lb8.pack()
    entry0 = Entry(winNew)  # 输入框
    entry0.pack()

    lb4 = Label(winNew, text="请输入要添加的桌台容量：")
    lb4.pack()
    entry1 = Entry(winNew)  # 输入框
    entry1.pack()

    lb5 = Label(winNew, text="请输入添加的桌台状态：")
    lb5.pack()
    entry2 = Entry(winNew)  # 输入框
    entry2.pack()

    lb6 = Label(winNew, text="请输入添加的桌台位置：")
    lb6.pack()
    entry3 = Entry(winNew)  # 输入框
    entry3.pack()

    lb3 = Label(winNew, text="请输入需要删除的桌台号：")
    lb3.pack()
    entry4 = Entry(winNew)  # 输入框
    entry4.pack()

    btn1 = Button(winNew, text='确认添加',
                  command=lambda: TianjiaZhuoTai(entry0.get(), entry1.get(), entry2.get(), entry3.get()))
    btn1.pack()
    btn2 = Button(winNew, text='确认删除', command=lambda: ShanChuZhuoTai(entry4.get()))
    btn2.pack()
    btClose = Button(winNew, text='退出', command=winNew.destroy)
    btClose.pack()


def TianjiaCaiPing(CaiNumber, CaiName, FenLiang, Price):  # 管理员添加菜品

    cainumber = int(CaiNumber)
    cainame = CaiName
    fenliang = FenLiang
    price = int(Price)

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')  # 连接数据库，  选项别为：服务器名,账户,密码,数据库名
    cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行

    sql = """insert into 菜品(CaiNumber,CaiName,Fenliang,Price) values ('%d','%s','%s','%d')"""  # 对 "订单细节"表格进行 添加数据
    sql = sql % (cainumber, cainame, fenliang, price)  # 使用参数替代

    cursor.execute(sql)  # 执行sql语句
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


def ShanChuCaiPing(Number):  # 输入订单菜品号，管理员删除菜品
    number = int(Number)
    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    cursor.execute("delete from 菜品 where  CaiNumber ={}".format(number))
    connect.commit()
    cursor.close()
    connect.close()


def CaiDan():  # 菜单管理
    winNew = Toplevel(root)
    winNew.geometry('590x560')
    winNew.title('菜单管理')
    lb1 = Label(winNew, text="当前菜品信息如下：")
    lb1.pack()
    lb2 = Label(winNew, text="")
    lb2.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select * from 菜品"
    cursor.execute(sql)
    row = cursor.fetchone()
    S = "菜品号     菜名      份量          价格   " + '\n'  # 定义一个字符串
    while row:  # 循环读取所有结果
        S = S + str(row) + '\n'
        row = cursor.fetchone()
    lb2.config(text=S)

    lb3 = Label(winNew, text="请输入菜品号：")
    lb3.pack()
    entry1 = Entry(winNew)  # 输入框
    entry1.pack()
    lb4 = Label(winNew, text="请输入菜名：")
    lb4.pack()
    entry2 = Entry(winNew)  # 输入框
    entry2.pack()

    lb5 = Label(winNew, text="请输入份量：")
    lb5.pack()
    entry3 = Entry(winNew)  # 输入框
    entry3.pack()

    lb6 = Label(winNew, text="请输入价格：")
    lb6.pack()
    entry4 = Entry(winNew)  # 输入框
    entry4.pack()

    lb7 = Label(winNew, text="请输入需要删除的菜品号：")
    lb7.pack()
    entry5 = Entry(winNew)  # 输入框
    entry5.pack()

    btn1 = Button(winNew, text='确认添加',
                  command=lambda: TianjiaCaiPing(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    btn1.pack()
    btn2 = Button(winNew, text='确认删除', command=lambda: ShanChuCaiPing(entry5.get()))
    btn2.pack()
    btClose = Button(winNew, text='退出', command=winNew.destroy)
    btClose.pack()


def YingYeErJiSuan():  # 直接计算营业总额，分时间段查看营业额以后再完善

    lb3 = Label(winNew, text="您当前订单需支付金额为：")
    lb3.pack()
    lb4 = Label(winNew, text="")  # 显示金额
    lb4.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select SUM(FinalPay) from 订单细节"
    cursor.execute(sql)
    row = cursor.fetchone()  # 不能强制转换为 int 类型
    lb4.config(text=row)
    lb5 = Label(winNew, text="元")  # 显示金额
    lb5.pack()
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    btClose = Button(winNew, text='点击关闭', command=winNew.destroy)
    btClose.pack()


def YingYeEr():  # 营业额管理

    winNew = Toplevel(root)
    winNew.geometry('340x200')
    winNew.title('营业额管理')
    lb3 = Label(winNew, text="当前营业总额为：\n")
    lb3.pack()

    lb4 = Label(winNew, text="")
    lb4.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select SUM(FinalPay) from 订单细节"
    cursor.execute(sql)
    row = cursor.fetchone()  # 不能强制转换为 int 类型
    lb4.config(text=row)
    lb5 = Label(winNew, text="元\n")  # 显示金额
    lb5.pack()
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    btClose = Button(winNew, text='点击关闭', command=winNew.destroy)
    btClose.pack()


def ZhangYongTai(Number):  # 删除桌台，主要进行 更改
    number = int(Number)
    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    cursor.execute("update 桌台 set TableRongliang=TableRongliang-1 where TableNumber ={}".format(number))
    connect.commit()
    cursor.close()
    connect.close()


def KaiTai():  # 开台
    winNew = Toplevel(root)
    winNew.geometry('550x340')
    winNew.title('开台管理')
    lb3 = Label(winNew, text="桌台信息如下：")
    lb3.pack()
    lb2 = Label(winNew, text="")
    lb2.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select * from 桌台"
    cursor.execute(sql)
    row = cursor.fetchone()
    S = "桌台号 容量 状态      位置   " + '\n'
    while row:  # 循环输出，当前桌台的情况，剩余位置等
        S = S + str(row) + '\n'
        row = cursor.fetchone()
    lb2.config(text=S)
    lb4 = Label(winNew, text="请选择相关人数的桌台号：")
    lb4.pack()
    entry1 = Entry(winNew)
    entry1.pack()
    btn1 = Button(winNew, text='点击确认',
                  command=lambda: ZhangYongTai(entry1.get()))  # 顾客确认后，表示当前桌台已有人占有，故 减一，  sql 删除
    btn1.pack()
    cursor.close()
    connect.close()
    btClose = Button(winNew, text='关闭', command=winNew.destroy)
    btClose.pack()


def DingDanXiJie(DingDanNumber, DetailNumber, CaiPingNumber, ShuLiangNumber, CaiPingPrice):  # 订单细节，也是点餐，添加餐

    dingdannumber = DingDanNumber
    detail = DetailNumber  # 主要进行格式转换
    caipingnumber = CaiPingNumber
    shuliangnumber = int(ShuLiangNumber)
    caipingprice = int(CaiPingPrice)
    finapay = shuliangnumber * caipingprice

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')  # 连接数据库
    cursor = connect.cursor()

    sql = """insert into 订单细节(OrderNumber,OrderXijieNumber,CaipinNumber,CaipinShuliang,CaipinMoney,FinalPay) values (%s,%s,%s,%d,%d,%d)"""  # 对 "订单细节"表格进行 添加数据
    sql = sql % (dingdannumber, detail, caipingnumber, shuliangnumber, caipingprice, finapay)  # 使用参数替代

    cursor.execute(sql)  # 执行sql语句
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


def ShanChuDingDanXijie(Number, Xijienumber):  # 输入订单细节号，删除刚刚添加到订单细节表格的 菜
    number = int(Number)
    xijienumber = int(Xijienumber)
    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    cursor.execute("delete from 订单细节 where  OrderNumber ={} and OrderXijieNumber = {} ".format(number, xijienumber))
    connect.commit()
    cursor.close()
    connect.close()


def DianCan():  # "点餐"窗口及其内容
    winNew = Toplevel(root)
    winNew.geometry('650x630')
    winNew.title('点餐管理')
    lb3 = Label(winNew, text="菜品信息如下：")
    lb3.pack()
    lb2 = Label(winNew, text="")
    lb2.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select * from 菜品"  # 打印出"菜品"表格，让客户便于选择菜色
    cursor.execute(sql)
    row = cursor.fetchone()
    S = "菜品号   菜名    份量          价格   " + '\n'
    while row:  # 循环读取出表格内容
        S = S + str(row) + '\n'
        row = cursor.fetchone()
    lb2.config(text=S)

    lb8 = Label(winNew, text="请输入订单号：")
    lb8.pack()
    entry0 = Entry(winNew)  # 输入框
    entry0.pack()

    lb4 = Label(winNew, text="请输入订单细节号：")
    lb4.pack()
    entry1 = Entry(winNew)  # 输入框
    entry1.pack()

    lb5 = Label(winNew, text="请选择菜品号：")
    lb5.pack()
    entry2 = Entry(winNew)  # 输入框
    entry2.pack()

    lb6 = Label(winNew, text="请选择菜品数量：")
    lb6.pack()
    entry3 = Entry(winNew)  # 输入框
    entry3.pack()

    lb7 = Label(winNew, text="请输入菜品单价：")
    lb7.pack()
    entry4 = Entry(winNew)  # 输入框
    entry4.pack()

    btn1 = Button(winNew, text='确认添加',
                  command=lambda: DingDanXiJie(entry0.get(), entry1.get(), entry2.get(), entry3.get(),
                                               entry4.get()))  # 将顾客的点餐细节添加到 "订单细节表"中，每个顾客有一个订单细节分组
    btn1.pack()

    btClose = Button(winNew, text='确认取消',
                     command=lambda: ShanChuDingDanXijie(entry0.get(), entry1.get()))  # 输入订单号和细节号
    btClose.pack()

    btClose = Button(winNew, text='退出', command=winNew.destroy)
    btClose.pack()
    lb7 = Label(winNew,
                text="(注：可重复添加,每个顾客的订单号要一样，同一个顾客每次添加的细节号不能一样\n取消已添加的菜品，需输入订单号和订单细节号)")  # 备注
    lb7.pack()
    cursor.close()
    connect.close()


def ShowMoney(Number):
    number = int(Number)
    winNew = Toplevel(root)
    winNew.geometry('230x120')
    winNew.title('订单金额')
    lb3 = Label(winNew, text="您当前订单需支付金额为：")
    lb3.pack()
    lb4 = Label(winNew, text="")  # 显示金额
    lb4.pack()

    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    sql = "select SUM(FinalPay) from 订单细节 where OrderNumber = {}".format(number)
    cursor.execute(sql)
    row = cursor.fetchone()  # 不能强制转换为 int 类型
    lb4.config(text=row)
    lb5 = Label(winNew, text="元")  # 显示金额
    lb5.pack()
    connect.commit()  # 提交
    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    btClose = Button(winNew, text='点击关闭', command=winNew.destroy)
    btClose.pack()


def ShiFangTai(Number):  # 释放桌台，客人走后
    number = int(Number)
    connect = pymssql.connect('VACATION0114', 'yu', '123456', 'soft2104')
    cursor = connect.cursor()
    cursor.execute("update 桌台 set TableRongliang=TableRongliang+1 where TableNumber ={}".format(number))
    connect.commit()
    cursor.close()
    connect.close()


def JieZhang():  # 结账
    winNew = Toplevel(root)
    winNew.geometry('350x210')
    winNew.title('查看账单')
    lb8 = Label(winNew, text="请输入订单号查看账单：")
    lb8.pack()

    entry9 = Entry(winNew)  # 输入框
    entry9.pack()

    lb9 = Label(winNew, text="请输入桌台号完成消费：")
    lb9.pack()

    entry0 = Entry(winNew)  # 输入框
    entry0.pack()

    btC = Button(winNew, text='查看账单', command=lambda: ShowMoney(entry9.get()))
    btC.pack()
    btC1 = Button(winNew, text='完成支付', command=lambda: ShiFangTai(entry0.get()))
    btC1.pack()
    btClose = Button(winNew, text='关闭', command=winNew.destroy)
    btClose.pack()


def GengXin():  # 系统维护
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('关于餐饮管理系统')
    lb = Label(winNew, text="\n\n\n当前已为最新版本\n\nEMUI 6.0\n")
    lb.pack()
    btClose = Button(winNew, text='点击关闭', command=winNew.destroy)
    btClose.pack()


root = Tk()  # 根窗口
root.geometry('780x366')
root.title('餐饮管理系统')

photo = PhotoImage(file='D:/liulanqidownloads/猫头2.gif ')
photoLabel = Label(root, text="欢迎光临老八餐厅", justify=LEFT, image=photo, compound=CENTER, font=("华文行楷", 30),
                   fg="black")
photoLabel.pack()

mainmenu = Menu(root)  # 给根窗体添加个菜单

GuanLimenu = Menu(mainmenu, tearoff=0)  # 这个是菜单的 "选项"
mainmenu.add_cascade(label='管理员入口', menu=GuanLimenu)
GuanLimenu.add_command(label="桌台管理", command=ZhuoTai)  # 对桌台增删
GuanLimenu.add_command(label="菜单管理", command=CaiDan)  # 对菜单增删
GuanLimenu.add_command(label="营业额管理", command=YingYeEr)  # 计算营业额

GuKemenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='顾客入口', menu=GuKemenu)
GuKemenu.add_command(label="开台", command=KaiTai)  #
GuKemenu.add_command(label="点餐", command=DianCan)
GuKemenu.add_command(label="结账", command=JieZhang)  #

XiTongmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='系统维护', menu=XiTongmenu)
XiTongmenu.add_command(label="退出程序", command=root.destroy)  # 关闭程序
XiTongmenu.add_command(label="系统更新", command=GengXin)  # 关闭程序

root.config(menu=mainmenu)  # 对所产生的菜单进行显示
root.mainloop()



```

出现问题：由于这是借鉴别人的代码，因此出现一个问题，winNew被多个函数所使用，而并未正确声明，出现此问题原因可能为原作者的python版本和我的不一样。

解决方法：在ZhuoTai函数下将winNew声明为全局变量。



代码打完后还需链接数据库端口，具体操作为（按照图片依次点击）：

![image-20241121233047644](C:\Users\29396\AppData\Roaming\Typora\typora-user-images\image-20241121233047644.png)

![image-20241121233134972](C:\Users\29396\AppData\Roaming\Typora\typora-user-images\image-20241121233134972.png)

![image-20241121233204697](C:\Users\29396\AppData\Roaming\Typora\typora-user-images\image-20241121233204697.png)

#### 此页登录名按照自己创建的登录名和密码来，按照我的就是User:yu    Password:123456，准备就绪后点击apply



## 三.接下来为SQL Sever management里的具体操作：

#### 此次设计仅仅需要创建基本表，因此我直接说操作：

1.点击数据库

2.展开自己创建的数据库，我的就是soft2104

3.右键点击表，新建

4.为各个需要用到的表创建列名，一般为了减少报错，我推荐都允许NULL值，更具实际需要调整

5.步骤4的操作也可以使用新建查询使用查询语言实现



#### 数据库如何配置前文已经提到过，这里不再赘述

#### 注意：此次设计数据库配置以及基本表的创建应当在python代码实现之前完成