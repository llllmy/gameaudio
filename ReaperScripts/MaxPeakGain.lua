count = reaper.CountSelectedMediaItems(0)
if count > 0 then
  for i=0, count-1 do
    item = reaper.GetSelectedMediaItem(0, i)
    Vol, maxPeakPos = reaper.NF_GetMediaItemMaxPeakAndMaxPeakPos(item)--获取MaxPeak值
    item_vol = reaper.GetMediaItemInfo_Value(item,"D_VOL")--获取对象音量
    MaxPeak = Vol+0.1--MaxPeak加0.1防止爆红
    gain = 10^(MaxPeak/20) --MaxPeak值转成音量倍数 
   reaper.SetMediaItemInfo_Value(item,"D_VOL",item_vol*(1/gain))--设置对象音量
  end
  reaper.UpdateArrange()--重绘排列视图
end
