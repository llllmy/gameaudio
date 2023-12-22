import unreal

@unreal.uclass()
class UEEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class EditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

EditorUtility = UEEditorUtility()
EditorAsset = EditorAssetLibrary()

# 获取选中的资产

selectedAssets = EditorUtility.get_selected_assets()

# 遍历选中的资产并执行相应操作

for selectedAsset in selectedAssets:
    # 检查选中的资产是否为AkAudioEvent类型
    if str(type(selectedAsset)) == "<class 'AkAudioEvent'>":
        # 检查选中的资产是否缺少RequiredBank属性
        if selectedAsset.get_editor_property('RequiredBank') is None:
            # 检出资产
            EditorAsset.checkout_asset(selectedAsset.get_path_name())

