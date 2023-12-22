import waapi
import re
import WAAPI as wa
#from pprint import pprint

# 连接到Waapi
#client = waapi.WaapiClient(url="ws://127.0.0.1:8080/waapi")
class bcolors:
    HEADER = '\x1b[95m'
    OKBLUE = '\x1b[94m'
    OKCYAN = '\x1b[96m'
    OKGREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    UNDERLINE = '\x1b[4m'


get = wa.get_audio_getSelectedObjects()



EventCh = wa.get_children(getE["id"])
oldEvents=[]
for e in EventCh["return"]:
    #print(e["name"])
    oldEvents.append(e["name"])
#print(oldEvents)
CCoutTrue=0
CCoutFalse=0
for Objects in get:

    ObjectsName = Objects["name"]
    ObjectsPath = Objects["path"]
    ObjectsId = Objects["id"]
    ObjectsType = Objects["type"]
    if wa.Iscontainer(wa.get_parent(ObjectsId)[0]["id"])==False:
        if wa.Iscontainer(ObjectsId):
            if wa.getchildrenCount(ObjectsId)>0:
                if ObjectsName == wa.getchildrenName(ObjectsId):
                    cname=ObjectsName
                else:
                    cname=wa.extract_name(wa.getchildrenName(ObjectsId))
                if wa.extract_name(wa.getchildrenName(ObjectsId)) in ObjectsName:
                    CEvt = False
                    CA = "P"
                    CB = "S"
                    if (("Play_"+cname) in oldEvents):
                        print('\x1b[1;31;40m'+"Play_"+cname+"事件已存在|"+ObjectsPath+ '\x1b[0m')
                        CCoutFalse+=1
                        CEvt =True
                    if (("Stop_"+cname) in oldEvents):
                        print('\x1b[1;31;40m'+"Stop_"+cname+"事件已存在|"+ObjectsPath+ '\x1b[0m')
                        CCoutFalse+=1
                        CEvt =True
                    if (CA+CB) !="XX": 
                        wa.CEvent(cname,ObjectsId,getE["path"],(CA+CB))
                        print('\x1b[1;32;40m'+"创建了"+ObjectsName+"音频"+ '\x1b[0m')
                        CCoutTrue+=1
                else:
                    print('\x1b[1;31;40m'+"检查此容器下命名："+ObjectsName+"   "+ObjectsPath+ '\x1b[0m')
                    CCoutFalse+=1
        elif ObjectsType=="Sound":
            CEvt = False
            CA = "P"
            CB = "S"
            if (("Play_"+cname) in oldEvents):
                print('\x1b[1;31;40m'+"Play_"+cname+"事件已存在|"+ObjectsPath+ '\x1b[0m')
                CCoutFalse+=1
                CEvt =True
            if (("Stop_"+cname) in oldEvents):
                print('\x1b[1;31;40m'+"Stop_"+cname+"事件已存在|"+ObjectsPath+ '\x1b[0m')
                CCoutFalse+=1
                CEvt =True
            if (CA+CB) !="XX":
                wa.CEvent(ObjectsName,ObjectsId,getE["path"],(CA+CB))
                print('\x1b[1;32;40m'+"创建了"+ObjectsName+"音频"+ '\x1b[0m')
                CCoutTrue+=1
    getD = wa.get_descendants(ObjectsId)['return']
    #print(getD)
    for i in getD:
        EventCh = wa.get_children(getE["id"])
        oldEvents=[]
        for e in EventCh["return"]:
            #print(e["name"])
            oldEvents.append(e["name"])
        #print(i["id"])
        if wa.Iscontainer(wa.get_parent(i["id"])[0]["id"])==False:
            if wa.Iscontainer(i["id"]):
                if wa.getchildrenCount(i["id"])>0:
                    #print(type(i))

                    if i["name"] == wa.getchildrenName(i["id"]):
                        cname=i["name"]
                    else:
                        cname=wa.extract_name(wa.getchildrenName(i["id"]))
                    print(wa.extract_name(wa.getchildrenName(i["id"])))
                    print(i["name"])
                    if i["name"] in wa.extract_name(wa.getchildrenName(i["id"])) :
                        CEvt = False
                        CA = "P"
                        CB = "S"
                        if (("Play_"+cname) in oldEvents):
                            print('\x1b[1;31;40m'+"Play_"+cname+"事件已存在|"+i["path"]+ '\x1b[0m')
                            CCoutFalse+=1
                            CEvt =True
                        if (("Stop_"+cname) in oldEvents):
                            print('\x1b[1;31;40m'+"Stop_"+cname+"事件已存在|"+i["path"]+ '\x1b[0m')
                            CCoutFalse+=1
                            CEvt =True
                        if (CA+CB) !="XX":  
                            wa.CEvent(cname,i['id'],getE["path"],(CA+CB))
                            CCoutTrue+=1
                            print('\x1b[1;32;40m'+"创建了"+i["name"]+"容器"+ '\x1b[0m')
                    else:
                        print('\x1b[1;32;40m'+"检查此容器下命名："+i["name"]+" |  "+i["path"]+ '\x1b[0m')
                        CCoutFalse+=1
            elif i["type"] =="Sound":
                #print(i)
                #print(wa.get_parent(i["id"])['id'])
                cname=i["name"]
                if wa.Iscontainer(wa.get_parent(i["id"])[0]["id"])==False:
                    CEvt = False
                    CA = "P"
                    CB = "S"
                    if (("Play_"+cname) in oldEvents):
                        print('\x1b[1;31;40m'+"Play_"+cname+"事件已存在|"+i["path"]+ '\x1b[0m')
                        CCoutFalse+=1
                        CEvt =True
                        CA = "X"
                    if (("Stop_"+cname) in oldEvents):
                        print('\x1b[1;31;40m'+"Stop_"+cname+"事件已存在|"+i["path"]+ '\x1b[0m')
                        CCoutFalse+=1
                        CEvt =True
                        CB = "X"
                    if (CA+CB) !="XX":   
                        wa.CEvent(i["name"],i['id'],getE["path"],(CA+CB))
                        print('\x1b[1;32;40m'+"创建了"+i["name"]+"音频"+ '\x1b[0m')
                        CCoutTrue+=1



wa.client.disconnect()
if CCoutFalse==0:
    print('\x1b[1;32;40m'+"全部创建成功"+ '\x1b[0m')
else:
    print('\x1b[1;33;40m'+ '\x1b[0m'+"创建完成,"+'\x1b[1;32;40m'+"成功："+'\x1b[0m'+str(CCoutTrue)+'\x1b[1;31;40m'+"|失败:"+'\x1b[0m'+str(CCoutFalse))
#input()