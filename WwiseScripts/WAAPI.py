import waapi
import os

import time
from functools import wraps
def time_this_function(func):
    #作为装饰器使用，返回函数执行需要花费的时间
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper


def get_audio_getSelectedObjects():

    getopts = {
        "return": [
            "name",
            "path",
            "id",
            "type"
        ]
    }

    getResult = {
    }

    return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)['objects']
@time_this_function
def setVolume(id,v):
    args ={
         
        
        "object": id,
        
        "property": "Volume", 
        "value": v,    
    }

    return client.call("ak.wwise.core.object.setProperty", args)

def setObj(id,v):
    args ={
         "objects": [
        {
            "object": id,
            
            "@Weight": v,
            

        }]
        
        
        
       
    }

    return client.call("ak.wwise.core.object.set", args)

def setProperty(id,V):
    args ={

        "object": id,
        
        "property": "Weight", 
        "value": V,    
    }

    return client.call("ak.wwise.core.object.setProperty", args)


def get_event_getSelectedObjects():

    getopts = {
        "return": [
            "name",
            "path",
            "id",
            "type"
        ]
    }

    getResult = {
    }

    return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)
def createPlayEvent(audioname,auidoid,parent):
    # newEvent="Play_"+audioname
    # if oldEvent == newEvent:
    #     print(newEvent+"已存在")
    #     return
    audioname = audioname.replace(" ", "")
    args = {
        "parent": parent,
        "type": "Event",
        "name": "Play_"+audioname,  
        "children": [
        {
            "type": "Action",
            "name": "",
            "@ActionType": 1,
            "@Target": auidoid
            # "@FadeTime": FadeTime,
            # "@Delay": Delay
        }
        ]
    }
    return client.call("ak.wwise.core.object.create", args)


def copyAudio(auidoid,parent):

    args = {
        "parent": parent,
        "object": auidoid
        
    }
    return client.call("ak.wwise.core.object.copy", args)


def createStopEvent(audioname,auidoid,parent):
    # newEvent="Stop_"+audioname
    # if oldEvent == newEvent:
    #     print(newEvent+"已经存在")
    #     return
    audioname = audioname.replace(" ", "")
    args = {
        "parent": parent,
        "type": "Event",
        "name": "Stop_"+audioname,  
        "children": [
        {
            "type": "Action",
            "name": "",
            "@ActionType": 2,
            "@Target": auidoid
            # "@FadeTime": FadeTime,
            # "@Delay": Delay
        }
        ]
    }
    return client.call("ak.wwise.core.object.create", args)


def getchildrenName(id):
    args = {
        "from": {
            "id": [
                id
            ]
        },
        "transform": [
            {"select": ['children']}
        ]

    }
    
    opts = {
        "return": [
            "name",
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)["return"][0]['name']

def getAllSub(path):
    Dirlist = []
    Filelist = []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            if os.path.splitext((filename))[-1] == ".wav":
                Filelist.append(os.path.join(home, filename))
    return Dirlist, Filelist

def check_all_elements_in_string(string_list, target_string):
    # 使用 all 函数和列表推导式来检查
    return all(element in target_string for element in string_list)


def check_if_children_are_containers(children):
    # 获取子对象
    
    for child in children["return"]:

        obj_type = child["type"]
        # 检查是否是容器类型
        if obj_type in ['WorkUnit', 'Folder', 'ActorMixer', 'RandomSequenceContainer', 'SwitchContainer', 'BlendContainer']:
            return True

        return False

def get_obj(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        }
    }


    opts = {
        "return": [
            "name","id","type","path","@Weight"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)


def get_children(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        },
        "transform": [
            {"select": ['children']}
        ]
    }


    opts = {
        "return": [
            "name","id","type","path"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)

def Iscontainer(object_id):
    Istype=get_audiotype(object_id)
    if (Istype =="RandomSequenceContainer")|(Istype=="SwitchContainer")|(Istype=="BlendContainer"):
        return True
    else:
        return False 

def getInclusions(id):

    getopts ={
        "soundbank":id
    }

    getResult = {
    }

    return client.call("ak.wwise.core.soundbank.getInclusions",getopts)
    


def get_descendants(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        },
        "transform": [
            {"select": ['descendants']}
        ]
    }


    opts = {
        "return": [
            "name","id","type","path","@Weight"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)



def get_parent(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        },
        "transform": [
            {"select": ['parent']}
        ]
    }


    opts = {
        "return": [
            "name","id","type","path","parent"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)['return']

def get_audiotype(sound_sfx_guid):

    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        }
    }


    opts = {
        "return": [
            "name","id","type","path"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)["return"][0]['type']

def extract_name(s):
    # 分割字符串，限定分割次数为最后一个下划线之前
    parts = s.rsplit('_', 1)
    # 返回分割后的第一个部分
    return parts[0] if len(parts) > 1 else s

def CEvent(ObjectsName1,ObjectsId1,parent1,S):
    #print(get_children(id)["return"][0]['name'])
    
    if isLoop(ObjectsId1):
        if S == "PS":
            createPlayEvent(ObjectsName1,ObjectsId1,parent1)
            createStopEvent(ObjectsName1,ObjectsId1,parent1)
        elif S == "XS":
            createStopEvent(ObjectsName1,ObjectsId1,parent1)
        else:
            createPlayEvent(ObjectsName1,ObjectsId1,parent1)
            
    else:
        if S == "PS":
            createPlayEvent(ObjectsName1,ObjectsId1,parent1)  
        if S == "PX":
            createPlayEvent(ObjectsName1,ObjectsId1,parent1)

def isLoop(id):
    #print(get_children(id)["return"][0]['name'])
    if "_LP_" in get_children(id)["return"][0]['name']:
        
        return True
    else:
        return False


def getchildrenCount(id):
    args = {
        "from": {
            "id": [
                id
            ]
        }
    }
    opts = {
        "return": [
            "childrenCount",
        ]
    }
    return client.call("ak.wwise.core.object.get", args, options=opts)["return"][0]['childrenCount']

client = waapi.WaapiClient(url="ws://127.0.0.1:8080/waapi")
