from matplotlib import pyplot as plt
import numpy as np
processor_name=["intel","AMD","snapdragon","tensor"]
use=[200,100,250,50]
plt.bar(processor_name,use,color='aqua',width=0.2)
plt.xlabel("processor_name"),
plt.ylabel("number of users")
plt.title("processors users in a community")
plt.show()

#pie cahrt
users = [12, 32, 16, 45]
laptops = ["asus", "dell", "lenovo", "hp"] 
explode = [0, 0, 0, 0.08]
colors = ["g", "c", "aqua", "grey"]

plt.pie(users, labels=laptops, startangle=90, explode=explode, colors=colors, autopct='%1.2f%%')
plt.show()




#bar chart
langs=('c','c++','java','python','php')
student=[23,17,35,29,12]
plt.bar(langs,student)
plt.show()

#line graph
emp_count=[3,20,50,200,350,400]
year=[2014,2015,2016,2017,2018,2019]
plt.plot(year,emp_count)
plt.show()
plt.savefig("Y:\AI and ML\lab manual ML\week 3\line.jpg")

#customize
plt.plot(year,emp_count,'o-r')
plt.xlabel("year")
plt.ylabel("emp_count")
plt.title ("EMPLOYEE GROWTH AT XYZ")
plt.show()

# customize
plt.plot(year,emp_count,'*--g')
plt.xlabel("year")
plt.ylabel("emp_count")
plt.title ("EMPLOYEE GROWTH AT XYZ")
plt.show()

#multilines
emp_counta=[3,10,540,240,300,440]
emp_countb=[3,20,50,200,350,400]
year=[2014,2015,2016,2017,2018,2019]

plt.plot(year,emp_counta,'o-r')
plt.xlabel("year")
plt.ylabel("employee")
plt.legend(['a','b'])
plt.show()

#histogram
x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()


#scatter plot
#saveplots
x=[2,3,4,5,6,7,4]
y=[8,8.5,9,9.5,10,10.5,11]
plt.scatter(x,y,label='Values of x&y',color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.savefig("scatterplot.jpg")







