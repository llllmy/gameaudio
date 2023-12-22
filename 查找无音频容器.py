from waapi import WaapiClient
from pprint import pprint
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
            "name","id","type","path"
        ]
    }

    client.call("ak.wwise.core.object.get", args, options=opts)["return"]
    
    handler = client.subscribe("ak.wwise.core.object.nameChanged", {"return": ["type"]})
    pprint(handler)
    for sfx in client.call("ak.wwise.core.object.get", args, options=opts)["return"]:
        None

        
        # if len(get_children(sfx["id"])["return"]) == 0:
        #     pprint(sfx["name"]+"        "+sfx["path"])
