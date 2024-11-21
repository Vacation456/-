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


