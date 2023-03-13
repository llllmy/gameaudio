cursorPos = reaper.GetCursorPosition()--获取光标位置；
count = reaper.CountSelectedMediaItems(0)--获取选定对象数量；
if count > 0 then
  for i=0, count-1 do
    item = reaper.GetSelectedMediaItem(0, i)
    rv, maxPeakPos = reaper.NF_GetMediaItemMaxPeakAndMaxPeakPos(item)--获取最大峰值位置，相对于对象开始位置；
   reaper.SetMediaItemInfo_Value(item,"D_POSITION",(cursorPos- maxPeakPos))--设置对象开始位置为光标位置减最大峰值位置。
  end
end

 
