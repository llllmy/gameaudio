import WAAPI as wa

get = wa.get_audio_getSelectedObjects()
copyList=[]
ContainerList=[]
for Objects in get:
    #print(Objects["type"])

    if Objects["type"] == "Sound":
        copyList.append(Objects)
    if wa.Iscontainer(Objects["id"]):
        ContainerList.append(Objects)
for Container in ContainerList:
    print(Container["id"])
    for copy in copyList:
        print(copy["id"])
        wa.copyAudio(copy["id"],Container["id"])
#copyAudio()

#print(copyList)
wa.client.disconnect()