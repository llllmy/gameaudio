from waapi import WaapiClient
import re
def get_sfx_getSelectedObjects():

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

def get_sfx_getSelectedObjectsE():

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

def getchildrenName(id):
    args = {
        "from": {
            "id": [
                id
            ]
        }

    }
    
    opts = {
        "return": [
            "name",
        ]
    }
    
    return client.call("ak.wwise.core.object.get", args, options=opts)["return"][0]['name']


def createPlayEvent(audioname,auidoid,parent):
    args = {
        "parent": parent,
        "type": "Event",
        "name": "Play_"+audioname, 
        "autoAddToSourceControl": True, 
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

def createStopEvent(audioname,auidoid,parent):
    args = {
        "parent": parent,
        "type": "Event",
        "name": "Stop_"+audioname,  
        "autoAddToSourceControl": True, 
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

def isLoop(id):
    print(get_children(id)["return"][0]['name'])
    if "_LP_" in get_children(id)["return"][0]['name']:
        
        return True
    else:
        return False

def CeaLP(ObjectsName1,ObjectsId1,parent1):
    print(get_children(id)["return"][0]['name'])
    if isLoop(ObjectsId1):
        createPlayEvent(ObjectsName1,ObjectsId1,parent1)
        createStopEvent(ObjectsName1,ObjectsId1,parent1)
    else:
        createPlayEvent(ObjectsName1,ObjectsId1,parent1)  


def check_pattern(string2):
    pattern = r'^\d.*'
    match = re.search(pattern, string2)

    if match:
        last_underscore_index = string2.rfind("_")  # 查找最后一个 "_" 的索引位置
        substring = string2[last_underscore_index:]  # 获取索引位置之前的子字符串
        return substring
    else:
        return ""
    
    

client = WaapiClient(url="ws://127.0.0.1:8070/waapi")
while True:
    input('这条信息后选择音频(Audio)位置后按Enter:')
    get = get_sfx_getSelectedObjects()
    if get["objects"][0]["path"][:6] != "\Actor":
        print("选择的不是音频对象")
        continue
    else:
        break
while True:
    input('这条信息后选择事件(Events)位置后按Enter:')
    getE = get_sfx_getSelectedObjectsE()["objects"][0]["path"]
    print(getE)
    if getE[:6] != "\Event":
        print("选择的不是事件对象")
        continue
    else:
        break


if __name__ == "__main__":
#print(type(getE))
#print(get["objects"][0]["path"])
    parent = "\\Events\\Elemental\\Energy\\Earthquake\\Earthquake_3L_A"
    parent = getE
    for Objects in get["objects"]:
        ObjectsName = Objects["name"]
        ObjectsPath = Objects["path"]
        ObjectsId = Objects["id"]
        ObjectsType = Objects["type"]

        pattern = r'([^_]+)_\d+$'
        #print("getchildrenName"+getchildrenName(ObjectsId))
        if (getchildrenCount(ObjectsId)>0)|(get_audiotype(ObjectsId) != "Sound"):
            if get_audiotype(ObjectsId) == "RandomSequenceContainer":
                

                match = re.search(pattern, getchildrenName(ObjectsId))
                if match:
                    name = getchildrenName(ObjectsId).rsplit('_', 1)[0]
                else:
                    name = getchildrenName(ObjectsId)
                CeaLP(name,ObjectsId,parent)
            for Objects1 in get_children(ObjectsId)['return']:
                if (getchildrenCount(Objects1["id"])>0)|(get_audiotype(Objects1["id"]) != "Sound"):
                    if get_audiotype(Objects1["id"]) == "RandomSequenceContainer":

                        match = re.search(pattern, getchildrenName(Objects1["id"]))
                        if match:
                            name = getchildrenName(Objects1["id"]).rsplit('_', 1)[0]
                        else:
                            name = getchildrenName(Objects1["id"])

                        CeaLP(name,Objects1,parent)
                    for Objects2 in get_children(Objects1["id"])['return']:
                        #pprint(Objects2["name"])
                        if (getchildrenCount(Objects2["id"])>0)|(get_audiotype(Objects2["id"]) != "Sound"):
                            if get_audiotype(Objects2["id"]) == "RandomSequenceContainer":

                                match = re.search(pattern, getchildrenName(Objects2["id"]))
                                if match:
                                    name = getchildrenName(Objects2["id"]).rsplit('_', 1)[0]
                                else:
                                    name = getchildrenName(Objects2["id"])


                                CeaLP(name,Objects2["id"],parent)
                            for Objects3 in get_children(Objects2["id"])['return']:
                                if (getchildrenCount(Objects3["id"])>0)|(get_audiotype(Objects3["id"]) != "Sound"):
                                    if get_audiotype(Objects3["id"]) == "RandomSequenceContainer":

                                        match = re.search(pattern, getchildrenName(Objects3["id"]))
                                        if match:
                                            name = getchildrenName(Objects3["id"]).rsplit('_', 1)[0]
                                        else:
                                            name = getchildrenName(Objects3["id"])


                                        CeaLP(name,Objects3["id"],parent)
                                    for Objects4 in get_children(Objects3["id"])['return']:
                                        if (getchildrenCount(Objects4["id"])>0)|(get_audiotype(Objects4["id"]) != "Sound"):
                                            if get_audiotype(Objects4["id"]) == "RandomSequenceContainer":

                                                
                                                match = re.search(pattern, getchildrenName(Objects4["id"]))
                                                if match:
                                                    name = getchildrenName(Objects4["id"]).rsplit('_', 1)[0]
                                                else:
                                                    name = getchildrenName(Objects4["id"])

                                                CeaLP(name,Objects4["id"],parent)


    client.disconnect()