
-- 获取用户选择的文件夹路径
local userFolderPath = reaper.GetResourcePath() -- 默认为 Reaper 资源路径
local result,folderPath= reaper.GetUserInputs("导入Region", 1, "请输入文件夹路径", "")
local numRegions = reaper.CountProjectMarkers(0)

-- 处理用户选择的文件夹
if result then
    reaper.ShowConsoleMsg("选择的文件夹: " .. folderPath .. "\n")

    -- 获取文件夹下的所有文件
    local files = {}

    local sep = string.match(reaper.GetOS(), "Win") and "\\" or "/"
    local function enumerateFiles(directory)
        local fileIndex = 0
        local fileName = reaper.EnumerateFiles(directory, fileIndex)
        while fileName do
            local filePath = directory .. sep .. fileName
            if string.match(fileName, ".wav") then
                table.insert(files, filePath)
            end
            fileIndex = fileIndex + 1
            fileName = reaper.EnumerateFiles(directory, fileIndex)
        end
    end

    enumerateFiles(folderPath)
    local numFiles = #files
    reaper.ShowConsoleMsg((numFiles.."个音频符合条件 \n"))
    -- 输出文件列表
    
    local numins = 0
    for _, filePath in ipairs(files) do
        for i = 0, numRegions - 1 do
            local retval, isRegion, pos, rgnend, name, markrgnindexnumber = reaper.EnumProjectMarkers(i)
                -- 检查是否为区域
              if isRegion then
                -- 移动光标到指定位置
                reaper.SetEditCurPos(pos, true, true)
                local filename = string.match(filePath, "([^/\\]+)%.%w+$")
                if string.format(filename)==name then
                    reaper.InsertMedia(string.gsub(filePath, "\\", "/"),0)
                    reaper.ShowConsoleMsg(markrgnindexnumber.."  "..name.."\n")
                    numins=numins+1
               end   
           end
        end
    end
    reaper.ShowConsoleMsg("成功导入"..numins.."个")
end
