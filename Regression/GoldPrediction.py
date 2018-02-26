from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import fix_yahoo_finance as yf
from scipy.optimize import curve_fit


#
# # 预测对象为黄金ETF收盘价
# Df=yf.download('GLD','2008-01-01','2018-02-01')
# Df=Df[['Close']]
# Df=Df.dropna()
#

# # 特征提取 黄金矿工ETF-GDX 石油ETF-USO
# Df['S3']=Df['Close'].shift(1).rolling(window=3).mean()
# Df['S9']=Df['Close'].shift(1).rolling(window=9).mean()
# Df=Df.dropna()
#
#
# Df2=yf.download('GDX','2008-01-01','2018-02-01')
# Df2=Df2[['Close']]
# Df2=Df2.dropna()
# Df['S_GDX']=Df2['Close']
# Df=Df.dropna()
#
# Df3=yf.download('USO','2008-01-01','2018-02-01')
# Df3=Df3[['Close']]
# Df3=Df3.dropna()
# Df['S_USO']=Df3['Close']
# Df=Df.dropna()
# X=Df[['S3','S9','S_GDX','S_USO']]
# y=Df[['Close']]

# np.save('data.npy',[X,y])

X,y=np.load('data.npy')

t=.8
t=int(t*len(y))

# Train Data
X_train=X[:t]
y_train=y[:t]

# Test Data
X_test=X[t:]
y_test=y[t:]

linear=LinearRegression().fit(X_train,y_train)

predicted_price=linear.predict(X_test)
predicted_price=pd.DataFrame(predicted_price,index=y_test.index,columns=['price'])



plt.plot(predicted_price)
plt.plot(y_test)
labels=['predicted_price','actual_price']
plt.legend(labels)
plt.ylabel('Gold ETF Price')
plt.show()
r2_score=linear.score(X[t:],y[t:])*100
print(float('{0:.2f}'.format(r2_score)))

