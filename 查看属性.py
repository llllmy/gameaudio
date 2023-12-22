from waapi import WaapiClient
from pprint import pprint
#import object_data

from tkinter import *


def on_name_changed(*args, **kwargs):

    obj_type = kwargs.get("object", {}).get("type")

    old_name = kwargs.get("oldName")

    new_name = kwargs.get("newName")

    print(f"Object {old_name} (of type {obj_type}) was renamed to {new_name}\n")
    pprint(kwargs.get("object", {}))
    # client.disconnect()


def on_object_created(*args, **kwargs):
    object_selected = kwargs.get("object")
    object_id = object_selected.get('id')
    #object_type = object_selected.get('type')
    #object_parent = object_selected.get('parent')

    #pprint(kwargs)

    pprint(f'New Object created ID: {object_id}')
object_type = None
object_name = None
object_parent= None
object_id =None
def on_object_selected(*args, **kwargs):
    global object_type
    global object_name
    global object_parent

    object_selected = kwargs.get("objects")[0]
    object_id = object_selected.get('id')
    object_name = object_selected.get("name")
    #object_type = object_selected.get('type')
    #object_parent = object_selected.get('parent')
    #canvas.itemconfig(itext,text=str(object_name))
    #pprint(kwargs)
    a = "123"
    tk.update()
    #a1 = f'Object selected is of type: {object_type}, \n ID of the object: {object_id}, \n Parent: {object_parent}'
    #pprint(f'Object selected is of type: {object_type}, \n ID of the object: {object_id}, \n Parent: {object_parent}')
    #return object_id


#if __name__ == '__main__':
    '''
    handler_name = client.subscribe(
        "ak.wwise.core.object.nameChanged", 
        on_name_changed, 
        {"return": ["type", 'parent']}
    )
    '''
    '''
    handler_create = client.subscribe(
        "ak.wwise.core.object.created",
        on_object_created,
        {"return": ["id"]}
    )
    '''
    #'''
   
    #'''

if __name__ == '__main__':
    li = []
    li1 = []
    li2 = []
    with WaapiClient() as client: 
        args = {
            "from": {
                "ofType": [
                    "Sound"
                ]
            }
        
        }


        opts = {
            "return": [
                "name","id","type","path","@Volume"
            ]
        }

        name= client.call("ak.wwise.core.object.get", args, options=opts)["return"]
        #print((name))
        for item in name: 
            if item["@Volume"] < 0:
                               # 第一个小部件插入数据
                li.append(item["name"].ljust(100)+str(item["@Volume"]).rjust(20))
                # li1.append(item["path"]) 
                # li2.append(str(item["@Volume"]))  
    tk=Tk()

    #canvas=Canvas(tk,width=1500,height=500)
    #canvas.pack()
    #tk.update()
   
    
    listb  = Listbox(tk,width=250,height=50)
    # listb1  = Listbox(tk,width=100,height=50)
    # listb2  = Listbox(tk,width=10,height=50)
    for item in li:                 # 第一个小部件插入数据
        listb.insert(0,item)
    # for item in li1:                 # 第一个小部件插入数据
    #     listb1.insert(0,item)
    # for item in li2:                 # 第一个小部件插入数据
    #     listb2.insert(0,item)

    num=0 
    listb.pack(side='left') 
    
    
    # listb1.pack(side='left')  
    # listb2.pack(side='right')    
   # itext=canvas.create_text(500,30,text=str(object_id))
    tk.mainloop()
    # while num<100000:
    #     num +=1
    #     #canvas.itemconfig(itext,text=str(object_type))
    #     #canvas.insert(itext,12,'')
    #     #tk.update()
    #     #print('num=%d'%num)
    #     print(object_type)
        #tk.after(100)
    