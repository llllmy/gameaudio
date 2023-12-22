import WAAPI as wa

get = wa.get_audio_getSelectedObjects()

for Objects in get:
    descendants= wa.get_descendants(Objects["id"])
    for descendant in descendants["return"]:
        if descendant["type"] == "Sound":
            wa.setProperty(descendant["id"],10)
wa.client.disconnect()