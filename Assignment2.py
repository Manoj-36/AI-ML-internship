from matplotlib import pyplot as plt
import pandas as pd

# reading the dataset from the csv file
data = pd.read_csv('covid19.csv')

# reading data
x1 = data.iloc[0:10,1].values
y1 = data.iloc[0:10,2].values
a1 = data.iloc[0:10,3].values
b1 = data.iloc[0:10,4].values

x2 = data.iloc[28:33,1].values
y2 = data.iloc[28:33,3].values
a2 = data.iloc[28:33,2].values
b2 = data.iloc[28:33,4].values



x3 = data.iloc[0:5,0].values
y3 = data.iloc[0:5,1].values
a3 = data.iloc[0:5,3].values

a4 = data.iloc[1,1:5].values


# scattering graph
plt.subplot(221)
plt.scatter(y1,x1,c='g',alpha=.5)
plt.scatter(a1,b1,c='r',alpha=.5)
plt.xlabel('confirmed & Recoverd')
plt.ylabel('deaths & active')

# plot graph
plt.subplot(222)
plt.plot(y2,x2,c='pink')
plt.plot(a2,b2,c='g')
plt.xlabel('confirmed & deaths')
plt.ylabel('Recoverd & active')

# bar graph
plt.subplot(223)
plt.bar(x3,y3,width=0.2,label="recoverd",color="r")
plt.bar(x3,a3,width=0.4,alpha=0.5,label="Recoverd",color="g")
plt.xlabel('Recoverd,deaths')
plt.ylabel('Active')
plt.legend()

# pie graph 
plt.subplot(224)
color = ['r','g','b','y']
activities = ['confirmed','Deaths','Recoverd','Active']
plt.pie(a4,labels=activities,colors=color,shadow=True,explode=(.1,.1,.1,.1),autopct='%1.2f%%')
plt.title('Covid19')


plt.show()