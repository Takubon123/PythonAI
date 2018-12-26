
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#図5.4のプロット" data-toc-modified-id="図5.4のプロット-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>図5.4のプロット</a></span></li></ul></div>

# ##### 図5.4のプロット

# In[1]:


#計算とグラフプロットに必要なモジュールの読み込み
from control import matlab
from matplotlib import pyplot as plt
from scipy import arange 


# In[2]:


#パラメータの値を与える
T1 = 1 #T=1の場合
T2 = 20 #T=20の場合
T3 = 50 #T=50の場合

#伝達関数の分子・分母多項式を与える
num1 = [0, T1] #T=1の場合の分子多項式
den1 = [T1,1] #T=1の場合の分母多項式

num2 = [0, T2] #T=20の場合の分子多項式
den2 = [T2,1] #T=20の場合の分母多項式

num3 = [0, T3] #T=50の場合の分子多項式 
den3 = [T3,1] #T=50の場合の分母多項式

#伝達関数表現を与える
sys1 = matlab.tf(num1, den1) #T=1の場合の伝達関数表現 
sys2 = matlab.tf(num2, den2) #T=20の場合の伝達関数表現 
sys3 = matlab.tf(num3, den3) #T=50の場合の伝達関数表現 


# In[3]:


#時間変数の定義
t = arange(0, 50, 0.01) #0から50まで0.01刻み

#インパルス応答の計算
y1, t1 = matlab.impulse(sys1, t) #T=1の場合のインパルス応答
y2, t2 = matlab.impulse(sys2, t) #T=20の場合のインパルス応答
y3, t3 = matlab.impulse(sys3, t) #T=50の場合のインパルス応答

#図5.4のプロット
plt.plot(t1, y1, label = "T = 1") #インパルス応答をプロット
plt.plot(t2, y2, label = "T = 20") #インパルス応答をプロット
plt.plot(t3, y3, label = "T = 50") #インパルス応答をプロット
plt.xlim([0,50]) #横軸（時間軸）の範囲の指定
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0]) #縦軸の目盛りの値の設定
plt.grid(color='gray') #罫線を灰色で表示
plt.xlabel("time   t[s]") #横軸のラベル表示
plt.ylabel("y(t)=K/T e^{-t/T}") #縦軸のラベル表示
plt.legend() #凡例の表示
plt.show() #グラフの表示

