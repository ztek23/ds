import matplotlib.pyplot as mp
import numpy as np
'''
x = [1,2,3]
y = [1,2,3]

x1 = [2,4,16]
y1 = [3,9,81]

mp.plot(x,y,"r--",label="y = x",linewidth=4)
mp.plot(x1,y1,"b--",label="y = x^2",linewidth=4)
mp.xlabel("x-axis")
mp.ylabel("y-axis")
mp.legend(loc="upper right")
mp.title("Line Graph")
mp.show()
'''
#contstant = float(input("Enter the constant: "))
#slope = float(input("Enter the slope: "))

#x = np.linspace(-10,10,400)
#y = slope*x + contstant
'''
mp.plot(x,y,"r--",label="y = x",linewidth=4)
mp.xlabel("x-axis")
mp.ylabel("y-axis")
mp.legend(loc="upper right")
mp.title("Bar graph")
mp.show()
'''

mp.bar([1, 3, 5, 7], [2, 6, 4, 9], color='b')
mp.bar([2, 4, 6, 8], [3, 5, 7, 9], color='g')
mp.show()

mp.bar(["Male Literacy", "Female Literacy"], [90, 95])
mp.show()
