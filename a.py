from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd 

data = pd.read_csv('covid19.csv')

x = data.iloc[0:10,3].values
y = data.iloc[0:10,0].values

# x1 = data.iloc[0:20,1].values
# y1 = data.iloc[0:20,0].values

# x=[1,2,3,4,5,6]
# y=[5,10,15,20,25,30]

plt.bar(x,y,label='x & y')
# plt.bar(x1,y1,label='x1 & y1')

plt.title('Covid 19')
plt.ylabel('Confirmed')
plt.xlabel('Deaths')
# plt.legend()

plt.show()
