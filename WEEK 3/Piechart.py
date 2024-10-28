from matplotlib import pyplot as plt

users = [12, 32, 16, 45]
laptops = ["asus", "dell", "lenovo", "hp"] 
explode = [0, 0, 0, 0.08]
colors = ["g", "c", "aqua", "grey"]

plt.pie(users, labels=laptops, startangle=90, explode=explode, colors=colors, autopct='%1.2f%%')
plt.show()
