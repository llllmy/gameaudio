import WAAPI as wa

with wa.client:
    get = wa.get_audio_getSelectedObjects()
    for Objects in get:
            getD = wa.get_descendants(Objects["id"])['return']
            for i in getD:
                if wa.Iscontainer(i["id"])|(i["type"]=="Sound"):
                    wa.setVolume(i["id"], 0)

