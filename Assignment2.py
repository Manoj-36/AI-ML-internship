from matplotlib import colors, pyplot as plt
import pandas as pd

data = pd.read_csv('covid19.csv')

x1 = data.iloc[0:20,1].values
y1 = data.iloc[0:20,2].values

x2 = data.iloc[0:20,1].values
y2 = data.iloc[0:20,3].values

x3 = data.iloc[0:5,0].values
y3 = data.iloc[0:5,1].values
a3 = data.iloc[0:5,3].values

a4 = data.iloc[1,1:5].values
# b4 = data.iloc[0:0,2].values
# c4 = data.iloc[0:0,3].values
# d4 = data.iloc[0:0,4].values



plt.subplot(221)
plt.scatter(y1,x1)
plt.xlabel('confirmed')
plt.ylabel('deaths')

plt.subplot(222)
plt.plot(y2,x2,c='pink')
plt.xlabel('confirmed')
plt.ylabel('Recoverd')

plt.subplot(223)
plt.bar(x3,y3,width=0.5,label="recoverd",color="r")
plt.bar(x3,a3,width=0.9,alpha=0.5,label="Recoverd",color="g")
plt.xlabel('Recoverd,deaths')
plt.ylabel('Active')
plt.legend()


plt.subplot(224)
color = ['r','g','b','y']
activities = ['confirmed','Deaths','Recoverd','Active']
plt.pie(a4,labels=activities,colors=color,shadow=True,explode=(.1,.1,.1,.1),autopct='%1.2f%%')
plt.title('Covid19')


plt.show()