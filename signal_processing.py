import numpy as np
import scipy.integrate as integrate
import scipy.special as special
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./01/1_raw_data_13-12_22.03.16.txt', sep='\s+') #double check why you have to set header as None
data['channel1'] = data['channel1'].apply(lambda x:x * 1000)
data['time'] = data['time'].apply(lambda x:x / 1000)

fig1 = plt.figure()
plt.subplot(9,1,1) #remember python reads it step by step since it is using an interpretation and talking about columns
plt.title('Emg Signals')
plt.plot(data['time'].to_numpy(), data['channel1'].to_numpy())
plt.ylabel('channel1')
plt.subplot(9,1,2)
plt.plot(data['time'].to_numpy(), data['channel2'].to_numpy())
plt.ylabel('channel2')
plt.subplot(9,1,3)
plt.plot(data['time'].to_numpy(), data['channel3'].to_numpy())
plt.ylabel('channel3')
plt.subplot(9,1,4)
plt.plot(data['time'].to_numpy(), data['channel4'].to_numpy())
plt.ylabel('channel4')
plt.subplot(9,1,5)
plt.plot(data['time'].to_numpy(), data['channel5'].to_numpy())
plt.ylabel('channel5')
plt.subplot(9,1,6)
plt.plot(data['time'].to_numpy(), data['channel6'].to_numpy())
plt.ylabel('channel6')
plt.subplot(9,1,7)
plt.plot(data['time'].to_numpy(), data['channel7'].to_numpy())
plt.ylabel('channel7')
plt.subplot(9,1,8)
plt.plot(data['time'].to_numpy(), data['channel8'].to_numpy())
plt.ylabel('channel8')
plt.subplot(9,1,9)
plt.plot(data['time'].to_numpy(), data['class'].to_numpy())
plt.ylabel('class')
plt.xlabel('time(s)')
plt.show()




















