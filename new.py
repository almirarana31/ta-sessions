import matplotlib.pyplot as plt

#list for storing x and y values
a=[]
b=[]

#loop to iterate through x values from -50 to 49
for x in range(-50,50,1):
    #calculating y value quadratically
    y=x**2+2*x+2
    #adding x and y to the lists
    a.append(x)
    b.append(y)


fig= plt.figure()
#determining rows and colums on grid
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()

