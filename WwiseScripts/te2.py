from waapi import WaapiClient
import re

client = WaapiClient(url="ws://127.0.0.1:8080/waapi")

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

    return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)

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
            "name","id","type","path"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)

get = get_audio_getSelectedObjects()['objects']

print(get_descendants(get[0]['id']))

client.disconnect()
#WorkUnit Folder ActorMi