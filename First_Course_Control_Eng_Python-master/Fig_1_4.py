
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#図1.4のプロット" data-toc-modified-id="図1.4のプロット-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>図1.4のプロット</a></span></li></ul></div>

# ##### 図1.4のプロット

# In[1]:


#計算とグラフプロットに必要なモジュールの読み込み
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#パラメータの値を与える
a1 = -0.1 #a=-0.1の場合
a2 = -1.0 #a=-1.0の場合
a3 = -5.0 #a=-5.0の場合

#時間変数の定義
t = np.arange(0, 10, 0.01) #0から10まで0.01刻み

#y(t) = ext(at)の計算
y1 = np.exp(a1 * t) #a=-0.1の場合
y2 = np.exp(a2 * t) #a=-1．0の場合
y3 = np.exp(a3 * t) #a=-5.0の場合


# In[3]:


#図1.4のプロット
plt.plot(t, y1, label = "a = -0.1") #exp(at)の値をプロット
plt.plot(t, y2, label = "a = -1.0") #exp(at)の値をプロット
plt.plot(t, y3, label = "a = -5.0") #exp(at)の値をプロット
plt.xlim([0,10]) #横軸（時間軸）の範囲の指定
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0]) #縦軸の目盛りの値の設定
plt.grid(color='gray') #罫線を灰色で表示
plt.xlabel("time   t[s]") #横軸のラベル表示
plt.ylabel("output") #縦軸のラベル表示
plt.legend() #凡例の表示
plt.show() #グラフの表示

