import WAAPI as wa
import os
import sys

def makefolder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def file_import(file_path,objectPath,sfxname,Folder_path):
    print(Folder_path)
    makefolder(Folder_path)
    args_import = {
        "importOperation": "createNew",
        "default": {
            "importLanguage": "SFX"
        },
        "imports": [{
            "audioFile": file_path,
            "objectPath": objectPath+"\\<Sound SFX> "+sfxname,
            "originalsSubFolder":Folder_path
        }],
        "autoAddToSourceControl": True
    }
    opts = {
        "platform": "Windows",
        "return": ["id", "name"]
    }
    return wa.client.call("ak.wwise.core.audio.import", args_import, options=opts)


def imp(ID,Fname,File,rfpath):
    for WAudio in wa.get_children(ID)["return"]:
        if WAudio["name"].lower() != Fname.lower():

            if wa.check_all_elements_in_string((WAudio["name"].lower()).split("_"), Fname.lower()):
                
                if wa.Iscontainer(WAudio["id"]):

                    if wa.check_if_children_are_containers(wa.get_children(WAudio["id"])):
                        imp(WAudio["id"],Fname,File,rfpath)
                    else:
                        Norepeat= True
                        for OldChild in wa.get_children(WAudio["id"])["return"]:

                            if OldChild["name"].replace(" ", "") == Fname.replace(" ", ""):
                                Norepeat= False
                                break
                        if Norepeat:
                            file_import(File,WAudio["path"],Fname,rfpath)
                elif WAudio["type"]=="Sound" :
                    None
                else:

                    imp(WAudio["id"],Fname,File,rfpath)
                    
        else:
            Norepeat= True
            for OldChild in wa.get_children(WAudio["id"])["return"]:
                if str(OldChild["name"]) == str(Fname):

                    Norepeat= False
                    break
            if Norepeat:
                file_import(File,WAudio["path"],Fname,rfpath)

            
if __name__ == "__main__":

    if len(sys.argv) > 2:
        param1 = sys.argv[1]
        param2 = sys.argv[2]
        print(f"接收到的参数: {param1} 和 {param2}")
    else:
        print("没有接收到参数")

    path = param1.replace("/", "\\")

    Dirlist, Filelist = wa.getAllSub(path)

    getid = wa.get_audio_getSelectedObjects()["objects"][0]["id"]
    getpath = wa.get_audio_getSelectedObjects()["objects"][0]["path"]

    selOriginals=param2
    for File in Filelist:

            part_to_remove = selOriginals.replace("/", '\\')
            
            # 替换路径部分为空字符串

            result_path = selOriginals.replace("/", '\\')+str(File).replace(path, '')

            rfpath=result_path[:result_path.rfind('\\')]

            rfpath = rfpath.replace(part_to_remove[:part_to_remove.rfind('\\')], '')

            imp(getid,str(os.path.basename(File)).rsplit('.',1)[0],File,rfpath)

wa.client.disconnect()