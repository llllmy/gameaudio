#!/usr/bin/python
# -*- coding: UTF-8 -*-
from waapi import WaapiClient
import get
from tkinter import * 
root = Tk() 
client = WaapiClient()                 # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
handler_select = client.subscribe(
        "ak.wwise.ui.selectionChanged",
        get.on_object_selected,
        {"return": ["type", "id", "parent"]}
    )
print((handler_select))
movie  = [{handler_select},'jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环