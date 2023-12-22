import WAAPI as wa

def createRandm(audioname, parent):
    # 创建一个随机容器对象
    audioname = audioname.replace(" ", "_")
    args = {
        "parent": parent,
        "type": "RandomSequenceContainer",
        "name": audioname
    }
    return wa.client.call("ak.wwise.core.object.create", args)

def Move(object, parent):
    # 移动对象到指定的父级
    args = {
        "object": object,
        "parent": parent
    }
    return wa.client.call("ak.wwise.core.object.move", args)

with wa.client:
    # 获取选中的音频对象
    get = wa.get_audio_getSelectedObjects()
    allname = []
    
    # 获取所有音频对象的前缀
    for Objects in get:
        print(wa.get_children(Objects["id"])["return"])
        for i in wa.get_children(Objects["id"])["return"]:
            
            if i["name"][:-3] not in allname:
                allname.append(i["name"][:-3])

    allRandm = []

    # 为共同前缀的音频对象创建一个随机容器对象
    for i in allname:
        randm = createRandm(i, get[0]["id"])
        allRandm.append(randm)
    print(allname)
    # 将音频对象移动到对应的随机容器对象中
    for Objects in get:
        for i in wa.get_children(Objects["id"])["return"]:
            print(i["name"])
            if i["name"][:-3] in allname:
                Move(i["id"], allRandm[allname.index(i["name"][:-3])]["id"])

#[:-3]是因为命名格式（例Player_Run_01,[:-3]为Player_Run）