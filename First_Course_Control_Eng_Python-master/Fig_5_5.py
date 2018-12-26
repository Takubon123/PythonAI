
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#図5.5のプロット" data-toc-modified-id="図5.5のプロット-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>図5.5のプロット</a></span></li></ul></div>

# ##### 図5.5のプロット

# In[1]:


#計算とグラフプロットに必要なモジュールの読み込み
from control import matlab
from matplotlib import pyplot as plt
from scipy import arange 


# In[2]:


#パラメータの値を与える．
T1 = 1 #T=1の場合
T2 = 5 #T=5の場合
T3 = 10 #T=10の場合

#伝達関数の分子・分母多項式を与える
num = [0, 1] #分子多項式
den1 = [T1, 1] #T=1の場合の分母多項式
den2 = [T2, 1] #T=5の場合の分母多項式
den3 = [T3, 1] #T=10の場合の分母多項式

#伝達関数表現を与える
sys1 = matlab.tf(num, den1) #T=1の場合の伝達関数表現 
sys2 = matlab.tf(num, den2) #T=5の場合の伝達関数表現  
sys3 = matlab.tf(num, den3) #T=10の場合の伝達関数表現  


# In[3]:


#時間変数の定義
t = arange(0, 50, 0.01) #0から10まで0.01刻み

#ステップ応答の計算
y1, t1 = matlab.step(sys1,t) #T=1の場合のステップ応答
y2, t2 = matlab.step(sys2,t) #T=5の場合のステップ応答
y3, t3 = matlab.step(sys3,t) #T=10の場合のステップ応答

#図5.6のプロット
plt.plot(t1, y1, label = "T = 1") #ステップ応答をプロット
plt.plot(t2, y2, label = "T = 5") #ステップ応答をプロット
plt.plot(t3, y3, label = "T = 10") #ステップ応答をプロット
plt.xlim([0,50]) #横軸（時間軸）の範囲の指定
plt.yticks([0,0.2,0.4,0.6,0.8,1.0]) #縦軸の目盛りの値の設定
plt.grid(color='gray') #罫線を灰色で表示
plt.xlabel("time   t[s]") #横軸のラベル表示
plt.ylabel("y(t) = 1 - e^{-t/T}") #縦軸のラベル表示
plt.legend() #凡例の表示
plt.show() #グラフの表示


# In[4]:


#図5.5をfor文を使ってプロット

t = arange(0, 50, 0.01) #0から50まで0.01刻み
for T in [1, 5, 10]: #Tを配列で与えるT = [1, 5, 10]
    y, t = matlab.step(matlab.tf([1],[T,1]), t) #Tの成分を1つ読み込みステップ応答を計算
    plt.plot(t, y) #ステップ応答をプロット
plt.xlim([0,50]) #横軸（時間軸の範囲の指定）
plt.ylim([0,1.2]) #縦軸（縦軸の範囲の指定）
plt.grid(color='gray') #罫線を灰色で表示
plt.xlabel("time   t[s]") #横軸のラベル表示
plt.ylabel("y(t) = 1 - e^{-t/T}") #縦軸のラベル表示
plt.legend(('T=1', 'T=5', 'T=10')) #凡例の表示
plt.show() #グラフの表示

