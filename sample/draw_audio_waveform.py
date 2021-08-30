import torch
import torchaudio
import requests
import numpy as np
import matplotlib.pyplot as plt


# url = "https://pytorch.org/tutorials/_static/img/steam-train-whistle-daniel_simon-converted-from-mp3.wav"
# r = requests.get(url)
#
# with open('steam-train-whistle-daniel_simon-converted-from-mp3.wav', 'wb') as f:
#     f.write(r.content)

sample_rate = 48000
time_interval = sample_rate

# 一. 读取原音频
filename = "../audio/mytestspeech.wav"
# Return the signal as a tensor and the sample rate，采样率为48000Hz，1秒音频的数组大小为48000
waveform, sample_rate = torchaudio.load(filename)

# 二. 对音频进行截取
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# t = torch.from_numpy(arr)
# # 1. 获取频率不为0的索引集合
# index = waveform[0, :].numpy()
# index_list = np.where(index < 0.00007, 0, index)
# index_list = np.mat(np.where(index_list == 0))
# j = index_list.shape[1]
# outcome_list = []
# a = index_list.tolist()[0]
# for i in range(1, j):
#     if a[i] - a[i-1] > sample_rate:
#         outcome_list.append(a[i])
#
# # 2. 通过二分法获取分段索引集合
# # list = torch.index_select(waveform, 1, torch.LongTensor([0, 3]))
#
# # 三. 保存截取后的音频
# torchaudio.save("a.wav", waveform, sample_rate=48000)

print("Shape of waveform: {}".format(waveform.size()))
print("Sample rate of waveform: {}".format(sample_rate))

plt.figure()

# 这里的t()相当于转置
plt.plot(waveform.t().numpy())
plt.show()