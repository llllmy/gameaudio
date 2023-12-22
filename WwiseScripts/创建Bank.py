import WAAPI as wa

def createBank(audioname,auidoid,parent,type1):

    audioname = audioname.replace(" ", "_")
    args = {
        "parent": parent,
        "type": "SoundBank",
        "name": "BNK_"+audioname,  
        "autoAddToSourceControl": True
    }
    return wa.client.call("ak.wwise.core.object.create", args)
def BankAdd(object,bankid):
    #print(bank)
    args_bank_add = {
            "soundbank": bankid,
            "operation": "add",
            "inclusions": [
                {
                    "object": object,
                    "filter": [
                        "events"
                    ]
                }
            ]
        }
    return wa.client.call("ak.wwise.core.soundbank.setInclusions", args_bank_add)


while True:
    
    Eve = False
    input('这条信息后选择事件(Events)位置后按Enter:')
    get = wa.get_audio_getSelectedObjects()
    for Objects in get:

        if Objects["path"][:6] != "\Event":
            Eve=True;
    if Eve:

        continue
    else:
        break

for Objects in get:

        cb =  createBank(Objects["name"],Objects["id"],r"\SoundBanks\Default Work Unit",Objects["type"])
        print(cb)
        BankAdd(Objects["id"],cb["id"])


               
wa.client.disconnect()

