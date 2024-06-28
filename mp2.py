import matplotlib.pyplot as mp
import numpy as np
'''
ages = [22,67,68,18,75,24,67,24,78,78,18,75]
bins = [0,10,20,30,40,50,60,70,80,90,100]

mp.hist(ages,bins,histtype='bar',rwidth=0.8)
mp.xlabel("bins")
mp.ylabel("ages")
mp.title("Age repetition")
'''
'''
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]
mp.scatter(x,y,label="scatter plot",color = 'red',marker='o',s=50)
mp.xlabel("x")
mp.ylabel("y")
mp.title("Scatter plot")
mp.legend(loc='upper right')
'''
'''
slices = [1,5,6,8,12,3,7]
activities = ['eating','sleeping','working','playing','workout','walking','swimming']
colors = ['c','m','r','b','g']
mp.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True)
mp.title("Pie chart")
'''
'''
days = [1,2,3,4,5]
eating = [2,3,2,3,2]
sleeping = [2,3,2,3,2]
working = [2,3,2,3,2]
playing = [2,3,2,3,2]

mp.plot([],[],color='m',label='Eating',linewidth = 5)
mp.plot([],[],color='c',label='Sleeping',linewidth = 5)
mp.plot([],[],color='r',label='Working',linewidth = 5)
mp.plot([],[],color='k',label='Playing',linewidth = 5)
mp.stackplot(days,eating,sleeping,working,playing,colors=['m','c','r','k'])
mp.xlabel("x")
mp.ylabel("y")
mp.title("Stack plot")
mp.legend(loc='upper right')
'''
mp.figure()
mp.subplot(221)
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)
mp.figure()
mp.subplot(221)
mp.plot(t1,f(t1),'bo')
mp.subplot(224)
mp.plot(t2,np.cos(2*np.pi*t2))

mp.show()