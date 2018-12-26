
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#図5.2のプロット" data-toc-modified-id="図5.2のプロット-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>図5.2のプロット</a></span></li></ul></div>

# ##### 図5.2のプロット

# In[1]:


#計算とグラフプロットに必要なモジュールの読み込み
from control import matlab
from matplotlib import pyplot as plt
from scipy import arange 


# In[2]:


#伝達関数の分子・分母多項式を与える
num = [0, 1] #分子多項式
den1 = [3, 1] #T=3の場合の分母多項式
den2 = [8, 1] #T=8の場合の分母多項式
den3 = [15, 1] #T=15の場合の分母多項式

#伝達関数表現を与える
sys1 = matlab.tf(num, den1) #T=3の場合の伝達関数表現 
sys2 = matlab.tf(num, den2) #T=8の場合の伝達関数表現  
sys3 = matlab.tf(num, den3) #T=15の場合の伝達関数表現  


# In[3]:


#時間変数の定義
t = arange(0, 50, 0.01) #0から10まで0.01刻み

#ステップ応答の計算
y1, t1 = matlab.step(sys1,t) #T=3の場合のステップ応答
y2, t2 = matlab.step(sys2,t) #T=8の場合のステップ応答
y3, t3 = matlab.step(sys3,t) #T=15の場合のステップ応答

#図5.6のプロット
plt.plot(t1, y1, label = "y_a(t)") #ステップ応答をプロット
plt.plot(t2, y2, label = "y_b(t)") #ステップ応答をプロット
plt.plot(t3, y3, label = "y_c(t)") #ステップ応答をプロット
plt.xlim([0,50]) #横軸（時間軸)の範囲の指定
plt.ylim([0,1.2]) #縦軸の範囲の指定
plt.xticks([0,5,10,15,20,25,30,35,40,45,50]) #横軸の目盛りの値の設定
plt.grid(color='gray') #罫線を灰色で表示
plt.xlabel("time   t[s]") #横軸のラベル表示
plt.ylabel("y(t)") #縦軸のラベル表示
plt.legend() #凡例の表示
plt.show() #グラフの表示

