from pyAudioAnalysis import audioSegmentation
import scipy.io.wavfile as wav
import uuid
import os

filename = "../audio/speech_orig.wav"
(rate, sig) = wav.read(filename)
segments = audioSegmentation.silence_removal(sig, rate, 0.020, 0.020, smooth_window=0.5, weight=0.5)
true_segments = []
for i in range(len(segments)):
    if segments[i][1] - segments[i][0] > 5:
        start = int(segments[i][0] * rate)
        end = int(segments[i][1] * rate)
        true_segments.append([start, end])

filePath = str(uuid.uuid1())
os.mkdir('../audio/' + filePath)
for j in range(len(true_segments)):
    per_segmentation = sig[true_segments[j][0]: true_segments[j][1]]
    wav.write('../audio/' + filePath + '/segmentation' + str(j) + '.wav', rate, per_segmentation)