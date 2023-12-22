import soundfile as sf 
import pyloudnorm as pyln
from pyloudnorm import IIRfilter
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def adjust_volume(input_file, output_file, volume_change):
    # 读取音频文件
    audio, sample_rate = sf.read(input_file)

    # 调整音量
    adjusted_audio = audio * (10 ** (volume_change / 20.0))

    # 写入调整后的音频文件
    sf.write(output_file, adjusted_audio, sample_rate)

# 创建一个隐藏的Tk窗口
root = Tk()
root.withdraw()

# 弹出选择文件夹对话框
folder_path = askdirectory()
root = Tk()
root.withdraw()

# 弹出选择文件夹对话框
folder_path2 = askdirectory()


input_path = folder_path #原始音频路径
output_path = folder_path2 #输出保存路径
filename = os.listdir(input_path) #遍历原始音频路径下所有文件名
a = float(input("目标响度："))
if a < 0:
    for file in filename:
        file_ext = os.path.splitext(file)[1]
        if file_ext.lower() == ".wav":
            #print(filename)
            audio, rate = sf.read(input_path + "\\" + file) 
            my_high_shelf = IIRfilter(5, 1, 3000, rate, 'high_shelf')
            my_peaking = IIRfilter(2, 2, 3000, rate, 'peaking')
            my_low_shelf = IIRfilter(3.5, 1, 400, rate, 'low_shelf')
            meter8 = pyln.Meter(rate, block_size=0.13)
            meter8._filters = {'my_high_shelf' : my_high_shelf, 'my_low_shelf' : my_low_shelf,'my_peaking' : my_peaking}
            loudness = meter8.integrated_loudness2(audio) 
            path1 = input_path + "\\" + file
            path2 = output_path + "\\" + file
            adjust_volume(path1, path2, a-loudness)
else:
    print("响度应为负数")